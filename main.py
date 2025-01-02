import pygame
from  constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

#create clock object to set framerate in main loop
fps = pygame.time.Clock()
dt = 0

#create groups for the game objects
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updateable, drawable)
asteroid_group = pygame.sprite.Group()
Asteroid.containers = (asteroid_group, updateable, drawable)
AsteroidField.containers = (updateable)
shots = pygame.sprite.Group()
Shot.containers = (shots, updateable, drawable)

def main():
    #initialize pygame and create screen
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    user = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()

    #infinite loop to continue game. first 2 lines paint the screen every loop
    while True:
        DISPLAY.fill((0,0,0))
        for each in drawable:
            each.draw(DISPLAY)
        pygame.display.flip()
        #checks if close button has been clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #sets delta time to have 60fps
        dt = (fps.tick(60))/1000
        for each in updateable:
            each.update(dt)
        for each in asteroid_group:
            x = CircleShape.collision(user, each)
            if x == False:
                print("Game over!")
                return False
        for each_x in asteroid_group:
            for each_y in shots:
                x = CircleShape.collision(each_x, each_y)
                if x == False:
                    each_x.split()
                    each_y.kill()



if __name__ == "__main__":
    main()