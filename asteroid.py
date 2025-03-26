import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius,asteroid_group):
        super().__init__(x,y,radius)
        self.asteroid_group = asteroid_group
    
    def draw(self, screen):
        pygame.draw.circle(screen,ASTEROID_COLOR,self.position,self.radius,2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)

    def split(self):
        self.kill()
        #print(f"1Splitting asteroid at ({self.position.x}, {self.position.y}) into two smaller ones!")
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x,self.position.y,new_radius,self.asteroid_group)
        asteroid_one.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_two = Asteroid(self.position.x,self.position.y,new_radius,self.asteroid_group)
        asteroid_two.velocity = self.velocity.rotate(-random_angle) * 1.2
        self.asteroid_group.add(asteroid_one)
        self.asteroid_group.add(asteroid_two)
        #print(f"2Splitting asteroid at ({self.position.x}, {self.position.y}) into two smaller ones!")