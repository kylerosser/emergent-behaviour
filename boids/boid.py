import pygame
import random
from config import *

class Boid():
    def __init__(self, position):
        self.position = position
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * MAX_SPEED
        self.acceleration = pygame.Vector2(0, 0)

    def steer_towards_point(self, point):
        steer_vector = (point - self.position).normalize() * MAX_SPEED
        steer_vector -= self.velocity
        if steer_vector.magnitude() > 0.000001:
            steer_vector = steer_vector.clamp_magnitude(MAX_FORCE)
        return steer_vector

    def separation(self, boids):
        # Returns a steer vector towards the point with least amount of neighbouring boids
        steer_vector = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance > 0 and distance < DESIRED_SEPARATION:
                steer_vector += (self.position - other_boid.position).normalize() / distance
                n += 1
        
        if n > 0:
            steer_vector /= n

        if steer_vector.magnitude() > 0:
            steer_vector = steer_vector.normalize()
            steer_vector *= MAX_SPEED
            steer_vector -= self.velocity
            if steer_vector.magnitude() > 0.000001:
                steer_vector = steer_vector.clamp_magnitude(MAX_FORCE)
        
        return steer_vector

    def alignment(self, boids):
        # Returns a steer vector towards average velocity of neighbouring boids
        velocity_sum = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance < MAX_ALIGNMENT_VISION:
                velocity_sum += other_boid.velocity
                n += 1
        
        if n > 0:
            average_velocity = velocity_sum / n
            steer_vector = average_velocity.normalize()
            steer_vector *= MAX_SPEED
            steer_vector -= self.velocity
            if steer_vector.magnitude() > 0.00001:
                steer_vector.clamp_magnitude(MAX_FORCE)
            return steer_vector
        else:
            return pygame.Vector2(0, 0)


    def cohesion(self, boids):
        # Returns a steer vector towards average position of neighbouring boids
        position_sum = pygame.Vector2(0, 0)
        n = 0
        for other_boid in boids:
            distance = (other_boid.position - self.position).magnitude()
            if distance < MAX_COHESION_VISION:
                position_sum += other_boid.position
                n += 1

        if n > 0:
            average_position = position_sum / n
            if abs((average_position - self.position).magnitude()) <= 0.00001:
                
                return pygame.Vector2(0, 0)
            
            steer_vector = self.steer_towards_point(average_position)
            return steer_vector
        else:
            return pygame.Vector2(0, 0)

    
    def update(self, boids, move_towards_mouse, mouse_position):
        # Calculate steering velocities for each rule
        seperation_velocity = self.separation(boids)
        alignment_velocity = self.alignment(boids)
        cohesion_velocity = self.cohesion(boids)
        towards_mouse_velocity = pygame.Vector2(0, 0)
        
        # If mouse button is down, apply the mouse attraction rule
        if move_towards_mouse:
            distance = (mouse_position - self.position).magnitude()
            if distance < TOWARDS_MOUSE_VISION:
                towards_mouse_velocity = self.steer_towards_point(mouse_position)
        
        # Weight each velocity to taste, and add to acceleration
        self.acceleration += seperation_velocity * SEPARATION_WEIGHT
        self.acceleration += alignment_velocity * ALIGNMENT_WEIGHT
        self.acceleration += cohesion_velocity * COHESION_WEIGHT
        self.acceleration += towards_mouse_velocity * TOWARDS_MOUSE_WEIGHT

        # Step velocity/position values
        self.velocity += self.acceleration
        if not self.velocity.magnitude() == 0:
            self.velocity = self.velocity.clamp_magnitude(MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0
        
        # Wrap-around borders of screen
        border_tolerance = 10
        if self.position.x < -border_tolerance: self.position.x = WIDTH + border_tolerance
        if self.position.x > WIDTH + border_tolerance: self.position.x = -border_tolerance
        if self.position.y < -border_tolerance: self.position.y = HEIGHT + border_tolerance
        if self.position.y > HEIGHT + border_tolerance: self.position.y = -border_tolerance
        

    def render(self, screen):
        # Render the boid on the pygame screen
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