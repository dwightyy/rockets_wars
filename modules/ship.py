import pygame
from modules.config import *


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
