import pygame
import random
from config import *
from boid import Boid

running = True
boids = []

for i in range(NUMBER_OF_BOIDS):
    boids.append(Boid(pygame.Vector2(random.randint(1, WIDTH), random.randint(1, HEIGHT))))

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boids')

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    mouse_down = pygame.mouse.get_pressed()[0]
    mouse_position = pygame.mouse.get_pos()
    
    for boid in boids:
        if mouse_down:
            boid.update(boids, True, mouse_position)
        else:
            boid.update(boids, False, None)
        boid.render(screen)

    if mouse_down:
        pygame.draw.circle(screen, (255, 255, 255, 150), mouse_position, TOWARDS_MOUSE_VISION, 1)
        
    pygame.display.flip()

    clock.tick(60)

pygame.quit()