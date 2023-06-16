# Pygame setup
import pygame

pygame.init()

# Window setup
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)
DISPLAY = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("Window Caption")
FPS = 60
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 255, 255)
ROYAL_BLUE = (0, 128, 255)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
PINK = (255, 0, 255)
MAGENTA = (255, 0, 128)

# Clock setup
clock = pygame.time.Clock()

# Running loop begins
running = True

while running:
    DISPLAY.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        clock.tick(FPS)
    pygame.display.update()
pygame.quit()
