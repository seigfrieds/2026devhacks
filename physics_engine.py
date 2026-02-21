from collider import Collider
from physics_objects import CollidingObject, MovingCollidingObject

#incredibly rudimentary.. no filtering of objects to check collisions
class PhysicsEngine:
    def __init__(self):
        self.colliding_objects: list[CollidingObject] = []        
        self.moving_colliding_objects: list[MovingCollidingObject] = []
    
    def register_colliding_object(self, colliding_obj):
        self.colliding_objects.append(colliding_obj)

    def deregister_colliding_object(self, colliding_obj):
        self.colliding_objects.remove(colliding_obj)

    def register_colliding_objects(self, colliding_objs):
        for colliding_obj in colliding_objs:
            self.register_colliding_object(colliding_obj)

    def register_moving_colliding_object(self, moving_colliding_obj):
        self.register_colliding_object(moving_colliding_obj)

        self.moving_colliding_objects.append(moving_colliding_obj)

    def deregister_moving_colliding_object(self, moving_colliding_obj):
        self.deregister_colliding_object(moving_colliding_obj)

        self.moving_colliding_objects.remove(moving_colliding_obj)

    def process_physics(self):
        for moving_colliding_object in self.moving_colliding_objects:
            reset_callback = moving_colliding_object.move()

            for other_colliding_object in self.colliding_objects:
                collided_objects = []

                if moving_colliding_object != other_colliding_object:
                    collided = moving_colliding_object.get_collider().check_collision(other_colliding_object.get_collider())
                    if collided:
                        reset_callback()
                        collided_objects.append(other_colliding_object)

                if len(collided_objects) > 0:
                    moving_colliding_object.run_collision_handler(collided_objects)
