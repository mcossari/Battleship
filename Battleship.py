import pygame
import random
# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battleship")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Grid variables
grid_size = 10
cell_size = screen_width // grid_size

def place_ship(grid, ship_length):
    placed = False
    while not placed:
        direction = random.choice(["horizontal", "vertical"])
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)

        if direction == "horizontal" and col + ship_length <= grid_size:
            # Check if space is available
            if all(grid[row][c] == 0 for c in range(col, col + ship_length)):
                # Place ship
                for c in range(col, col + ship_length):
                    grid[row][c] = 1
                placed = True

        elif direction == "vertical" and row + ship_length <= grid_size:
            if all(grid[r][col] == 0 for r in range(row, row + ship_length)):
                for r in range(row, row + ship_length):
                    grid[r][col] = 1
                placed = True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
        # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // cell_size
            row = mouse_y // cell_size
            print(f"Clicked on row {row}, col {col}")


    # Fill the screen with white
    screen.fill(WHITE)


    # Draw the grid
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, GRAY, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

    pygame.display.update()

pygame.quit()
