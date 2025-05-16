from pyOpenBCI import OpenBCICyton 
import numpy as np
import threading #allows multiple operations to run at once 
import pyqtgraph as pg #graphs to visualize data 
from pyqtgraph.Qt import QtWidgets, QtCore #handles GUI and event loops
import sys #
from collections import deque

# --- Constants ---
SCALE_FACTOR = (4500000) / 24 / (2**23 - 1)
CHANNEL_COUNT = 8
BUFFER_SIZE = 250 #can change, kept low to reduce historical data 

# --- Shared buffers for EEG channels ---
eeg_buffers = [deque([0]*BUFFER_SIZE, maxlen=BUFFER_SIZE) for _ in range(CHANNEL_COUNT)]

# --- PyQtGraph setup ---
app = QtWidgets.QApplication(sys.argv)
win = pg.GraphicsLayoutWidget(title="EEG Real-Time Viewer")
win.resize(1000, 600)
win.show()

plots = []
curves = []

for i in range(CHANNEL_COUNT):
    p = win.addPlot(title=f"Channel {i+1}")
    p.setYRange(-100, 100)
    c = p.plot(pen=pg.intColor(i))
    plots.append(p)
    curves.append(c)

# --- Function to update EEG buffer with each new sample ---
def handle_sample(sample):
    for i in range(CHANNEL_COUNT):
        value = sample.channels_data[i] * SCALE_FACTOR
        eeg_buffers[i].append(value)

# --- Start Cyton streaming thread ---
def start_stream():
    print("Starting Cyton stream...")
    board = OpenBCICyton(port='COM8', daisy=False)
    board.start_stream(handle_sample)

stream_thread = threading.Thread(target=start_stream)
stream_thread.daemon = True
stream_thread.start()

# --- Update the plot every 50 ms ---
def update_plot():
    for i in range(CHANNEL_COUNT):
        curves[i].setData(list(eeg_buffers[i]))

timer = QtCore.QTimer()
timer.timeout.connect(update_plot)
timer.start(50)

# --- Run the application ---
if __name__ == '__main__':
    QtWidgets.QApplication.instance().exec_()
