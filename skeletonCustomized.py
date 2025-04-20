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
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)  # ~153 samples
N400_START_SAMPLES = 0
N400_END_SAMPLES   = EEG_WINDOW_SAMPLES + 1            # 154 samples
N400_CHANNELS     = list(range(CHANNEL_COUNT))
EXPECTED_FEATURES = len(N400_CHANNELS) * (N400_END_SAMPLES - N400_START_SAMPLES)
WORD_DISPLAY_TIME = 1.5   # seconds
TRIAL_INTERVAL   = 8.0    # seconds

print(f"Expecting {EXPECTED_FEATURES} features ({len(N400_CHANNELS)} channels × {N400_END_SAMPLES} samples)")

# === Load Model & Transforms ===
with open(r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl','rb') as f:
    model = pickle.load(f, fix_imports=True, encoding='latin1')
print("Loaded RF model classes:", model.classes_)

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

# === Sample Handler ===
def handle_sample(sample):
    if len(eeg_buffer) == 0:
        print("[DEBUG] First EEG sample received")
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
    arr = arr[N400_CHANNELS, N400_START_SAMPLES:N400_END_SAMPLES]
    arr = notch_filter(arr)
    arr = bandpass_filter(arr)
    if ica:
        arr = ica.apply(arr)
    if pca:
        arr = pca.transform(arr.T).T
    flat = arr.flatten()
    return flat.reshape(1, -1)

# === Pygame UI Setup ===
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
pygame.display.set_caption("EEG Understanding")

font  = pygame.font.SysFont(None, 90)
small = pygame.font.SysFont(None, 90)
clock = pygame.time.Clock()

def draw_text(text, surf_font, color, y_offset=0):
    """Render centered text with a vertical offset."""
    surf = surf_font.render(text, True, color)
    rect = surf.get_rect(center=screen_rect.center)
    rect.centery += y_offset
    screen.blit(surf, rect)

def draw_plus():
    """Show a fixation '+' for 1 second."""
    screen.fill((30,30,30))
    draw_text("+", font, (200,200,200), y_offset=0)
    pygame.display.flip()
    time.sleep(1)

def draw(symbol, pred=None):
    """Draw the word (and optionally the prediction)."""
    screen.fill((30,30,30))
    draw_text(symbol, font, (255,255,255), y_offset=-100)
    if pred is not None:
        label = "Understood" if pred == 0.0 else "Not Understood"
        color = (0,255,0) if pred == 0.0 else (255,100,100)
        draw_text(label, small, color, y_offset=+50)
    pygame.display.flip()

# === Language Selection Menu ===
user_input = ""
screen.fill((30,30,30))
menu_text = """Choose a language to learn
Up = French
Down = English
Left = Spanish
Right = Italian"""
y = 100
for line in menu_text.splitlines():
    surf = font.render(line, True, (255,255,255))
    rect = surf.get_rect(centerx=screen_rect.centerx, y=y)
    screen.blit(surf, rect)
    y += font.get_linesize()
pygame.display.flip()

# Wait up to 10s or until a key is pressed
start = time.time()
while user_input == "" and time.time() - start < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user_input = "FRENCH"
            elif event.key == pygame.K_DOWN:
                user_input = "ENGLISH"
            elif event.key == pygame.K_LEFT:
                user_input = "SPANISH"
            elif event.key == pygame.K_RIGHT:
                user_input = "ITALIAN"

# Default to Italian if no choice
language = user_input or "ITALIAN"
if language == "FRENCH":
    symbols = ["Cette","Pomme","Fille","Nous","Aimer","Aller"]
elif language == "ENGLISH":
    symbols = ["Apple","House","Friend","Learning","Python"]
elif language == "SPANISH":
    symbols = ["Casa","Amigo","Libro","Aprender"]
else:
    symbols = ["Ciao","Amore","Mare","Pizza"]

results = []

# === Main Trial Loop ===
for sym in symbols:
    # 1) fixation cross
    draw_plus()

    # 2) show word without prediction
    draw(sym)
    time.sleep(WORD_DISPLAY_TIME)

    # 3) collect & predict
    while len(eeg_buffer) < EEG_WINDOW_SAMPLES+1:
        time.sleep(0.001)
    window   = list(eeg_buffer)
    features = preprocess_window(window)
    pred     = model.predict(features)[0]
    results.append((sym, pred))

    # 4) show word + prediction
    draw(sym, pred)

    # 5) inter-trial interval
    t0 = time.time()
    while time.time() - t0 < TRIAL_INTERVAL:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        clock.tick(30)

# === Summary Screen ===
got = sum(1 for _,p in results if p == 0.0)
bad = sum(1 for _,p in results if p == 1.0)

screen.fill((10,10,10))
draw_text("Summary", font, (255,255,255), y_offset=-100)
draw_text(f"Understood: {got}", small, (0,255,0), y_offset=20)
draw_text(f"Not Understood: {bad}", small, (255,100,100), y_offset=100)
pygame.display.flip()
time.sleep(6)

pygame.quit()
print("Done")
