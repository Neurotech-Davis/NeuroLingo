import pygame
import sys
import time
import threading
import numpy as np
from pyOpenBCI import OpenBCICyton
from collections import deque
import pickle
import scipy.signal as signal
from mne.preprocessing import ICA
from mne import create_info, io
from sklearn.decomposition import PCA

# === Configuration ===
COM_PORT = 'COM8'
CHANNEL_COUNT = 8
SAMPLE_RATE = 255
EEG_WINDOW_SEC = 0.6
# Number of samples in analysis window
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)  # ~153
# Feature count = channels × samples (no padding needed)
N400_START_SAMPLES = 0
N400_END_SAMPLES   = EEG_WINDOW_SAMPLES + 1  # include endpoint ⇒ 154 samples
N400_CHANNELS     = list(range(CHANNEL_COUNT))
EXPECTED_FEATURES = len(N400_CHANNELS) * (N400_END_SAMPLES - N400_START_SAMPLES)
print(f"Expecting {EXPECTED_FEATURES} features ({len(N400_CHANNELS)} channels × {N400_END_SAMPLES} samples)")

WORD_DISPLAY_TIME = 1.5  # seconds
TRIAL_INTERVAL   = 8.0  # seconds

# === Load Model & Transforms ===
with open(r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl','rb') as f:
    model = pickle.load(f, fix_imports=True, encoding='latin1')
print("Loaded RF model classes:", model.classes_)
# Optional: load pre-fitted ICA & PCA
try:
    with open(r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/ica.pkl','rb') as f:
        ica = pickle.load(f)
    with open(r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/pca.pkl','rb') as f:
        pca = pickle.load(f)
    print("Loaded ICA & PCA objects from disk.")
except FileNotFoundError:
    print("[WARNING] ICA/PCA pickles not found; skipping transforms.")
    ica = pca = None

# === Data Buffer ===
eeg_buffer = deque(maxlen=EEG_WINDOW_SAMPLES+1)

# === Filters ===
def notch_filter(data, freq=60, fs=SAMPLE_RATE):
    b, a = signal.butter(3, [(freq-1.5)/(fs/2), (freq+1.5)/(fs/2)], btype='bandstop')
    return signal.filtfilt(b, a, data, axis=-1)


def bandpass_filter(data, low=1.0, high=30.0, fs=SAMPLE_RATE):
    b, a = signal.butter(5, [low/(fs/2), high/(fs/2)], btype='bandpass')
    return signal.filtfilt(b, a, data, axis=-1)

# === Sample Handler (Callback) ===
def handle_sample(sample):
    # Debugging: confirm callback is firing
    if len(eeg_buffer) == 0:
        print("[DEBUG] First EEG sample received")
    # convert raw to microvolts
    scaled = [ch * (4500000/24/(2**23-1)) for ch in sample.channels_data]
    eeg_buffer.append(scaled)
    if len(eeg_buffer) % 50 == 0:
        print(f"[DEBUG] EEG buffer length: {len(eeg_buffer)}/{EEG_WINDOW_SAMPLES+1}")

# === Stream Worker ===
def stream_worker():
    while True:
        try:
            board = OpenBCICyton(port=COM_PORT, daisy=False)
            board.start_stream(handle_sample)
            print(f"[INFO] Streaming from {COM_PORT}")
            break
        except Exception as e:
            print(f"[ERROR] EEG stream error: {e}. Retrying in 2s...")
            time.sleep(2)

threading.Thread(target=stream_worker, daemon=True).start()

# === Preprocessing ===
def preprocess_window(window):
    arr = np.array(window).T
    print(f"Raw arr size: {arr.shape}")
    # slice exactly the 0–600ms window (inclusive)
    arr = arr[N400_CHANNELS, N400_START_SAMPLES:N400_END_SAMPLES]
    print(f"Sliced arr size: {arr.shape}")
    arr = notch_filter(arr)
    arr = bandpass_filter(arr)
    if ica:
        arr = ica.apply(arr)
        print(f"After ICA, arr size: {arr.shape}")
    if pca:
        arr = pca.transform(arr.T).T
        print(f"After PCA, arr size: {arr.shape}")
    flat = arr.flatten()
    print(f"flat.size = {flat.size}, expected = {EXPECTED_FEATURES}")
    return flat.reshape(1, -1)

# === Pygame UI ===
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("EEG Understanding")
font = pygame.font.SysFont(None, 90)
small = pygame.font.SysFont(None, 90)
clock = pygame.time.Clock()
symbols = ["Cette","Pomme", "Fille", "Nous","Aimer","Aller"]
results = []

def draw(symbol, pred=None):
    screen.fill((30,30,30))
    screen.blit(font.render(symbol, True, (255,255,255)), (250,100))
    if pred is not None:
        label = "Understood" if pred == 0.0 else "Not Understood"
        color = (0,255,0) if pred == 0.0 else (255,100,100)
        screen.blit(small.render(label, True, color), (240,250))
    pygame.display.flip()

# === Main Loop ===
for i, sym in enumerate(symbols):
    # wait until buffer has enough samples
    while len(eeg_buffer) < EEG_WINDOW_SAMPLES+1:
        print(f"Buffer fill: {len(eeg_buffer)}/{EEG_WINDOW_SAMPLES+1}")
        time.sleep(0.0000001)
    draw(sym)
    time.sleep(WORD_DISPLAY_TIME)
    window = list(eeg_buffer)
    features = preprocess_window(window)
    pred = model.predict(features)[0]
    print(f"Prediction for {sym}: {pred}")
    results.append((sym, pred))
    draw(sym, pred)
    t0 = time.time()
    while time.time() - t0 < TRIAL_INTERVAL:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        clock.tick(30)

# === Summary ===
got = sum(1 for _,p in results if p == 0.0)
bad = sum(1 for _,p in results if p == 1.0)
screen.fill((10,10,10))
# Render texts
summary_text = font.render("Summary", True, (255, 255, 255))
understood_text = small.render(f"Understood: {got}", True, (0, 255, 0))
not_understood_text = small.render(f"Not Understood: {bad}", True, (255, 100, 100))

# Get rectangles and center them
summary_rect = summary_text.get_rect(center=(500, 100))
understood_rect = understood_text.get_rect(center=(500, 200))
not_understood_rect = not_understood_text.get_rect(center=(500, 300))

# Blit centered texts
screen.blit(summary_text, summary_rect)
screen.blit(understood_text, understood_rect)
screen.blit(not_understood_text, not_understood_rect)

pygame.display.flip()
time.sleep(6)
pygame.quit()
print("Done")