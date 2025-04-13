import pygame
import sys
import time
import threading
import joblib
import numpy as np
from pyOpenBCI import OpenBCICyton
from collections import deque
import pickle
from scipy import signal
from sklearn.decomposition import PCA
from mne.preprocessing import ICA
from mne import create_info, io

# --- EEG Constants ---
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)
CHANNEL_COUNT = 8
SAMPLE_RATE = 250
EEG_WINDOW_SEC = 0.8
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)
eeg_history = deque(maxlen=1000)

# --- Load ML Model ---
model_path = 'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# --- EEG Filtering Functions ---
def notch_filter(val, data, fs=250):
    notch_freq_Hz = np.array([float(val)])
    for freq_Hz in np.nditer(notch_freq_Hz):
        bp_stop_Hz = freq_Hz + 3.0 * np.array([-1, 1])
        b, a = signal.butter(3, bp_stop_Hz / (fs / 2.0), 'bandstop')
        data = signal.lfilter(b, a, data)
    return data

def bandpass(start, stop, data, fs=250):
    bp_Hz = np.array([start, stop])
    b, a = signal.butter(5, bp_Hz / (fs / 2.0), btype='bandpass')
    return signal.lfilter(b, a, data, axis=0)

def apply_ica(eeg_data):
    info = create_info(ch_names=[f'chan{i}' for i in range(CHANNEL_COUNT)], sfreq=SAMPLE_RATE, ch_types='eeg')
    raw = io.RawArray(eeg_data, info)
    ica = ICA(n_components=CHANNEL_COUNT, random_state=42, max_iter=800)
    ica.fit(raw)
    ica.detect_artifacts(raw)
    ica.apply(raw)
    return raw.get_data()

def apply_pca(data, n_components=8):
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(data.T).T
    return reduced_data

# --- Handle EEG samples from OpenBCI ---
def handle_sample(sample):
    timestamp = time.time()
    scaled = [sample.channels_data[i] * SCALE_FACTOR for i in range(CHANNEL_COUNT)]
    eeg_history.append((timestamp, scaled))

def start_stream():
    board = OpenBCICyton(port='COM8', daisy=False)
    board.start_stream(handle_sample)

# --- Start EEG thread ---
stream_thread = threading.Thread(target=start_stream)
stream_thread.daemon = True
stream_thread.start()

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Language Learning Test")
font = pygame.font.SysFont("Arial", 60)
small_font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

# --- Configuration ---
symbols_data = [
    {"symbol": "Computer"},
    {"symbol": "Water"},
    {"symbol": "Cmaflr"},
    {"symbol": "Amazing"},
    {"symbol": "Moasdut"},
]

def draw_screen(symbol, prediction=None):
    screen.fill((30, 30, 30))
    symbol_render = font.render(symbol, True, (255, 255, 255))
    screen.blit(symbol_render, (270, 100))

    if prediction:
        response_render = small_font.render(f"ML: {prediction}", True, (0, 255, 0))
        screen.blit(response_render, (200, 250))

    pygame.display.flip()

def get_next_symbol(index):
    base = symbols_data[index % len(symbols_data)]
    return base["symbol"]

# --- Main Loop ---
start_time = time.time()
symbol_index = 0
INTERVAL = 5
WORD_DISPLAY_TIME = 1
TOTAL_DURATION = 60

while time.time() - start_time < TOTAL_DURATION:
    interval_start = time.time()
    symbol = get_next_symbol(symbol_index)
    response = None

    draw_screen(symbol)
    time.sleep(WORD_DISPLAY_TIME)

    window = [s for t, s in eeg_history if interval_start <= t <= interval_start + EEG_WINDOW_SEC]
    if len(window) >= EEG_WINDOW_SAMPLES * 0.8:
        eeg_array = np.array(window).T

        for i in range(eeg_array.shape[0]):
            eeg_array[i] = notch_filter(60, eeg_array[i])
        eeg_array = bandpass(0.1, 30, eeg_array)
        eeg_array = apply_ica(eeg_array)
        eeg_array = apply_pca(eeg_array)

        features = eeg_array.flatten().reshape(1, -1)
        prediction = model.predict(features)[0]
        print(f"Prediction: {prediction}")
        response = prediction

    if response is not None:
        draw_screen(symbol, prediction=response)
    else:
        draw_screen(symbol, prediction="No EEG")

    while time.time() - interval_start < INTERVAL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)

    symbol_index += 1

pygame.quit()
print("Done!")
