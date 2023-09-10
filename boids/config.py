WIDTH = 700 # Screen size
HEIGHT = 700

NUMBER_OF_BOIDS = 100 # Number of boids (m ore boids results in quadratically poorer performance :) )

MAX_SPEED = 2 # The maximum speed of boids
MAX_FORCE = 0.01 # The maximum magnitude of force applied to boids each step

DESIRED_SEPARATION = 25 # Boids will try to steer away from eachother if they are within this distance
MAX_COHESION_VISION = 50 # Boids will try to steer towards eachother if they are within this distance
MAX_ALIGNMENT_VISION = 50 # Boids will try to steer such that they align with eachother if they are within this distance
TOWARDS_MOUSE_VISION = 150 # Boids will try to steer towards the mouse if they are within this distance of it

# Arbitrary weights for each steering force
SEPARATION_WEIGHT = 10
ALIGNMENT_WEIGHT = 0.5
COHESION_WEIGHT = 0.5
TOWARDS_MOUSE_WEIGHT = 20