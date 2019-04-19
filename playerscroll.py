import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
    for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

# define display surface            
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# define player score system
score = 0


# define lifebar
life = 100
damage = 100


bg = pygame.image.load("mountains.png").convert()
#bg = pygame.image.load("level_2.jpg").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX = 0

# main loop
while True:
    events()

    k = pygame.key.get_pressed()
    
    if k[K_RIGHT]:
        playerVelocityX = 1
        if life >= 0 and damage <= 100:
                life -= 1       
    elif k[K_LEFT]:
        playerVelocityX = -1
        if life <= 100 and damage >= 0:
                life += 1
    else:
        playerVelocityX = 0
        
    playerPosX += playerVelocityX
    if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius: playerPosX = circleRadius
    if playerPosX < startScrollingPosX: circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX: circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX
    
    rel_x = stagePosX % bgWidth
    DS.blit(bg, (rel_x - bgWidth, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))

    pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))
    pygame.draw.circle(DS, (255,0,0), (int(circlePosX), int(50)), int(50), 0)
    
    

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
