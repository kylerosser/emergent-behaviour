import pygame
import config

class Boid():
    def __init__(self, position):
        self.__position = position
        self.__velocity = pygame.Vector2(0, 1)
        self.__acceleration = pygame.Vector2(-0.1,0.1)
    
    def update(self):
        print(self.__position)

        self.__velocity += self.__acceleration
        self.__position += self.__velocity
        self.__velocity = self.__velocity.clamp_magnitude(config.MAX_VELOCITY)
        
        # Wrap-around borders of screen
        border_tolerance = 10 # tolerance
        if self.__position.x < -border_tolerance: self.__position.x = config.WIDTH + border_tolerance
        if self.__position.x > config.WIDTH + border_tolerance: self.__position.x = -border_tolerance
        if self.__position.y < -border_tolerance: self.__position.y = config.HEIGHT + border_tolerance
        if self.__position.y > config.HEIGHT + border_tolerance: self.__position.y = -border_tolerance
        

    def render(self, screen):
        tip_point = self.__position + self.__velocity.normalize() * 10
        left_point = self.__position - self.__velocity.normalize().rotate(-30) * 15
        right_point = self.__position - self.__velocity.normalize().rotate(30) * 15
        pygame.draw.polygon(
            screen, 
            "white", 
            [tip_point, left_point, right_point],
            2
        )