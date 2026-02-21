NO_LAYER = -1
LAYER_PLAYER = 1
LAYER_POWERUP = 2

class CollidingObject():
    def __init__(self, c, l):
        self.collider = c
        self.layer = l

    def get_collider(self):
        return self.collider
    
    def get_layer(self):
        return self.layer

    def run_collision_handler(self, collided_objects):
        pass #user can override..

class MovingCollidingObject(CollidingObject):
    def __init__(self, x, y, c, l):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        super().__init__(c, l)

    def get_pos(self):
        return (self.x, self.y)
    
    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def set_velocity(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self):
        old_x = self.x
        old_y = self.y

        self.x += self.velocity_x
        self.y += self.velocity_y
        self.get_collider().change_collider_position(self.x, self.y)

        def reset():
            self.x = old_x
            self.y = old_y
            self.get_collider().change_collider_position(old_x, old_y)

        return reset