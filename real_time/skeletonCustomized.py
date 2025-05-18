# Running this on Chengyi's machine:
#   Use Anaconda Python3.11.1: conda activate NeuroLingo
#   Set API key: set COHERE_API_KEY={key}
import pygame
import pygame_gui
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
from mne.decoding import UnsupervisedSpatialFilter
import cohere
import re
import os
import json

# Andy
AndyML = r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/my_model.pkl'
AndyICA = r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/ica.pkl'
AndyPCA = r'C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/ml_model/pca.pkl'
AndyFont = "C:/Users/akim0/Documents/OpenBCI_GUI/NeuroLingo/realTime/NotoSansEthiopic-VariableFont_wdth,wght.ttf"

# Chengyi
ChengyiML = r'C:/Users/cheng/OneDrive/Desktop/NeuroLingo/ml_model/my_model.pkl'
ChengyiICA = r'C:/Users/cheng/OneDrive/Desktop/NeuroLingo/ml_model/ica.pkl'
ChengyiPCA = r'C:/Users/cheng/OneDrive/Desktop/NeuroLingo/ml_model/pca.pkl'
ChengyiFont = "C:/Users/cheng/OneDrive/Desktop/NeuroLingo/real_time/NotoSansEthiopic-VariableFont_wdth,wght.ttf"

# Set paths
pathML = ChengyiML
pathICA = ChengyiICA
pathPCA = ChengyiPCA
pathFont = ChengyiFont

# DEBUGGING
debugging = True

if not debugging:
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
    with open(AndyML,'rb') as f:
        model = pickle.load(f, fix_imports=True, encoding='latin1')
    print("Loaded RF model classes:", model.classes_)

    try:
        with open(AndyICA,'rb') as f:
            ica = pickle.load(f)
        with open(AndyPCA,'rb') as f:
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
                #board = OpenBCICyton(port=COM_PORT, daisy=False)
                #board.start_stream(handle_sample)
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

else:
    print("🤓 Debugging Mode Activated 🤓")
    WORD_DISPLAY_TIME = 1.5   # seconds
    DEBUGGING_WINDOW = 60 # seconds
    TRIAL_INTERVAL   = 2.0    # seconds NOTE: changed from 8 to 2 seconds
    def debugger_input(): 
        return input()
    debugger_thread = threading.Thread(target=debugger_input, daemon=True)

# === Pygame UI Setup ===
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
pygame.display.set_caption("EEG Understanding")
manager = pygame_gui.UIManager(screen.get_size())

font_path = pathFont
ethiopic_font = pygame.font.Font(font_path, 100)

font  = pygame.font.SysFont(None, 100) # Changed from 200 to 100 because my monitor isn't as big :/ -Chengyi
small = pygame.font.SysFont(None, 90)
clock = pygame.time.Clock()

title_font = pygame.font.SysFont(None, 60)

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

def draw(symbol, pred=None, translation=None):
    """Draw the word (and optionally the prediction)."""
    screen.fill((30,30,30))
    draw_text(symbol, ethiopic_font, (255,255,255), y_offset=-100)
    if pred is not None:
        label = "Understood" if pred == 0.0 else "Not Understood" # TODO: Confirm that 0 means understood.
        color = (0,255,0) if pred == 0.0 else (255,100,100)
        draw_text(label, small, color, y_offset=+50)
    if translation is not None:
        draw_text(translation, small, (255,255,255), y_offset=+200)
    pygame.display.flip()


def prompt_custom_symbols(screen, manager):
    """Prompts the user to enter words into the existing UI without resetting the screen."""
    
    screen_width, screen_height = screen.get_size()
    rect_width, rect_height = 700, 50

    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(
            ((screen_width - rect_width) // 2, (screen_height - rect_height) // 2),
            (rect_width, rect_height)
        ),
        manager=manager,
        object_id="#user_input"
    )

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    symbols = []
    running = True

    while running:
        screen.fill((30, 30, 30))  # Keep UI consistent
        draw_text("Enter words in 'word, translation' format, then press ENTER. To exit, type EXIT:", font, (255, 255, 255), y_offset=-150)

        UI_REFRESH_RATE = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#user_input":
                if event.text.upper() == "EXIT":
                    running = False
                else:
                    try:
                        sym = event.text.split(",")[0].strip()
                        translation = event.text.split(",")[1].strip()
                        symbols.append((sym, translation))
                        text_input.set_text('')  # Clear input field so user can enter more words
                    except:
                        running = False

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(screen)
        pygame.display.flip()

    return symbols  # Return collected words without quitting PyGame


def display_side_by_side(left_text, right_text): # Display function for learning phase
    
    # Colors
    BACKGROUND_COLOR = (30,30,30)
    TEXT_COLOR = (255,255,255)
    TITLE_COLOR = (100, 100, 100)

    # Screen
    screen.fill(BACKGROUND_COLOR)
    width, height = screen.get_size()

    # Title
    title = language
    title_render = title_font.render(title, True, TITLE_COLOR)
    title_rect = title_render.get_rect(center=(width // 2, 80))
    screen.blit(title_render, title_rect)

    # Words
    left_render = font.render(left_text, True, TEXT_COLOR)
    right_render = font.render(right_text, True, TEXT_COLOR)
    left_rect = left_render.get_rect(center=(width // 4, height // 2))
    right_rect = right_render.get_rect(center=(3 * width // 4, height // 2))

    screen.blit(left_render, left_rect)
    screen.blit(right_render, right_rect)

    pygame.display.flip()

def get_text_input(screen, manager):
    screen_width, screen_height = screen.get_size()
    rect_width, rect_height = 700, 50
    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(
            ((screen_width - rect_width) // 2, (screen_height - rect_height) // 2),
            (rect_width, rect_height)
        ),
        manager=manager,
        object_id="#user_input"
    )
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    entry = ""
    done = False
    while not done:
        screen.fill((30, 30, 30))  # Keep UI consistent
        draw_text("Enter the language you want to learn, then press ENTER:", font, (255, 255, 255), y_offset=-150)
        UI_REFRESH_RATE = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#user_input":
                entry = event.text
                done = True
            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(screen)
        pygame.display.flip()
    return entry

# === Cohere setup ===
co_key = os.getenv("COHERE_API_KEY")
if not co_key:
    sys.exit("Error: set COHERE_API_KEY environment variable.")
co = cohere.ClientV2(co_key)
def fetch_top_words(language):
    system = {"role": "system", "content": "You are a JSON-only assistant."}
    user = {"role": "user", "content": (
        f"List the 10 most important words to learn in {language}. "
        "Return exactly a JSON array of objects with keys 'word' and 'translation'."
    )}
    resp = co.chat(
        model="command-nightly",
        messages=[system, user],
        temperature=0.0,
        max_tokens=512
    )
    raw = "".join(chunk.text for chunk in resp.message.content).strip()
    raw = re.sub(r'^```[\w]*\n', '', raw)
    raw = re.sub(r'\n```$', '', raw)
    raw = re.sub(r'^json\n', '', raw, flags=re.IGNORECASE)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise ValueError(f"Failed to parse JSON: {e}\nRAW: {raw}")

# === Language Selection Menu ===
user_input = ""
screen.fill((30,30,30))
menu_text = """Choose a language to learn

Press '0' for Custom (manual)
Press '1' for Custom (AI) 
Press '2' for Amharic
Press '3' for Spanish
Press '4' for Italian
Press '5' for English"""
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
            if event.key == pygame.K_0:
                user_input = "MANUAL"
            elif event.key == pygame.K_1:
                user_input = "AI"
            elif event.key == pygame.K_2:
                user_input = "AMHARIC"
            elif event.key == pygame.K_3:
                user_input = "SPANISH"
            elif event.key == pygame.K_4:
                user_input = "ITALIAN"
            elif event.key == pygame.K_5:
                user_input = "ENGLISH"

# Default to AI if no choice
language = user_input or "AI"   
if language == "AMHARIC":
    symbols = [("ቮ", "cats"),("ዒ", "eager"),("ሀ", "salesman"), ("ሿ", "shopping"), ("ሜ", "artist")]
elif language == "ENGLISH":
    symbols = [("Apple", "Manzana"),("House", "Casa"),("Friend", "Amigo/a"), ("Learning", "Aprender"),("Python", "Python")]
elif language == "SPANISH":
    symbols = [("Casa", "House"),("Amigo", "Friend"), ("Libro", "Book"),("Aprender", "Learn")]
elif language == "ITALIAN":
    symbols = [("Ciao", "Hello/Goodbye"),("Amore", "Love"),("Mare", "Sea"),("Pizza", "Pizza")]
elif language == "MANUAL":
    symbols = prompt_custom_symbols(screen, manager)
    #print(symbols)
else: 
    custom_lang = get_text_input(screen, manager)
    items = fetch_top_words(custom_lang)
    print(items)
    syms = [it.get('word', '') for it in items]
    translations = {it.get('word', ''): it.get('translation', '') for it in items}
    symbols = list(translations.items())

# === Main learning loop ===
# Let the user know it is the learning phase
screen.fill((30,30,30))
menu_text = """Learning: 

Try your best to learn these symbols 
with their associating translation"""
y = 100
for line in menu_text.splitlines():
    surf = font.render(line, True, (255,255,255))
    rect = surf.get_rect(centerx=screen_rect.centerx, y=y)
    screen.blit(surf, rect)
    y += font.get_linesize()

# display an example of the learning phase
width, height = screen.get_size()
left_render = small.render("[symbol]", True, (100, 100, 100))
right_render = small.render("[translation]", True, (100, 100, 100))
left_rect = left_render.get_rect(center=(width // 4, height // 2))
right_rect = right_render.get_rect(center=(3 * width // 4, height // 2))
screen.blit(left_render, left_rect)
screen.blit(right_render, right_rect)
pygame.display.flip()

# Event handling for avoiding crashes
start_time = time.time()
while time.time() - start_time < 8:  # Keeping the delay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Iterate through symbols for learning
running = True
index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get word/translation pair
    pair = symbols[index % len(symbols)]
    sym = pair[0]
    translation = pair[1] 

    # show word + translation side by side
    display_side_by_side(sym, "")
    time.sleep(WORD_DISPLAY_TIME)
    display_side_by_side(sym, translation)
    time.sleep(WORD_DISPLAY_TIME)
    
    # Stop after 1 full loop
    if index == len(symbols) - 1:
        running = False

    # increment 
    index += 1

# === Main Trial Loop ===
# Let the user know it is the trial phase
screen.fill((10,10,10))
menu_text = """Testing: 

Sit comfortably and try not to blink or 
clench your jaw when a symbol pops up"""
y = 100
for line in menu_text.splitlines():
    surf = font.render(line, True, (255,255,255))
    rect = surf.get_rect(centerx=screen_rect.centerx, y=y)
    screen.blit(surf, rect)
    y += font.get_linesize()
pygame.display.update()

# Event handling to prevent crashes
start_time = time.time()
while time.time() - start_time < 8:  # Keeping the delay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Iterate through symbols for testing
results = []
for pair in symbols:

    # Get word/translation pair
    sym = pair[0]
    translation = pair[1] 

    # 1) fixation cross
    draw_plus()

    # 2) show word without prediction
    draw(sym)
    time.sleep(WORD_DISPLAY_TIME)

    # 3) collect & predict
    if not debugging:
        while len(eeg_buffer) < EEG_WINDOW_SAMPLES+1:
            time.sleep(0.001)
        window   = list(eeg_buffer)
        features = preprocess_window(window)
        pred     = model.predict(features)[0]
        results.append((sym, pred))
    else: # TODO: Debugging path
        t0 = time.time()
        recieved_input = ""
        while recieved_input == "" and time.time() - t0 < DEBUGGING_WINDOW:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        recieved_input = 'Y'
                    elif event.key == pygame.K_n:
                        recieved_input = 'N'
        if recieved_input is None:
            print("No input received. Continuing...")
            pred = 1.0  # Default to "Not Understood"
        else:
            pred = 0.0 if recieved_input == 'Y' else 1.0
        results.append((sym, pred))

    # 4) show word + prediction
    draw(sym, pred, translation)

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
