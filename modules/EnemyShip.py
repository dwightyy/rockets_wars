import pygame
from random import randint
from modules.ship import *
from modules.config import *

class EnemyBullet(Bullet):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)     
        Bullet.__init__(self, x, y)
        self.image = pygame.Surface((20, 10))
        self.image.fill((BLACK))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        print('----------O X É:', x)
        self.rect.centerx = x - 100
        self.speed_x = 10

    def update(self):
        
        self.rect.x -= self.speed_x
        # kill if off top of screen
        if self.rect.right > W:
            self.kill()



class EnemyShip(Ship):
    def __init__(self, x, y, enemy_ship_life):
        Ship.__init__(self)
        self.image = pygame.image.load('assets/imgs/enemyShip.png').convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.speed_y = 2
        self.rect.centery = y
        self.rect.centerx = x
        self.points = self.get_move_points()
        self.column = 0
        self.enemy_ship_life = enemy_ship_life
        self.start_ticks = pygame.time.get_ticks()

    def get_move_points(self):
        first = 0
        points = []
        for i in range(5):
            points.append(randint(first, first + 256))
            first += 256
        return points

    def move(self):
        if self.rect.y <= randint(-20, 50):
            self.speed_y = 2
        if self.rect.y >= randint(550, 720):
            self.speed_y = -2

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def update(self):
        self.speed_x = -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # self.check_boundaries()
        self.move()

    
    def shoot(self, all_sprites, bullets):
        bullet = EnemyBullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
        return all_sprites

