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

# === Setup ===
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)  # converts raw ADC units to microvolts
CHANNEL_COUNT = 8
SAMPLE_RATE = 255
BUFFER_SIZE = SAMPLE_RATE * 1  # 1 second of data for the buffer
# Initialize data buffer for each channel: a deque that holds up to BUFFER_SIZE recent samples
# holds one second worth of data, aka 255 samples of data
eeg_buffers = [deque(maxlen=BUFFER_SIZE) for _ in range(CHANNEL_COUNT)]


# === Callback: This runs every time a sample arrives ===
def handle_sample(sample):
    # for each channel
    for i in range(CHANNEL_COUNT):  
        # value = the ith channel data and scale it to make it microvolts
        value = sample.channels_data[i] * SCALE_FACTOR
        # at the matching channel in eeg_buffers, add the data
        eeg_buffers[i].append(value)



# === Stream Setup ===      I THINK THIS IS UNCESSARY, seems to have just served as a check
board = OpenBCICyton(port='COM8', daisy=False) # open connection to Cyton board on COMB
board.start_stream(handle_sample)     # BEGIN STREAMING, calls handle sample defined above per sample

# === Collect for 1 second ===
import time
time.sleep(1.0)  # Wait for buffer to fill with 1 second of data

# === Stop stream and disconnect ===
board.stop_stream()    # stop stream
board.disconnect()     # close the port from earlier



# === Convert to array ===
raw_epoch = np.array([list(buf) for buf in eeg_buffers])   # stack each channel's buffer, which is data, into an array
print(raw_epoch.shape)  # for confirmation should be 8x255 because 8 channels, buffer = 255 samples

# --- EEG Constants ---
EEG_WINDOW_SEC = 0.8                            # window to analyze
EEG_WINDOW_SAMPLES = int(SAMPLE_RATE * EEG_WINDOW_SEC)  # 255*0.8, makes sense. if the window was 1 there would be 255 samples
eeg_history = deque(maxlen=1000)   # record of timestamps

# --- Load ML Model ---
model_path = 'ml_model/my_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# --- EEG Filtering Functions ---
def notch_filter(val, data, fs=SAMPLE_RATE):
    notch_freq_Hz = np.array([float(val)])   # makes an array of just one value, the notch filter eg 60Hz
    for freq_Hz in np.nditer(notch_freq_Hz):
        bp_stop_Hz = freq_Hz + 3.0 * np.array([-1, 1])
        b, a = signal.butter(3, bp_stop_Hz / (fs / 2.0), 'bandstop')
        data = signal.lfilter(b, a, data)     # applies notch filter
    return data

def bandpass(start, stop, data, fs=SAMPLE_RATE):
    bp_Hz = np.array([start, stop])             # desired pass band
    b, a = signal.butter(5, bp_Hz / (fs / 2.0), btype='bandpass')
    return signal.lfilter(b, a, data, axis=0)   # apply bandpass across samples

def apply_ica(eeg_data):
    info = create_info(ch_names=[f'chan{i}' for i in range(CHANNEL_COUNT)], sfreq=SAMPLE_RATE, ch_types='eeg')
    raw = io.RawArray(eeg_data, info)   # RAW just like in preprocessing
    ica = ICA(n_components=CHANNEL_COUNT, random_state=42, max_iter=800)   # setting components to channel count? is this right?
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
    timestamp = time.time()     # current time in seconds
    # sample at ith channel, scale it for each channel
    scaled = [sample.channels_data[i] * SCALE_FACTOR for i in range(CHANNEL_COUNT)]
    eeg_history.append((timestamp, scaled))
    # append a tuple of timestampe and scaled data to eeg history

def start_stream():
    board = OpenBCICyton(port='COM8', daisy=False)  # starts stream
    board.start_stream(handle_sample)

# --- Start EEG thread ---
stream_thread = threading.Thread(target=start_stream)
stream_thread.daemon = True     # background stuff
stream_thread.start()           # start background data collection




# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((600, 400))   # create window
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
    screen.fill((30, 30, 30))    # dark grey background
    symbol_render = font.render(symbol, True, (255, 255, 255))  # white text
    screen.blit(symbol_render, (270, 100))  # coords for where to display

    if prediction:
        response_render = small_font.render(f"ML: {prediction}", True, (0, 255, 0)) # true or false
        screen.blit(response_render, (200, 250))

    pygame.display.flip()  # updates display

def get_next_symbol(index):
    base = symbols_data[index % len(symbols_data)]
    return base["symbol"]  # cycle through symbols list

# --- Main Loop ---
start_time = time.time()
symbol_index = 0
INTERVAL = 5
WORD_DISPLAY_TIME = 1  # CONSIDER SETTING THIS TO 0
TOTAL_DURATION = 60

while time.time() - start_time < TOTAL_DURATION:  # while we have't reached the total duration
    interval_start = time.time()
    symbol = get_next_symbol(symbol_index)
    response = None

    draw_screen(symbol)              # show new symbol
    time.sleep(WORD_DISPLAY_TIME)    # sleep forces code to wait before analyzing EEG THIS CAUSES A PROBLEM PROBABLY

    window = [s for t, s in eeg_history if interval_start <= t <= interval_start + EEG_WINDOW_SEC]
    # collect all EEG samples in the EEG_WINDOW_SEC after sleep

    if len(window) >= EEG_WINDOW_SAMPLES * 0.8: # if the window is more than 80% filled
        eeg_array = np.array(window).T

        for i in range(eeg_array.shape[0]):   # for each row in eeg_array apply the filters, ica, and pca
            eeg_array[i] = notch_filter(60, eeg_array[i])
        eeg_array = bandpass(0.1, 30, eeg_array)
        eeg_array = apply_ica(eeg_array)
        eeg_array = apply_pca(eeg_array)

        features = eeg_array.flatten().reshape(1, -1)  # gets features somehow, I don't think we should be doing this, data not trained this way
        # let's print out the shape of this to see if matches the dimensions of what the model needs
        prediction = model.predict(features)[0]  # also check the dimensions here to make sure it's right
        print(f"Prediction: {prediction}")
        response = prediction

    if response is not None:    # if the model classified something basically...
        draw_screen(symbol, prediction=response)
    else:
        draw_screen(symbol, prediction="No EEG")  # if model didn't classify there's something wrong with the data

    while time.time() - interval_start < INTERVAL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)

    symbol_index += 1

pygame.quit()
print("Done!")

## Issues 
# I'm not seeing code that gets you the summary of learned vs not learned
# dimensions for feeding it into the model may be wrong
# sleep early on in the code shouldn't be set to 1
# two instances of opening the board?
# handle sample was defined twice, with the second version overriding the second
#    should choose just one to run
# issue with ML and accuracy is probably with how the data is passed in
#    we should add print statements everywhere to see what dimension everything is in
