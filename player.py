from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

    shot_cooldown = 0
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #draw player to screen
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self,dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        vector = pygame.Vector2(0,1)
        vector = vector.rotate(self.rotation)
        vector *= PLAYER_SHOOT_SPEED
        new_shot.velocity = vector
        


    def update(self, dt):
        #movement controls for player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown > 0:
                return
            else: 
                self.shoot()
                self.shot_cooldown = PLAYER_SHOT_COOLDOWN
        self.shot_cooldown -= dt


        