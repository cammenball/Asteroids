import pygame
from  constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        DISPLAY.fill(0)
        pygame.display.flip()

if __name__ == "__main__":
    main()