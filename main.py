# this allows us to use code from the Open Source pygame library
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import * 
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

#Object Groups

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)

pc = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
af = AsteroidField()

def main():
    pygame.init()
    
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
  

    #Game loop
    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
          screen.fill((0,0,0), rect=None, special_flags=0)
          
          for asteroid in asteroids:
               if asteroid.collision_check(pc) ==True:
                    print("Game over!")
                    sys.exit()

          for asteroid in asteroids:
                for bullet in shots:
                    if bullet.collision_check(asteroid) == True:
                         asteroid.split()

          
          updatable.update(dt)
          for object in drawable:
               object.draw(screen)
          
          
          
          
          pygame.display.flip()
          dt = clock.tick(60)/1000

















if __name__ == "__main__":
        main()