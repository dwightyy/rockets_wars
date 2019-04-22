


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
