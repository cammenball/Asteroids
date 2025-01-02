from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY,(255,255,255),(self.position.x,self.position.y),self.radius,20)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()