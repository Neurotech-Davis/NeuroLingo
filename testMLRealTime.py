import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pygame
import io
from PIL import Image

# -----------------------------
# Step 1: Load Time-Freq EEG CSV
# -----------------------------
csv_file = "C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/processed_EEG_data/clean_2025-02-23_14-24-48_1.csv"  # Replace with actual path
df = pd.read_csv(csv_file)

# Optional: Set axes (assumes rows = freq, cols = timepoints)
freqs = np.linspace(0.1, 30, df.shape[0])  # e.g. 7–30 Hz
times = np.linspace(0, 1, df.shape[1])   # e.g. 0–5 seconds over N columns

df.index = freqs
df.columns = np.round(times, 2)

# -----------------------------
# Step 2: Plot Seaborn Heatmap
# -----------------------------
plt.figure(figsize=(14, 6))

sns.heatmap(
    df,
    cmap='RdBu_r',
    center=0.0,
    vmin=-50, vmax=50,
    cbar_kws={'label': 'Amplitude (µV)'}
)

plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Frequency (Hz)", fontsize=12)
plt.title("EEG Time-Frequency Heatmap", fontsize=14)
plt.tight_layout()

# Save to buffer
buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
buf.seek(0)
plt.close()

# -----------------------------
# Step 3: Display with Pygame
# -----------------------------
img = Image.open(buf)
mode = img.mode
size = img.size
data = img.tobytes()

pygame.init()
pygame.display.set_caption("EEG Time-Frequency Heatmap")
screen = pygame.display.set_mode(size)
surface = pygame.image.fromstring(data, size, mode)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(surface, (0, 0))
    pygame.display.flip()

pygame.quit()
