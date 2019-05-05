import pygame
from modules.ship import *

class EnemyShip(Ship):
    def __init__(self, x, y):
        Ship.__init__(self)
        self.rect.centery = y
        self.rect.centerx = x
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.check_boundaries()