# this allows us to use code from the Open Source pygame library
import pygame

from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

def main():
    pygame.init()
    
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pc = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Game loop
    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
          screen.fill(000, rect=None, special_flags=0)
          
          
          pc.update(dt)
          pc.draw(screen)
          
          
          
          
          pygame.display.flip()
          dt = clock.tick(60)/1000

















if __name__ == "__main__":
        main()