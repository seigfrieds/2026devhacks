import pygame
from ray import Ray
from settings import *

class Raycaster:
    def __init__(self, player):
        self.rays = []
        self.player = player
    
    def cast_all_rays(self):
        self.rays = []

        ray_angle = (self.player.rotation_angle - FOV / 2)
        for i in range(NUM_RAYS):
            ray = Ray(ray_angle, self.player)
            ray.cast()
            self.rays.append(ray)

            ray_angle += (FOV / NUM_RAYS) # FOV / NUM_RAYS
 
    def render(self, screen):
        for ray in self.rays:
            ray.render(screen)