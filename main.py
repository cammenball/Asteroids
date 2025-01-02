import pygame
from  constants import *

#create clock object to set framerate in main loop
fps = pygame.time.Clock()
dt = 0

def main():
    #initialize pygame and create screen
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #infinite loop to continue game. first 2 lines paint the screen every loop
    while True:
        DISPLAY.fill(0)
        pygame.display.flip()
        #checks if close button has been clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #sets delta time to have 60fps
        dt = (fps.tick(60))/1000

if __name__ == "__main__":
    main()