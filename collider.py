import pygame

#assuming collider will be rectangle.. but should probably be a base class
class Collider:
    def __init__(self, left, top, width, height):
        self.collider = pygame.Rect(left, top, width, height)

    def check_collision(self, other_collider):
        return self.collider.colliderect(other_collider.collider)

    def change_collider_position(self, new_left, new_top):
        self.collider.left = new_left
        self.collider.top = new_top