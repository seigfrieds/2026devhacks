from collider import Collider

#incredibly rudimentary.. no filtering of objects to check collisions
class PhysicsEngine:
    def __init__(self):
        self.colliders: list[Collider] = []
        self.num_colliders = 0
    
    def register_collider(self, collider):
        self.colliders.append(collider)
        self.num_colliders += 1

    def register_colliders(self, colliders):
        for collider in colliders:
            self.register_collider(collider)
    
    #check if a given collider is colliding
    def collider_is_colliding(self, collider):
        for i in range(self.num_colliders):
            other_collider = self.colliders[i]

            if collider != other_collider:
                collided = collider.check_collision(other_collider)
                if collided:
                    return True
        
        return False