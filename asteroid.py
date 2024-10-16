import pygame
from circleshape import CircleShape
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt
   
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_1_vector = pygame.math.Vector2.rotate(self.velocity, random_angle)
        asteroid_2_vector = pygame.math.Vector2.rotate(self.velocity, random_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_1.velocity = asteroid_1_vector * 1.2
        asteroid_2.velocity = asteroid_2_vector * 1.2