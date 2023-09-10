CELLS_X = 70 # Number of cells on the grid
CELLS_Y = 70

PIXELS_PER_CELL = 10 # Size of each cell in pixels

FPS = 10 # Maximum number of updates per second

BORN_NEIGHBORS = [3] # A dead cell will be reborn if it has this many neighbors
SURVIVE_NEIGHBORS = [2, 3] # A living cell will survive if it has this many neighbors
# ( All other living cells die )

# Common rulesets include: B3/S23 (Conway's Game Of Life) and B36/S23 (HighLife)