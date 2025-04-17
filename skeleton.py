import pygame
import sys
import time
import threading
import numpy as np
from pyOpenBCI import OpenBCICyton
from collections import deque
import pickle
from scipy import signal
from sklearn.decomposition import PCA
from mne.preprocessing import ICA
from mne import create_info, io

# === Constants ===
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)
CHANNEL_COUNT = 10
SAMPLE_RATE = 250
EEG_WINDOW_SEC = 0.8
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)
EXPECTED_FEATURES = 2456
N400_START_MS = 200
N400_END_MS = 600
N400_START_SAMPLES = int((N400_START_MS / 1000.0) * SAMPLE_RATE)
N400_END_SAMPLES = int((N400_END_MS / 1000.0) * SAMPLE_RATE)
eeg_history = deque(maxlen=3000)
board = None

# === Load ML Model ===
model_path = 'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
print("Model will predict one of these labels:", model.classes_)

# === EEG Filters ===
def notch_filter(freq, data, fs=250):
    bp_stop_Hz = freq + 3.0 * np.array([-1, 1])
    b, a = signal.butter(3, bp_stop_Hz / (fs / 2.0), 'bandstop')
    return signal.lfilter(b, a, data)

def bandpass(start, stop, data, fs=250):
    bp_Hz = np.array([start, stop])
    b, a = signal.butter(5, bp_Hz / (fs / 2.0), btype='bandpass')
    return signal.lfilter(b, a, data, axis=0)

def apply_ica(eeg_data):
    info = create_info([f'chan{i}' for i in range(eeg_data.shape[0])], sfreq=SAMPLE_RATE, ch_types='eeg')
    raw = io.RawArray(eeg_data, info)
    ica = ICA(n_components=eeg_data.shape[0], random_state=42, max_iter=1000)
    ica.fit(raw)
    raw = ica.apply(raw)
    return raw.get_data()

def apply_pca(data, n_components=6):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data.T).T

# === Sample Handler ===
def handle_sample(sample):
    scaled = [sample.channels_data[i] * SCALE_FACTOR for i in range(CHANNEL_COUNT)]
    eeg_history.append(scaled)

# === Start Stream Thread ===
def start_stream():
    global board
    try:
        board = OpenBCICyton(port='COM8', daisy=False)
        board.start_stream(handle_sample)
    except Exception as e:
        print(f"[ERROR] EEG stream failed: {e}")

stream_thread = threading.Thread(target=start_stream)
stream_thread.daemon = True
stream_thread.start()

# === Pygame Setup ===
pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("EEG Language Understanding")
font = pygame.font.SysFont("Arial", 60)
small_font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

symbols_data = [
    {"symbol": "Notebook"},
    {"symbol": "Glavune"},     # non-word
    {"symbol": "Window"},
    {"symbol": "Treldar"},     # non-word
    {"symbol": "Sunlight"},
    {"symbol": "Broshent"},    # non-word
    {"symbol": "Apple"},
    {"symbol": "Dranquil"},    # non-word
    {"symbol": "Rocket"},
    {"symbol": "Garden"}
]


results = []

def draw_screen(symbol, prediction=None):
    screen.fill((30, 30, 30))
    symbol_render = font.render(symbol, True, (255, 255, 255))
    screen.blit(symbol_render, (250, 100))
    if prediction:
        label = "Understood" if prediction == 1.0 else "Not Understood"
        response_render = small_font.render(f"ML: {label}", True, (0, 255, 0))
        screen.blit(response_render, (200, 250))
    pygame.display.flip()

def draw_summary(results):
    screen.fill((10, 10, 10))
    understood = sum(1 for r in results if r["prediction"] == 1.0)
    not_understood = sum(1 for r in results if r["prediction"] == 0.0)
    title = font.render("Summary", True, (255, 255, 255))
    summary1 = small_font.render(f"Understood: {understood}", True, (0, 255, 0))
    summary2 = small_font.render(f"Not Understood: {not_understood}", True, (255, 100, 100))
    screen.blit(title, (270, 60))
    screen.blit(summary1, (230, 160))
    screen.blit(summary2, (230, 220))
    pygame.display.flip()

def get_next_symbol(index):
    return symbols_data[index % len(symbols_data)]["symbol"]

# === Main Loop ===
symbol_index = 0
INTERVAL = 8
WORD_DISPLAY_TIME = 1.5

while symbol_index < len(symbols_data):
    interval_start = time.time()
    symbol = get_next_symbol(symbol_index)
    prediction_result = None
    draw_screen(symbol)
    time.sleep(WORD_DISPLAY_TIME)
    prediction_ready = False
    process_start = time.time()
    while not prediction_ready and time.time() - process_start < 4:
        if len(eeg_history) >= EEG_WINDOW_SAMPLES:
            raw_window = list(eeg_history)[-EEG_WINDOW_SAMPLES:]
            n400_window = raw_window[N400_START_SAMPLES:N400_END_SAMPLES]
            eeg_array = np.array(n400_window).T
            n400_channels = [3, 4, 5, 6, 7, 8]  # T7, T8, P7, P8, P3, P4
            eeg_array = eeg_array[n400_channels, :]
            for i in range(eeg_array.shape[0]):
                eeg_array[i] = notch_filter(60, eeg_array[i])
            eeg_array = bandpass(1.0, 30, eeg_array)
            eeg_array = apply_ica(eeg_array)
            eeg_array = apply_pca(eeg_array)
            features = eeg_array.flatten()
            if features.shape[0] < EXPECTED_FEATURES:
                padding = np.zeros(EXPECTED_FEATURES - features.shape[0])
                features = np.concatenate([features, padding])
            elif features.shape[0] > EXPECTED_FEATURES:
                features = features[:EXPECTED_FEATURES]
            features = features.reshape(1, -1)
            if features.shape[1] == EXPECTED_FEATURES:
                prediction_result = model.predict(features)[0]
                print(f"Prediction: {'Understood' if prediction_result == 1.0 else 'Not Understood'}")
                prediction_ready = True
            else:
                print(f"[ERROR] Feature mismatch: got {features.shape[1]}")
        else:
            print("Waiting for EEG buffer to fill...")
        time.sleep(0.1)
    results.append({"word": symbol, "prediction": prediction_result if prediction_ready else None})
    draw_screen(symbol, prediction=prediction_result if prediction_ready else "Buffering...")
    while time.time() - interval_start < INTERVAL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                if board:
                    board.stop_stream()
                sys.exit()
        clock.tick(30)
    symbol_index += 1

draw_summary(results)
time.sleep(6)
pygame.quit()
if board:
    board.stop_stream()
print("Done!")
