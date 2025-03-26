import pygame
from circleshape import CircleShape
from constants import *
from bullet import Bullet

class Player (CircleShape):
    def __init__(self,x,y,bullet_group):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.bullet_group = bullet_group
        self.basic_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,PLAYER_COLOR,self.triangle(),2)

    def rotate(self,delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.basic_timer -= delta_time

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE] and not self.basic_timer > 0:
            self.shoot()
            


    def move(self,delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        bullet = Bullet(self.position.x,self.position.y,SHOT_RADIUS,self.rotation)
        self.bullet_group.add(bullet)
        self.basic_timer = PLAYER_BASIC_COOLDOWN
        