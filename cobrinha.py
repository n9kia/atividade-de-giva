import pygame 
import random
from pygame.locals import *

def grid_random():
   x = random.randint(0,590)
   y = random.randint(0,590)
   return (x//10 * 10, y//10*10)

def colisao(c1,c2):
   return (c1[0]== c2[0]) and (c1[1]==c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("cobra")

cobra=[(200,200),(210,200),(220,200)]
cobra_skin = (pygame.Surface((10,10)))
cobra_skin.fill((255,255,255))

apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direct = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for event in pygame.event.get():
       if event.type == quit:
        pygame.quit()

       if colisao(cobra[0], apple_pos):
         apple_pos = grid_random()
         cobra.append((0,0))



       if event.type == KEYDOWN:
         if event.key == K_UP:
          my_direct = UP
         if event.key == K_DOWN:
          my_direct = DOWN
         if event.key == K_LEFT:
          my_direct = LEFT
         if event.key == K_RIGHT:
          my_direct = RIGHT

       if my_direct ==UP: 
        cobra[0]= (cobra[0][0], cobra[0][1]-10)
       if my_direct ==DOWN: 
        cobra[0]= (cobra[0][0], cobra[0][1]+10)
       if my_direct ==RIGHT: 
        cobra[0]= (cobra[0][0] +10, cobra[0][1])
       if my_direct ==LEFT: 
        cobra[0]= (cobra[0][0]-10, cobra[0][1])
 
  
    for i in range(len(cobra) - 1, 0, -1):
       cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    screen.fill((0,0,0))
    screen.blit(apple,apple_pos)
    for pos in cobra:
     screen.blit(cobra_skin,pos)
    
    pygame.display.update()
