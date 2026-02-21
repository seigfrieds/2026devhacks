import pygame
import math
from settings import *
from collider import Collider
from physics_engine import PhysicsEngine

class Player:
    def __init__(self, phys_engine: PhysicsEngine):
        self.x = 250
        self.y = 250
        self.radius = 3
        self.turn_direction = 0
        self.walk_direction = 0
        self.rotation_angle = 0 * (math.pi / 180)
        self.move_speed = 2.5
        self.rotation_speed = 2 * (math.pi / 180)
        self.collider = Collider(self.x, self.y, self.radius, self.radius)
        self.physics_engine = phys_engine

    def get_collider(self):
        return self.collider

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

        #move
        move_step = self.walk_direction * self.move_speed
        new_x = self.x + math.cos(self.rotation_angle) * move_step
        new_y = self.y + math.sin(self.rotation_angle) * move_step
        self.collider.change_collider_position(new_x, new_y)
        if self.physics_engine.collider_is_colliding(self.collider):
            print("test")
            self.collider.change_collider_position(self.x, self.y)
        else:
            self.x = new_x
            self.y = new_y

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)