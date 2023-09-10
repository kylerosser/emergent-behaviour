import pygame
import config
import random
from boid import Boid

running = True
boids = []

for i in range(config.NUMBER_OF_BOIDS):
    boids.append(Boid(pygame.Vector2(random.randint(1, config.WIDTH), random.randint(1, config.HEIGHT))))

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Boids')

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for boid in boids:
        boid.update(boids)
        boid.render(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()