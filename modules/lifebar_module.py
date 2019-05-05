import math, random, sys
import pygame
from pygame.locals import *


green = (0, 255, 0)
red  = (255, 0 ,0)


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# define display surface            
W, H = 640, 360



### define lifebar
# positive life
life = 100
#negative life
damage = 0

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500


# main loop
while True:
    events()
            
    k = pygame.key.get_pressed()
	
    if k[K_RIGHT]:
        if life >= 0 and damage <= 100:
            life -= 1
    elif k[K_LEFT]:
        if life <= 100 and damage >= 0:
            life += 1

    
    
    pygame.draw.rect(DS, red, pygame.Rect(20, 20, 100, 30))
    pygame.draw.rect(DS, green, pygame.Rect(20, 20, life, 30))
    
    
    

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill((255,255,255))
