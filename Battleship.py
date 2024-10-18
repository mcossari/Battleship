# Matt Cossari Python Project 10/15/2024

import pygame
from assets.entities import place_ship, create_grid, draw_grid, check_victory
from assets.sounds.sounds import splash, explode

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

grid = create_grid(grid_size)

place_ship(grid, 6, grid_size) # aircraft carrier
place_ship(grid, 2, grid_size) # Skiff
place_ship(grid, 4, grid_size) # Submarine
place_ship(grid, 5 , grid_size) # Battleship

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // cell_size
            row = mouse_y // cell_size
            # print(f"Clicked on row {row}, col {col}")
            if grid[row][col] == 1:
                print("Hit!")
                explode()
                grid[row][col] = 2
            elif grid[row][col] == 2:
                print("You've already hit this location!")
            elif grid[row][col] == 0:
                print("Miss!")
                splash()
                grid[row][col] = 3

    screen.fill(WHITE)

    #draw_ships(pass the coords of the ships somehow)
    draw_grid(grid, grid_size, WHITE, BLUE, RED, GRAY, cell_size, screen)

    running = check_victory(grid,grid_size)

    pygame.display.update()

pygame.quit()
