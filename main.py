import math
import random
import sys
import pygame
from pygame.locals import *
from modules.config import *
from modules.ship import Ship


def desenharTiro(tiros):
    for t in range(len(tiros)):
        if(tiros[t]['status'] == 1):
            pygame.draw.rect(DS, RED, pygame.Rect(
                tiros[t]['x'], tiros[t]['y'], 10, 5))

            tiros[t]['x'] += 10


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


# define lifebar
life = 100
damage = 100

# create background and main character images
bg = pygame.image.load("assets/imgs/mountains.png").convert()

tiros = []
# main loop
ship = Ship(30, H/2, MAIN_SHIP_SPRITE)

while True:
    events()

    k = pygame.key.get_pressed()

    if k[K_RIGHT]:
        ship.move_right()

    elif k[K_LEFT]:
        ship.move_left()

    elif k[K_UP]:
        ship.move_up()

    elif k[K_DOWN]:
        ship.move_down()

    elif k[K_SPACE]:
        tiros.append({'x': playerPosX+50, 'y': playerPosY+23, 'status': 1})

    pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))
    DS.fill([255, 255, 255])
    DS.blit(bg, (0, 0))
    DS.blit(ship.sprite, (ship.pos_x, ship.pos_y))

    desenharTiro(tiros)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
