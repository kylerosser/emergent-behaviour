import random
from config import *

def is_in_nest(x, y):
    if x > CELLS_X - CELLS_X //5 and x < CELLS_X - CELLS_X //10:
        if y > CELLS_Y // 3 and y < CELLS_Y - (CELLS_Y // 3):
            return True
    return False

class Ant():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.foraging = True

    def update(self, foraging_pheromone, retreating_pheromone, food):
        if food[self.x][self.y]:
            self.foraging = False
            food[self.x][self.y] = False
        
        if is_in_nest(self.x, self.y):
            self.foraging = True

        if self.foraging:
            foraging_pheromone[self.x][self.y] = min(1, foraging_pheromone[self.x][self.y] + PHEROMONE_AMOUNT)
        else:
            retreating_pheromone[self.x][self.y] = min(1, retreating_pheromone[self.x][self.y] + PHEROMONE_AMOUNT)

        pheromone = retreating_pheromone
        if not self.foraging:
            pheromone = foraging_pheromone

        highest_pheromone = 0
        highest_position = []

        for neighbor_x in range(self.x - 1, self.x + 2, 1):
                for neighbor_y in range(self.y - 1, self.y + 2, 1):
                    if neighbor_x >= CELLS_X or neighbor_x < 0:
                        continue
                    if neighbor_y >= CELLS_Y or neighbor_y < 0:
                        continue
                    if neighbor_y == self.y and neighbor_x == self.x:
                        continue
                    
                    value = pheromone[neighbor_x][neighbor_y]
                    if value == highest_pheromone:
                        highest_position.append([neighbor_x, neighbor_y])
                    elif value > highest_pheromone:
                        highest_pheromone = value
                        highest_position = []
                        highest_position.append([neighbor_x, neighbor_y])

        chosen_position = highest_position[random.randint(0, len(highest_position) - 1)]
        self.x = chosen_position[0]
        self.y = chosen_position[1]
        
        


