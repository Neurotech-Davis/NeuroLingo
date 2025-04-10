import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((600, 400)) #display screen
pygame.display.set_caption("Language Learning Test")

# Fonts
font = pygame.font.SysFont("Language/NotoSansEthiopic-VariableFont_wdth,wght.ttf", 60) #can upload font here to be able to show amharic 
small_font = pygame.font.SysFont(None, 40) #font for the choices
clock = pygame.time.Clock()

# Timing (in seconds)
SYMBOL_DISPLAY_TIME = 3
TOTAL_DURATION = 30

# Default response options
DEFAULT_UP = "I understand"
DEFAULT_DOWN = "I don't understand"

# Symbol list
symbols_data = [
    {"symbol": "ሂ"},
    {"symbol": "ቁ"},
    {"symbol": "ኙ"},
    #To override if needed{"symbol": "", "up": "I know this!", "down": "No clue"},
]

# Function to draw a screen with the symbol and options
def draw_screen(symbol, up_option, down_option):
    screen.fill((30, 30, 30))  # background color

    # Render text
    symbol_render = font.render(symbol, True, (255, 255, 255))
    up_render = small_font.render(f"↑ {up_option}", True, (100, 200, 255))
    down_render = small_font.render(f"↓ {down_option}", True, (255, 100, 100))

    # Draw to screen
    screen.blit(symbol_render, (270, 100))
    screen.blit(up_render, (200, 200))
    screen.blit(down_render, (200, 250))

    pygame.display.flip()

# Get symbol with defaults filled in
def get_next_symbol(index):
    base = symbols_data[index % len(symbols_data)]
    return {
        "symbol": base["symbol"],
        "up": base.get("up", DEFAULT_UP),
        "down": base.get("down", DEFAULT_DOWN)
    }

# Start timing
start_time = time.time()
symbol_index = 0

# Main loop
while time.time() - start_time < TOTAL_DURATION:
    current_data = get_next_symbol(symbol_index)
    draw_screen(current_data["symbol"], current_data["up"], current_data["down"])

    symbol_start = time.time()
    response = None

    while time.time() - symbol_start < SYMBOL_DISPLAY_TIME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    response = current_data["up"]
                    print(f"You chose: {response}")
                    break
                elif event.key == pygame.K_DOWN:
                    response = current_data["down"]
                    print(f"You chose: {response}")
                    break
        if response:
            break
        clock.tick(30)

    symbol_index += 1

pygame.quit()
print("Done!")
