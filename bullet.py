import pygame
from circleshape import CircleShape
from constants import *

class Bullet (CircleShape):
    def __init__(self, x, y, radius,player_rotation):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 1).rotate(player_rotation) * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen,BASIC_WEAPON_COLOR,self.position,self.radius,2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)
    