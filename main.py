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

#score
score = 0

#defining time
minutes = 0
seconds = 0
milliseconds = 0

# define lifebar
life = 100
damage = 100

#reference to fase
fase = 1

# create background and main character images
bg = pygame.image.load("assets/imgs/forest.jpg").convert()
bg_rect = bg.get_rect()

# main loop

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_ships = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)

x = 0

def spawn_enemy_ships(enemy_ships):
    for i in range(5):
        random_y, random_x = random.randint(50, 680), random.randint(1000, 1150)
        enemy_ships.add(EnemyShip(random_x, random_y))
    return enemy_ships

enemy_ships = spawn_enemy_ships(enemy_ships)

all_sprites.add(enemy_ships)
start_ticks=pygame.time.get_ticks()

while True:
    CLOCK.tick(FPS)    
    game_fase = FONT.render("Fase " + str(fase), False, (WHITE))
    
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                all_sprites = ship.shoot(all_sprites, bullets)
                print(all_sprites, bullets)

    seconds = int((pygame.time.get_ticks()-start_ticks)/1000)
    if seconds > 60:
        minutes += 1
        seconds = 0
    timelabel = FONT.render("{}:{}".format(minutes, int(seconds)), False, (WHITE))    
    

    DS.fill(BLACK)


    rel_x = x % bg.get_rect().width
    DS.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))
    x -= 1


    k = pygame.key.get_pressed()
 

    all_sprites.update()
 

    hits_enemy_ship = pygame.sprite.groupcollide(enemy_ships, bullets, True, True)    

    if hits_enemy_ship != {} and fase == 1:
        score += 10
    if hits_enemy_ship != {} and fase == 2:
        score += 20
    if hits_enemy_ship != {} and fase == 3:
        score += 30
        
    game_score = FONT.render("Score: " + str(score), False, (WHITE))

    if minutes == 1 and seconds == 30 and fase == 1:
        bg = pygame.image.load("assets/imgs/mountains.png").convert()
        bg_rect = bg.get_rect()
        start_ticks=pygame.time.get_ticks()
        seconds = 0
        minutes = 0
        fase = 2

    if minutes == 2 and seconds == 30 and fase == 2:
        bg = pygame.image.load("assets/imgs/space.jpg").convert()
        bg_rect = bg.get_rect()
        start_ticks=pygame.time.get_ticks()
        seconds = 0
        minutes = 0
        fase = 3    
        

    #pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
    #pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))

   # Draw / render

    DS.blit(game_fase, (10, 20))
    DS.blit(timelabel,(1180, 20))
    DS.blit(game_score, (10, 60))
    
    all_sprites.draw(DS)
    # *after* drawing everything, flip the display
    pygame.display.flip()
