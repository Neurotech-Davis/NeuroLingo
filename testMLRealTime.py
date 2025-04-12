from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QTimer
import sys
import random
import time

# Word list
WORDS = ["apple", "xylophone", "pencil", "idea", "qwerty"]
WORD_INTERVAL_MS = 2000  # 2 seconds
current_word_time = None  # To sync EEG

class WordDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Display")
        self.setGeometry(100, 100, 400, 200)
        self.label = QLabel("", self)
        self.label.setGeometry(50, 50, 300, 100)
        self.label.setStyleSheet("font-size: 30px;")
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_word)
        self.timer.start(WORD_INTERVAL_MS)
        self.show()

    def show_word(self):
        global current_word_time
        word = random.choice(WORDS)
        current_word_time = time.time()
        self.label.setText(word)
        print(f"Showing word: {word}")
