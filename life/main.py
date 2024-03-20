import pygame
from config import *

cells = [ [ False for y in range(CELLS_Y) ] for x in range(CELLS_X) ]
running = True
paused = True
age = 0

pygame.init() 

screen = pygame.display.set_mode((CELLS_X * PIXELS_PER_CELL, CELLS_Y * PIXELS_PER_CELL))
pygame.display.set_caption('Game of Life')

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

def update_cells():
    global cells
    global age

    new_cells = [ [False for y in range(CELLS_Y)] for x in range(CELLS_X)]

    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            alive = cells[x][y]
            alive_neighbors = 0

            for neighbor_x in range(x - 1, x + 2, 1):
                for neighbor_y in range(y - 1, y + 2, 1):
                    # Reject neighbors out of bounds
                    if neighbor_x >= CELLS_X or neighbor_x < 0:
                        continue
                    if neighbor_y >= CELLS_Y or neighbor_y < 0:
                        continue
                    if neighbor_y == y and neighbor_x == x:
                        continue

                    if cells[neighbor_x][neighbor_y]:
                        alive_neighbors += 1
            
            if alive:
                should_live = False
                for n in SURVIVE_NEIGHBORS:
                    if alive_neighbors == n:
                        should_live = True
                new_cells[x][y] = should_live
            else:
                should_live = False
                for n in BORN_NEIGHBORS:
                    if alive_neighbors == n:
                        should_live = True
                new_cells[x][y] = should_live

    cells = new_cells
    age += 1

def draw_cells():
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            alive = cells[x][y]
            if alive:
                pygame.draw.rect(screen, "white", pygame.Rect(x * PIXELS_PER_CELL, y * PIXELS_PER_CELL, PIXELS_PER_CELL, PIXELS_PER_CELL))

def draw_ui():
    stats_string = f"RULE: B{''.join(map(str, BORN_NEIGHBORS))}/S{''.join(map(str, SURVIVE_NEIGHBORS))}  FPS: {FPS}  AGE: {age}"
    stats_image = font.render(stats_string, True, 'white')
    controls_string = "SPACE to pause/play the simulation; MOUSE1 to toggle cell"
    controls_image = font.render(controls_string, True, 'white')
    screen.blit(stats_image, (10, 10))
    screen.blit(controls_image, (10, 30))

def handle_events():
    global running
    global paused

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            cell_x = mouse_position[0] // PIXELS_PER_CELL
            cell_y = mouse_position[1] // PIXELS_PER_CELL
            cells[cell_x][cell_y] = not cells[cell_x][cell_y]

while running:
    screen.fill("black")

    handle_events()

    if not paused:
        update_cells()

    draw_cells()
    draw_ui()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
