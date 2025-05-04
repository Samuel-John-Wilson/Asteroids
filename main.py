# this allows us to use code from the Open Source pygame library
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_KINDS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Game loop
    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
          screen.fill(000, rect=None, special_flags=0)
          pygame.display.flip()

















if __name__ == "__main__":
        main()