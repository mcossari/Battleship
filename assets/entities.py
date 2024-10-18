
import random
import pygame
from assets.sounds.sounds import win


def create_grid(grid_size):
    return [[0 for _ in range(grid_size)] for _ in range(grid_size)]



def draw_grid(grid, grid_size, WHITE, BLUE, RED, GRAY, cell_size, screen):
    for row in range(grid_size):
        for col in range(grid_size):
            # Draw empty water cells
            color = BLUE
            if grid[row][col] == 1:  # Ship (for debugging purposes, we'll make it blue)
                color = BLUE
            elif grid[row][col] == 2:  # Hit
                color = RED
            elif grid[row][col] == 3:  # Miss
                color = WHITE
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GRAY, (col * cell_size, row * cell_size, cell_size, cell_size), 1)



def place_ship(grid, ship_length, grid_size):
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


def check_victory(grid, grid_size):
    checker = 0
    total = 17
   # print(total)
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == 2:
                checker += 1
    if total == checker:

        print("Victory!")
        win()
        i = 0
        bool = True
        while bool:
            i = i + 1
            if i == 100000:
                bool = False
        return False
    else:
        return True


