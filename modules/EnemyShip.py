import pygame
from random import randint
from modules.ship import *

class EnemyShip(Ship):
    def __init__(self, x, y):
        Ship.__init__(self)
        self.speed_y = 2
        self.rect.centery = y
        self.rect.centerx = x
        self.points = self.get_move_points()
        self.column = 0
            
    def get_move_points(self):        
        first = 0
        points = []
        for i in range(5):
            points.append(randint(first, first + 256))
            first += 256
        return points

    def move(self):
        if self.rect.y <= 100:
            self.speed_y = 2
            print('foi')
        if self.rect.y >= 500:
            self.speed_y = -2
            print('foi 2')
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


    def update(self):
        self.speed_x = -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.check_boundaries()
        self.move()
