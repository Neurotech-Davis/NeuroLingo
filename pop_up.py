import tkinter as tk
import random
from datetime import datetime

symbols = [
    {"symbol": "ቮ"}, {"symbol": "ተ"}, {"symbol": "ቺ"}, {"symbol": "ኇ"}, {"symbol": "ነ"}, {"symbol": "ኟ"},
    {"symbol": "አ"}, {"symbol": "ዒ"}, {"symbol": "ዞ"}, {"symbol": "የ"}, {"symbol": "ገ"}, {"symbol": "ጵ"},
    {"symbol": "ኈ"}, {"symbol": "ኴ"}, {"symbol": "ዄ"}, {"symbol": "ጕ"}, {"symbol": "፠"}, {"symbol": "፫"},
    {"symbol": "፸"}, {"symbol": "ሀ"}, {"symbol": "ሊ"}, {"symbol": "ሧ"}, {"symbol": "ቅ"}, {"symbol": "ቤ"},
    {"symbol": "ሐ"}, {"symbol": "ሜ"}, {"symbol": "ሣ"}, {"symbol": "ሯ"}, {"symbol": "ሴ"}, {"symbol": "ሿ"},
    {"symbol": "ቃ"}, {"symbol": "ብ"}, {"symbol": "ቬ"}, {"symbol": "ት"}, {"symbol": "ቾ"}, {"symbol": "ኃ"},
    {"symbol": "ና"}, {"symbol": "ኞ"}, {"symbol": "ኧ"}, {"symbol": "ኬ"}, {"symbol": "ኼ"}, {"symbol": "ው"},
    {"symbol": "ዐ"}, {"symbol": "ዥ"}, {"symbol": "ዚ"}, {"symbol": "ያ"}, {"symbol": "ፗ"}, {"symbol": "ቈ"},
]

class SymbolFlasher:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root, font=("Arial", 100))
        self.label.pack(expand=True)

        self.time_label = tk.Label(root, font=("Arial", 14))
        self.time_label.pack()

        self.state = "cross"  # start with focus cross
        self.start_flash_loop()

    def start_flash_loop(self):
        if self.state == "cross":
            self.label.config(text="+", fg="black")
            self.time_label.config(text="")
            self.state = "symbol"
        else:
            chosen = random.choice(symbols)["symbol"]
            now = datetime.now().strftime("%H:%M:%S")
            self.label.config(text=chosen, fg="blue")
            self.time_label.config(text=f"Time: {now}")
            self.state = "cross"

        # call this method again after 1000 milliseconds (1 second)
        self.root.after(1000, self.start_flash_loop)

# Main window setup
root = tk.Tk()
root.title("Auto Symbol Display")
root.geometry("400x250")

flasher = SymbolFlasher(root)
root.mainloop()