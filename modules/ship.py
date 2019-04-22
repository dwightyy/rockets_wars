class Ship():
    def __init__(self, pos_x, pos_y, sprite):
        self.accel = 0
        self.y_vel = 0
        self.x_vel = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprite = sprite

    def move_up():
        self.y_vel = y_vel - self.accel
        self.pos_y = self.pos_y - y_vel

    def move_down():
        self.y_vel = y_vel + self.accel
        self.pos_y = self.pos_y + y_vel

    def move_left():
        self.x_vel = x_vel - self.accel
        self.pos_x = self.pos_x - x_vel

    def move_right():
        self.x_vel = x_vel + self.accel
        self.pos_x = self.pos_y + x_vel
