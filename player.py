import pygame
import math
from settings import *
from collider import Collider
from physics_objects import MovingCollidingObject, LAYER_PLAYER, LAYER_POWERUP, LAYER_ENEMY

class Player(MovingCollidingObject):
    def __init__(self):
        self.radius = 3
        self.turn_direction = 0
        self.walk_direction = 0
        self.rotation_angle = 0 * (math.pi / 180)
        self.move_speed = 2.5
        self.rotation_speed = 2 * (math.pi / 180)
        super().__init__(250, 250, Collider(250, 250, self.radius, self.radius), LAYER_PLAYER) 

    def run_collision_handler(self, collided_objects):
        for collided_obj in collided_objects:
            if collided_obj.get_layer() == LAYER_POWERUP:
                event = pygame.event.Event(0, message="make sure to change the event id")
                pygame.event.post(event)
            if collided_obj.get_layer() == LAYER_ENEMY:
                event_params = {"player" : self}
                event = pygame.event.Event(GAME_OVER, event_params)
                pygame.event.post(event)

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

        #set velocity
        move_step = self.walk_direction * self.move_speed
        self.set_velocity(math.cos(self.rotation_angle) * move_step, math.sin(self.rotation_angle) * move_step)

    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.get_pos()[0], self.get_pos()[1]), self.radius)