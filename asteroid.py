from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY,(255,255,255),(self.position.x,self.position.y),self.radius,20)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        asteroid_1 = self.velocity.rotate(random_angle)
        asteroid_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        create_1 = Asteroid(self.position.x, self.position.y, new_radius)
        create_2 = Asteroid(self.position.x, self.position.y, new_radius)
        create_1.velocity = asteroid_1
        create_2.velocity = asteroid_2
