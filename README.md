# Emergent Behaviour
A collection of graphics simulations that showcase how simple rules can be used to form complex emergent behaviours.

Each example can be run using the `main.py` file in its corresponding folder.
[Pygame](https://github.com/pygame/pygame) must be installed (`pip install pygame`)

## Life
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a cellular automaton consisting of a grid of cells that evolve over discrete time steps based on simple rules, leading to cool patterns. The standard rules are as follows:
- A dead cell with 3 alive neighbors is reborn
- An alive cell with 2 or 3 alive neighbors survives
- All other cells die
These rules are applied across all cells simultaneously each iteration of the simulation.

## Boids
[Boids](https://en.wikipedia.org/wiki/Boids) (bird-oids) is a simulation that models the flocking behavior of birds by applying three basic rules: 
- Separation (avoiding collisions)
- Alignment (matching the direction of nearby boids)
- Cohesion (moving toward the average position of nearby boids)
This results in realistic group formations of animal motion.

## Ant Colony Simulation