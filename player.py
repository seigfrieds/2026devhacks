import pygame
import math
from settings import *
from collider import Collider
from physics_objects import MovingCollidingObject

class Player(MovingCollidingObject):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.radius = 3
        self.turn_direction = 0
        self.walk_direction = 0
        self.rotation_angle = 0 * (math.pi / 180)
        self.move_speed = 2.5
        self.rotation_speed = 2 * (math.pi / 180)
        super().__init__(Collider(self.x, self.y, self.radius, self.radius)) 

    def update(self):
        keys = pygame.key.get_pressed()

        self.turn_direction = 0
        self.walk_direction = 0

        if keys[pygame.K_LEFT]:
            self.turn_direction = -1
        if keys[pygame.K_RIGHT]:
            self.turn_direction = 1
        if keys[pygame.K_UP]:
            self.walk_direction = 1
        if keys[pygame.K_DOWN]:
            self.walk_direction = -1

        #rotate
        self.rotation_angle += self.turn_direction * self.rotation_speed
    
    #will be called by physics engine
    def move(self):
        old_x = self.x
        old_y = self.y

        move_step = self.walk_direction * self.move_speed

        new_x = self.x + math.cos(self.rotation_angle) * move_step
        new_y = self.y + math.sin(self.rotation_angle) * move_step
        
        self.x = new_x
        self.y = new_y
        self.get_collider().change_collider_position(new_x, new_y) 

        def reset():
            self.x = old_x
            self.y = old_y
            self.get_collider().change_collider_position(old_x, old_y)

        return reset

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)