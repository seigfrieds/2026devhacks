import pygame
import math

#all angles within 0-2pi 
def normalize_angle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle += 2 * math.pi
    return angle

class Ray:
    def __init__(self, angle, player):
        self.ray_angle = normalize_angle(angle)
        self.player = player

    def cast(self):
        pass

    def render(self, screen):
        pygame.draw.line(screen, "red", (self.player.x, self.player.y), (self.player.x + math.cos(self.ray_angle) * 100, self.player.y + math.sin(self.ray_angle) * 100))