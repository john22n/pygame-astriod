import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, circle_shape):
        distance_between_circles = pygame.math.Vector2.distance_to(circle_shape.position, self.position)
        distance_between_radius = self.radius + circle_shape.radius

        print(distance_between_circles, distance_between_radius) 

        if distance_between_circles < distance_between_radius:
            return True

        return False

