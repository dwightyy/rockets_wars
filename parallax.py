import pygame
from pygame.locals  import *
import  sys
import os

def events():
    for event  in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()

def parallax():
    #define display surface 
    W,  H = 576, 1024
    HR,  RH = W / 2, H / 2 
    AREA = W* H

    os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"


    pygame.init()
    CLOCK = pygame.time.Clock() 
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("teste")
    FPS = 60

    bkgd = pygame.image.load("mountains.png").convert()
    x = 0

    while True:
        events()
        rel_x = x % bkgd.get_rect().width
        DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
        if rel_x < W:
            DS.blit(bkgd, (rel_x, 0))
        x -= 1
        pygame.display.update()
        CLOCK.tick(FPS)
