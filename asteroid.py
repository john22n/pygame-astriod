import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        generated_random = random.uniform(20, 50)

        new_asteroid1 = self.velocity.rotate(generated_random)
        new_asteroid2 = self.velocity.rotate(-generated_random)

        new_radius = self.radius - ASTEROID_MIN_RADIUS 

#       pygame.draw.circle(screen, "white", self.position, new_radius, 2)
#       pygame.draw.circle(screen, "white", self.position, new_radius, 2)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_asteroid1 * 1.2
        asteroid2= Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_asteroid2 * 1.2


