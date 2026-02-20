from ray import *
from settings import *

class Ray_Caster():
    def __init__(self, player):
        self.player = player

    def castRays(self):
        ray_angle = self.player.rotation_angle - (FOV / 2)
        for i in range(NUM_RAYS):
            ray = Ray(ray_angle, self.player)
            ray.cast()
            ray_angle += FOV / NUM_RAYS