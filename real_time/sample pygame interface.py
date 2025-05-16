import pygame
import time

pygame.init()
pygame.font.init()

# Display setup
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Language Learning App")
font = pygame.font.SysFont(None, 120)
title_font = pygame.font.SysFont(None, 60)

# Define word pairs for multiple languages
language_pairs = {
    "English-Spanish": [
        ("hello", "hola"),
        ("thank you", "gracias"),
        ("goodbye", "adiós"),
        ("please", "por favor")
    ],
    "English-French": [
        ("hello", "bonjour"),
        ("thank you", "merci"),
        ("goodbye", "au revoir"),
        ("please", "s'il vous plaît")
    ],
    "English-German": [
        ("hello", "hallo"),
        ("thank you", "danke"),
        ("goodbye", "auf Wiedersehen"),
        ("please", "bitte")
    ]
}

# Ask user to choose language in terminal
print("Available languages:")
for i, lang in enumerate(language_pairs):
    print(f"{i + 1}. {lang}")
choice = int(input("Choose a language pair (number): "))
language_name = list(language_pairs.keys())[choice - 1]
word_pairs = language_pairs[language_name]

# Colors
BACKGROUND_COLOR = (240, 248, 255)
TEXT_COLOR = (30, 30, 30)
TITLE_COLOR = (100, 100, 100)

# Display function
def display_side_by_side(left_text, right_text, title=language_name):
    screen.fill(BACKGROUND_COLOR)

    # Title
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

# Main loop
running = True
index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    word, translation = word_pairs[index % len(word_pairs)]

    display_side_by_side(word, "")
    time.sleep(2)

    display_side_by_side(word, translation)
    time.sleep(2)

    index += 1

pygame.quit()