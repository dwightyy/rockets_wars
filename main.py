import math
import random
import sys
import pygame
from pygame.locals import *
from modules.config import *
from modules.ship import Ship
from modules.EnemyShip import EnemyShip
import random

# initialise display
pygame.init()


FONT = pygame.font.SysFont('Comic Sans MS', 30)
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Enemies Atacks the moon - seasson 1")


# define lifebar
life = 100
damage = 100

# create background and main character images
bg = pygame.image.load("assets/imgs/winter.jpg").convert()
bg_rect = bg.get_rect()

# main loop


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_ships = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)

x = 0

def spawn_enemy_ships(enemy_ships):
    for i in range(3):
        random_y, random_x = random.randint(50, 680), random.randint(1000, 1150)
        enemy_ships.add(EnemyShip(random_x, random_y))
    return enemy_ships

enemy_ships = spawn_enemy_ships(enemy_ships)

all_sprites.add(enemy_ships)
start_ticks=pygame.time.get_ticks()


while True:
    CLOCK.tick(FPS)
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    game_time = 
    game_fase = FONT.render("Fase 1", False, (BLACK))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                all_sprites = ship.shoot(all_sprites, bullets)
                print(all_sprites, bullets)

        #teste
        elif CLOCK.tick(FPS)
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        game_fase = FONT.render('Fase 1', False, (BLACK) event in pyga)
    

    DS.fill(BLACK)


    rel_x = x % bg.get_rect().width
    DS.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))
    x -= 1


    k = pygame.key.get_pressed()
 

    all_sprites.update()
 

    hits_enemy_ship = pygame.sprite.groupcollide(enemy_ships, bullets, True, True)
        

    #pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    #pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))

   # Draw / render

    DS.blit(game_time, (10, 0))
    DS.blit(game_fase, (10, 40))
    all_sprites.draw(DS)
    # *after* drawing everything, flip the display
    pygame.display.flip()
