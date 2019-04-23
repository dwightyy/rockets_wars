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
bg_rect = bg.get_rect()

# main loop


all_sprites = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)

while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    k = pygame.key.get_pressed()

    if k[K_RIGHT]:
        pass

    elif k[K_LEFT]:
        pass

    elif k[K_UP]:
        pass

    elif k[K_DOWN]:
        pass

    all_sprites.update()

    #pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    #pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))

    ship.fire(DS, bullets)

   # Draw / render
    DS.fill(BLACK)
    DS.blit(bg, bg_rect)
    all_sprites.draw(DS)
    # *after* drawing everything, flip the display
    pygame.display.flip()
