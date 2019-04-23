import math
import random
import sys
import pygame
from pygame.locals import *
from modules.config import *
from modules.ship import Ship

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

bullets = []
# main loop
ship = Ship(30, H/2, MAIN_SHIP_SPRITE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    {'x': ship.pos_x+50, 'y': ship.pos_y+23, 'status': 1})

    k = pygame.key.get_pressed()

    if k[K_RIGHT]:
        ship.move_right()

    elif k[K_LEFT]:
        ship.move_left()

    elif k[K_UP]:
        ship.move_up()

    elif k[K_DOWN]:
        ship.move_down()

    pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))
    DS.fill([255, 255, 255])
    DS.blit(bg, (0, 0))

    ship.fire(DS, bullets)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
