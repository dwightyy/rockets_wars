from pygame import draw
from modules.config import *


class Ship():
    def __init__(self, pos_x, pos_y, sprite):
        self.accel = 5
        self.y_vel = 0
        self.x_vel = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprite = sprite

    def move_up(self):
        self.pos_y -= self.accel

    def move_down(self):
        self.pos_y += self.accel

    def move_left(self):
        self.pos_x -= self.accel

    def move_right(self):
        self.pos_x += self.accel

    def fire(self, DS, bullets):
        for t in range(len(bullets)):
            if(bullets[t]['status'] == 1):
                draw.rect(DS, RED, pygame.Rect(
                    bullets[t]['x'], bullets[t]['y'], 10, 5))

                bullets[t]['x'] += 10
