from pyOpenBCI import OpenBCICyton
from collections import deque
import numpy as np

# === Setup ===
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)
CHANNEL_COUNT = 8
SAMPLE_RATE = 250
BUFFER_SIZE = SAMPLE_RATE * 1  # 1 second of data
# Initialize data buffer for each channel
eeg_buffers = [deque(maxlen=BUFFER_SIZE) for _ in range(CHANNEL_COUNT)]
# === Callback: This runs every time a sample arrives ===
def handle_sample(sample):
    for i in range(CHANNEL_COUNT):
        value = sample.channels_data[i] * SCALE_FACTOR
        eeg_buffers[i].append(value)
# === Stream Setup ===
board = OpenBCICyton(port='COM8', daisy=False)
board.start_stream(handle_sample)
# === Collect for 1 second ===
import time
time.sleep(1.0)  # Wait for buffer to fill with 1 second of data
# === Stop stream and disconnect ===
board.stop_stream()
board.disconnect()
# === Convert to array ===
raw_epoch = np.array([list(buf) for buf in eeg_buffers])  # shape: (8, 250)
print(raw_epoch.shape)  # for confirmation