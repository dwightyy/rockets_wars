import math
import random
import sys
import pygame
from pygame.locals import *
from modules.config import *
from modules.ship import Ship
from modules.EnemyShip import EnemyShip
import random
import time

# initialise display
pygame.init()


FONT = pygame.font.SysFont('Comic Sans MS', 30)
FONT2 = pygame.font.SysFont('Comic Sans MS', 80)
FONT3 = pygame.font.SysFont('Comic Sans MS', 40)
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Enemies Atacks the moon - seasson 1")


spawn_ships_time = [2, 10, 15, 25, 45, 62, 70, 85, 100, 122, 140, 155]


def main():
    # score
    score = 0

    # defining time
    minutes = 0
    seconds = 0

    # define lifebar
    life = 100
    damage = 100

    # reference to fase
    fase = 1

    # create background and main character images
    bg = pygame.image.load("assets/imgs/forest.jpg").convert()
    bg_rect = bg.get_rect()

    # main loop

    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    ship = Ship()

    main_ship_sprite_group = pygame.sprite.Group()
    main_ship_sprite_group.add(ship)
    all_sprites.add(main_ship_sprite_group)

    x = 0

    def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN or event.type == KEYDOWN:
                    return

            DS.fill(WHITE)
            gameName = FONT2.render("ROCKETS WAR", False, (GREEN))
            startInstruction = FONT.render(
                "Press the mouse or any key to start the game", False, (BLACK))
            startInstruction2 = FONT.render(
                "Press esc or q anytime to quit the game", False, (BLACK))
            gameNameRect = gameName.get_rect()
            gameNameRect.center = (HW, (HH-150))
            DS.blit(gameName, gameNameRect)
            DS.blit(startInstruction, (330, HH))
            DS.blit(startInstruction2, (370, (HH+60)))
            pygame.display.update()
            # CLOCK.tick(15)

    def change_fase():

        newfase = True

        while newfase:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN or (event.type == KEYDOWN and event.key == K_c):
                    return

            DS.fill(WHITE)
            congratulations = FONT3.render("CONGRATULATIONS!", False, (GREEN))
            faseName = FONT3.render(
                "YOU FINISHED THE FASE " + str(fase), False, (GREEN))
            faseInstruction = FONT.render(
                "Press the mouse or c to start the new fase", False, (BLACK))
            faseInstruction2 = FONT.render(
                "Press esc or q anytime to quit the game", False, (BLACK))
            congratulationsRect = congratulations.get_rect()
            congratulationsRect.center = (HW, (HH-90))
            DS.blit(congratulations, congratulationsRect)
            DS.blit(faseName, (380, (HH-70)))
            DS.blit(faseInstruction, (350, HH))
            DS.blit(faseInstruction2, (370, (HH+60)))
            pygame.display.update()
            # CLOCK.tick(15)

    def end_game():

        endGame = True

        while endGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN or (event.type == KEYDOWN and event.key == K_c):
                    return

            DS.fill(WHITE)
            congratulations = FONT3.render("CONGRATULATIONS!", False, (GREEN))
            faseName = FONT3.render("YOU FINISHED THE GAME!", False, (GREEN))
            yourScore = FONT.render(
                "Final Score: " + str(score), False, (BLACK))
            faseInstruction = FONT.render(
                "Press the mouse or c to start a new game", False, (BLACK))
            faseInstruction2 = FONT.render(
                "Press esc or q anytime to quit the game", False, (BLACK))
            congratulationsRect = congratulations.get_rect()
            congratulationsRect.center = (HW, (HH-90))
            DS.blit(congratulations, congratulationsRect)
            DS.blit(faseName, (380, (HH-70)))
            DS.blit(yourScore, (550, HH))
            DS.blit(faseInstruction, (350, HH+60))
            DS.blit(faseInstruction2, (370, (HH+120)))
            pygame.display.update()
            # CLOCK.tick(15)

    def spawn_enemy_ships(enemy_ships, level):
        if level == 1:
            enemy_ship_life = 200
        elif level == 2:
            enemy_ship_life = 400
        elif level == 3:
            enemy_ship_life = 600

        for i in range(5):
            random_y, random_x = random.randint(
                50, 680), random.randint(1000, 1150)
            enemy_ships.add(EnemyShip(random_x, random_y, enemy_ship_life))
        return enemy_ships

    def check_enemy_ships_limit(enemy_ships):
        for en_ships in enemy_ships:
            if en_ships.rect.left <= -20:
                en_ships.kill()

    game_intro()

    start_ticks = pygame.time.get_ticks()
    enemy_ships = pygame.sprite.Group()

    enemy_ship_spawn_flag = 1
    curr_second = 0
    while True:

        CLOCK.tick(FPS)
        game_fase_font = FONT.render("Fase " + str(fase), False, (WHITE))

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
            start_ticks = pygame.time.get_ticks()
        timelabel = FONT.render("{}:{}".format(
            minutes, int(seconds)), False, (WHITE))

        DS.fill(BLACK)

        rel_x = x % bg.get_rect().width
        DS.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < W:
            DS.blit(bg, (rel_x, 0))
        x -= 1

        k = pygame.key.get_pressed()

        if seconds in spawn_ships_time and enemy_ship_spawn_flag == 1:
            curr_second = seconds
            enemy_ships = spawn_enemy_ships(enemy_ships, fase)
            all_sprites.add(enemy_ships)
            enemy_ship_spawn_flag = 0

        if seconds == curr_second + 1:
            enemy_ship_spawn_flag = 1

        all_sprites.update()

        hits_enemy_ship = pygame.sprite.groupcollide(
            enemy_ships, bullets, False, True)

        ship_hit_by_enemy = pygame.sprite.groupcollide(
            main_ship_sprite_group, enemy_ships, False, True)

        if hits_enemy_ship:
            for hit_ship in hits_enemy_ship:
                hit_ship.enemy_ship_life -= ship.damage
                if hit_ship.enemy_ship_life <= 0:
                    hit_ship.kill()
                    if hits_enemy_ship != {} and fase == 1:
                        score += 10
                    elif hits_enemy_ship != {} and fase == 2:
                        score += 20
                    elif hits_enemy_ship != {} and fase == 3:
                        score += 30

        check_enemy_ships_limit(enemy_ships)

        game_score = FONT.render("Score: " + str(score), False, (WHITE))

        if minutes == 1 and fase == 1:
            change_fase()
            bg = pygame.image.load("assets/imgs/mountains.png").convert()
            bg_rect = bg.get_rect()
            start_ticks = pygame.time.get_ticks()
            seconds = 0
            minutes = 0
            fase = 2

        if minutes == 2 and fase == 2:
            change_fase()
            bg = pygame.image.load("assets/imgs/space.jpg").convert()
            bg_rect = bg.get_rect()
            start_ticks = pygame.time.get_ticks()
            seconds = 0
            minutes = 0
            fase = 3

        if minutes == 3 and fase == 3:
            end_game()
            main()

        # pygame.draw.rect(DS, RED, pygame.Rect(20, 20, 100, 30))
        # pygame.draw.rect(DS, GREEN, pygame.Rect(20, 20, life, 30))

    # Draw / render

        DS.blit(game_fase_font, (10, 20))
        DS.blit(timelabel, (1180, 20))
        DS.blit(game_score, (10, 60))

        all_sprites.draw(DS)
    # *after* drawing everything, flip the display
        pygame.display.flip()


main()
