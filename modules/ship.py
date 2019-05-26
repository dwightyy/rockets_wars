import pygame
from modules.config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_x = -10

    def update(self):
        self.rect.x -= self.speed_x
        # kill if off top of screen
        if self.rect.right > W:
            self.kill()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/imgs/spaceship.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #self.radius = 25
        self.rect.centery = H / 2
        self.rect.centerx = 50
        self.speed_x = 0
        self.damage = 100

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        k = pygame.key.get_pressed()
        if k[pygame.K_LEFT]:
            self.move_left()
        if k[pygame.K_RIGHT]:
            self.move_right()
        if k[pygame.K_UP]:
            self.move_up()
        if k[pygame.K_DOWN]:
            self.move_down()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.check_boundaries()

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
        return all_sprites

    def check_boundaries(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > H:
            self.rect.bottom = H
        elif self.rect.right > W:
            self.rect.right = W
        elif self.rect.left < 0:
            self.rect.left = 0

    def move_up(self):
        self.speed_y = -8

    def move_down(self):
        self.speed_y = 8

    def move_left(self):
        self.speed_x = -8

    def move_right(self):
        self.speed_x = 8
