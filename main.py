# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from bullet import Bullet

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    updatable_sprite_group = pygame.sprite.Group()
    drawable_sprite_group = pygame.sprite.Group()
    asteroid_sprite_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    Player.containers = (updatable_sprite_group, drawable_sprite_group)
    Asteroid.containers = (asteroid_sprite_group, updatable_sprite_group, drawable_sprite_group)
    AsteroidField.containers =(updatable_sprite_group)
    Bullet.containers = (bullets_group, updatable_sprite_group, drawable_sprite_group)

    player1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,bullets_group)
    asteroid_field = AsteroidField() 

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable_sprite_group.update(delta_time)

        for asteroid in asteroid_sprite_group:
            if asteroid.collision(player1):
                print("Game over!")
                return

        screen.fill("black")

        for sprite in drawable_sprite_group:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        delta_time = clock.tick(60)/1000


if __name__ == "__main__":
    main()