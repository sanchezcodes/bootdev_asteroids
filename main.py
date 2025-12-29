from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updatable)

    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill((0,0,0))

        updatable.update(dt)
        
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
