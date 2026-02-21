class CollidingObject():
    def __init__(self, c):
        self.collider = c

    def get_collider(self):
        return self.collider

class MovingCollidingObject(CollidingObject):
    def move() -> tuple[int, int]:
        raise NotImplementedError("Implement the method")