import math
import random
import sys
import pygame
from pygame.locals import *
from config import *

# exit the program
def events():
    for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Enemies Atacks the moon - seasson 1")

# define player score system
score = 0

# define lifebar
life = 100
damage = 100

# create background and main character images
bg = pygame.image.load("mountains.png").convert()
spaceship = pygame.transform.scale(pygame.image.load("spaceship.png").convert(), (50, 50))
bgWidth, bgHeight = bg.get_rect().size


# define level size. For increase level difficult, change the factor after bgWidth
stageWidth = bgWidth * 2
stagePosX = 0

# define inicial scroll status
startScrollingPosX = HW


circleRadius = 25
spaceShipPosX = circleRadius

playerPosX = circleRadius
playerPosY = H / 2
playerVelocityX = 0
playerVelocityY = 0

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
    elif k[K_UP]:
        playerPosY -= 1

    elif k[K_DOWN]:
        playerPosY += 1
    
    else:
        playerVelocityX = 0
        
    playerPosX += playerVelocityX
    if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius: playerPosX = circleRadius
    if playerPosX < startScrollingPosX: spaceShipPosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX: spaceShipPosX = playerPosX - stageWidth + W
    else:
        spaceShipPosX = startScrollingPosX
        stagePosX += -playerVelocityX
    
    rel_x = stagePosX % bgWidth
    DS.blit(bg, (rel_x - bgWidth, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))

    pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))
    DS.blit(spaceship, (int(spaceShipPosX), int(playerPosY)))


    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
