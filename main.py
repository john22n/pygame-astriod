import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for entity in asteroids:
            if entity.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(entity):
                    shot.kill()
                    entity.split()

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        time_passed = clock_obj.tick(60)
        dt = time_passed / 1000



if __name__ == "__main__":
    main()

