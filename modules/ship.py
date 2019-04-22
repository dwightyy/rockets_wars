#TODO BUG a nova pula para frente e para trás na primeira vez que aperta a direção
#TODO BUG a nave vai para baixo quando aperta para cima e vice versa

class Ship():
    def __init__(self, pos_x, pos_y, sprite):
        self.accel = 10
        self.y_vel = 0
        self.x_vel = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprite = sprite

    def move_up(self):
        self.y_vel = self.y_vel - self.accel
        self.pos_y = self.pos_y - self.y_vel

    def move_down(self):
        self.y_vel = self.y_vel + self.accel
        self.pos_y = self.pos_y + self.y_vel

    def move_left(self):
        self.x_vel = self.x_vel - self.accel
        self.pos_x = self.pos_x - self.x_vel

    def move_right(self):
        self.x_vel = self.x_vel + self.accel
        self.pos_x = self.pos_y + self.x_vel
