import pygame
import config
import random
from pygame import gfxdraw

class Boid():
    def __init__(self, position):
        self.position = position
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * config.MAX_SPEED
        self.acceleration = pygame.Vector2(0, 0)

    def separation(self, boids):
        steer_vector = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance > 0 and distance < config.DESIRED_SEPARATION:
                steer_vector += (self.position - other_boid.position).normalize() / distance
                n += 1
        
        if n > 0:
            steer_vector /= n

        if steer_vector.magnitude() > 0:
            steer_vector = steer_vector.normalize()
            steer_vector *= config.MAX_SPEED
            # Reynold's steering behaviour
            steer_vector -= self.velocity
            if steer_vector.magnitude() > 0.000001:
                steer_vector = steer_vector.clamp_magnitude(config.MAX_FORCE)
        
        return steer_vector

    def alignment(self, boids):
        velocity_sum = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance < config.MAX_ALIGNMENT_VISION:
                velocity_sum += other_boid.velocity
                n += 1
        
        if n > 0:
            average_velocity = velocity_sum / n
            steer_vector = average_velocity.normalize()
            steer_vector *= config.MAX_SPEED
            steer_vector -= self.velocity
            if steer_vector.magnitude() > 0.00001:
                steer_vector.clamp_magnitude(config.MAX_FORCE)
            return steer_vector
        else:
            return pygame.Vector2(0, 0)


    def cohesion(self, boids):
        position_sum = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance < config.MAX_COHESION_VISION:
                position_sum += other_boid.position
                n += 1

        if n > 0:
            average_position = position_sum / n
            if abs((average_position - self.position).magnitude()) <= 0.00001:
                
                return pygame.Vector2(0, 0)
            
            steer_vector = (average_position - self.position).normalize() * config.MAX_SPEED
            steer_vector -= self.velocity
            steer_vector = steer_vector.clamp_magnitude(config.MAX_FORCE)
            return steer_vector
        else:
            return pygame.Vector2(0, 0)

                    
    
    def update(self, boids):
        seperation_velocity = self.separation(boids)
        alignment_velocity = self.alignment(boids)
        cohesion_velocity = self.cohesion(boids)

        self.acceleration += seperation_velocity * 2
        self.acceleration += alignment_velocity * 0.5
        self.acceleration += cohesion_velocity

        self.velocity += self.acceleration
        if not self.velocity.magnitude() == 0:
            self.velocity = self.velocity.clamp_magnitude(config.MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0
        
        # Wrap-around borders of screen
        border_tolerance = 10
        if self.position.x < -border_tolerance: self.position.x = config.WIDTH + border_tolerance
        if self.position.x > config.WIDTH + border_tolerance: self.position.x = -border_tolerance
        if self.position.y < -border_tolerance: self.position.y = config.HEIGHT + border_tolerance
        if self.position.y > config.HEIGHT + border_tolerance: self.position.y = -border_tolerance
        

    def render(self, screen):
        if not self.velocity.magnitude() == 0:
            direction_vector = self.velocity.normalize()
        else:
            direction_vector = pygame.Vector2(0, 1)
        tip_point = self.position + direction_vector * 5
        left_point = self.position - direction_vector.rotate(-30) * 7
        right_point = self.position - direction_vector.rotate(30) * 7
        pygame.draw.polygon(
            screen, 
            "white", 
            [tip_point, left_point, right_point]
        )