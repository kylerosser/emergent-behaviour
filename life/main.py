import pygame

CELLS_X = 70
CELLS_Y = 70
FPS = 10

cells = [ [ False for x in range(100) ] for y in range(100) ]

cells[10][10] = True
cells[11][10] = True
cells[12][10] = True
cells[10][9] = True

cells[20][20] = True
cells[19][20] = True
cells[18][20] = True

cells[22][21] = True
cells[22][20] = True
cells[22][19] = True

cells[2][0] = True
cells[3][1] = True
cells[3][2] = True
cells[2][2] = True
cells[1][2] = True

def update_cells():
    global cells
    new_cells = [ [False for x in range(100)] for y in range(100)]

    for x in range(100):
        for y in range(100):
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
                new_cells[x][y] = (alive_neighbors == 2 or alive_neighbors == 3)
            else:
                new_cells[x][y] = (alive_neighbors == 3)

    cells = new_cells

pygame.init()
screen = pygame.display.set_mode((CELLS_X * 10, CELLS_Y * 10))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    update_cells()

    for x in range(100):
        for y in range(100):
            alive = cells[x][y]
            if alive:
                pygame.draw.rect(screen, "white", pygame.Rect(x * 10, y * 10, 10, 10))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()