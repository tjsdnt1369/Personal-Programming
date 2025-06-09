import pygame
import random

# Grid configuration
WIDTH, HEIGHT = 20, 20  # grid size
CELL_SIZE = 20  # pixel size of each grid cell
SCREEN_WIDTH, SCREEN_HEIGHT = WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Snake - Never Game Over")
clock = pygame.time.Clock()

# Precompute Hamiltonian cycle path (serpentine with wrapping)
path = []
for y in range(HEIGHT):
    if y % 2 == 0:
        for x in range(WIDTH):
            path.append((x, y))
    else:
        for x in reversed(range(WIDTH)):
            path.append((x, y))

# Snake state
snake = [(0, 0)]
path_index = 0

# Place food at random unoccupied cell
def new_food():
    available = [p for p in path if p not in snake]
    return random.choice(available) if available else None

food = new_food()

def draw_cell(pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move snake to next position in path
    path_index = (path_index + 1) % len(path)
    next_pos = path[path_index]
    snake.insert(0, next_pos)

    # Check if food eaten
    if food and snake[0] == food:
        food = new_food()
    else:
        snake.pop()  # remove tail if not growing

    screen.fill(BLACK)

    # Draw food
    if food:
        draw_cell(food, RED)

    # Draw snake
    for segment in snake:
        draw_cell(segment, GREEN)

    pygame.display.flip()
    clock.tick(10)  # 10 frames per second

pygame.quit()
