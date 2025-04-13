import pygame
import sys
import time
import threading
import joblib
import numpy as np
from pyOpenBCI import OpenBCICyton
from collections import deque
import pickle 











# --- EEG Constants ---
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)
CHANNEL_COUNT = 8
SAMPLE_RATE = 250  # adjust if different
EEG_WINDOW_SEC = 0.8
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)
eeg_history = deque(maxlen=1000)  # stores (timestamp, [channel_values])

# --- Load ML Model ---
model_path = 'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl'  # make sure this is trained properly
with open(model_path, 'rb') as file:
    model = pickle.load(file)

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
font = pygame.font.SysFont("NotoSansEthiopic-VariableFont_wdth,wght.ttf", 60) #Not working 
small_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

# --- Configuration ---
SYMBOL_DISPLAY_TIME = 3
TOTAL_DURATION = 30

symbols_data = [
    {"symbol": "ሂ"},
    {"symbol": "ቁ"},
    {"symbol": "ኙ"},
    # Add more as needed
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

while time.time() - start_time < TOTAL_DURATION:
    symbol = get_next_symbol(symbol_index)
    draw_screen(symbol)
    symbol_start = time.time()
    response = None

    while time.time() - symbol_start < SYMBOL_DISPLAY_TIME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if it's time to extract EEG window
        if not response and time.time() - symbol_start >= EEG_WINDOW_SEC:
            window = [s for t, s in eeg_history if symbol_start <= t <= symbol_start + EEG_WINDOW_SEC]
            if len(window) >= EEG_WINDOW_SAMPLES * 0.8:
                eeg_array = np.array(window).T  # shape: (channels, timepoints)
                features = eeg_array.flatten().reshape(1, -1)
                prediction = model.predict(features)[0]
                print(f"Prediction: {prediction}")
                response = prediction
                draw_screen(symbol, prediction)

        clock.tick(30)

    symbol_index += 1

pygame.quit()
print("Done!")
