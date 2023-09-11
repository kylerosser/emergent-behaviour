import pygame
from config import *
from ant import *

running = True
foraging_pheromone = [[0 for y in range(CELLS_Y)] for x in range(CELLS_X)]
retreating_pheromone = [[0 for y in range(CELLS_Y)] for x in range(CELLS_X)]
food = [[False for y in range(CELLS_Y)] for x in range(CELLS_X)]
ants = []

pygame.init()

screen = pygame.display.set_mode((CELLS_X * PIXELS_PER_CELL, CELLS_Y * PIXELS_PER_CELL))
pygame.display.set_caption('Ant Colony Simulation')

clock = pygame.time.Clock()

def default_values():
    food[0] = [True for y in range(CELLS_Y)]
    food[1] = [True for y in range(CELLS_Y)]
    food[2] = [True for y in range(CELLS_Y)]
    food[3] = [True for y in range(CELLS_Y)]
    food[4] = [True for y in range(CELLS_Y)]
    food[5] = [True for y in range(CELLS_Y)]

def generate_ants():
    global ants
    for x in range(ANT_COUNT):
        ants.append(Ant(CELLS_X // 2, CELLS_Y // 2))

def update_ants():
    for ant in ants:
        ant.update(foraging_pheromone, retreating_pheromone, food)

def blur_cells_1(cells):
    new_cells = [[0 for y in range(CELLS_Y)] for x in range(CELLS_X)]
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            sum = cells[x][y]
            neighbor_count = 0
            for neighbor_x in range(x - 1, x + 2, 1):
                for neighbor_y in range(y - 1, y + 2, 1):
                    if neighbor_x >= CELLS_X or neighbor_x < 0:
                        continue
                    if neighbor_y >= CELLS_Y or neighbor_y < 0:
                        continue
                    if neighbor_y == y and neighbor_x == x:
                        continue

                    sum += cells[neighbor_x][neighbor_y] * DIFFUSE_FACTOR
                    neighbor_count += 1
            
            average = sum / (DIFFUSE_FACTOR * neighbor_count + 1 + DECAY_FACTOR)
            new_cells[x][y] = average
    return new_cells

def blur_cells(cells):
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            cells[x][y] = cells[x][y] * DECAY_FACTOR

def draw_cells():
    for cell_x in range(CELLS_X):
        for cell_y in range(CELLS_Y):
            cell_color = (
                retreating_pheromone[cell_x][cell_y] * 255, 
                0,
                foraging_pheromone[cell_x][cell_y] * 255
            )
            if food[cell_x][cell_y]:
                cell_color = (200, 200, 10)
            if is_in_nest(cell_x, cell_y):
                cell_color = (20, 180, 20)

            pygame.draw.rect(
                screen, 
                cell_color, 
                pygame.Rect(
                    cell_x * PIXELS_PER_CELL, 
                    cell_y * PIXELS_PER_CELL, 
                    PIXELS_PER_CELL, 
                    PIXELS_PER_CELL
                )
            )

def draw_ants():
    for ant in ants:
        color = (200, 200, 10)
        if ant.foraging:
            color = (250, 220, 220)
        pygame.draw.rect(
                screen, 
                color, 
                pygame.Rect(
                    ant.x * PIXELS_PER_CELL, 
                    ant.y * PIXELS_PER_CELL, 
                    PIXELS_PER_CELL, 
                    PIXELS_PER_CELL
                )
            )

default_values()
generate_ants()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    blur_cells(foraging_pheromone)
    blur_cells(retreating_pheromone)
    update_ants()

    draw_cells()
    draw_ants()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()