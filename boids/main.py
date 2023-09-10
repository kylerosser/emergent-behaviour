import pygame
import config
from boid import Boid

running = True
boids = []

boids.append(Boid(pygame.Vector2(500, 200)))

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
        boid.update()
        boid.render(screen)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()