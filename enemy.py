import pygame
import math
import random
from settings import *
from utility import *
from enum import Enum
from collider import Collider
from physics_engine import PhysicsEngine
from physics_objects import *

class Enemy(MovingCollidingObject):
    def __init__(self, spawn_tile):
        x = spawn_tile[0] * TILE_SIZE + TILE_SIZE / 2
        y = spawn_tile[1] * TILE_SIZE + TILE_SIZE / 2
        self.radius = 8
        self.current_tile = get_tile(x, y)
        self.turn_direction = 0
        self.walk_direction = 1
        self.rotation_angle = Rotation.RIGHT
        self.move_speed = 1.5
        super().__init__(x, y, Collider(x, y, self.radius, self.radius), LAYER_ENEMY)
        self.collided = False
        self.collision_time = 0
        self.collision_pause = 1000 # 1 second pause before rotating
    
    def run_collision_handler(self, collided_objects):
        self.collided = True
        self.set_velocity(0,0)
        self.collision_time = pygame.time.get_ticks()

        for collided_object in collided_objects:
            if collided_object.get_layer() == LAYER_PLAYER:
                event_params = {"player" : collided_object}
                event = pygame.event.Event(GAME_OVER, event_params)
                pygame.event.post(event)

    def update(self, world_map):
        if self.collided:
            self.check_pause_timer()
        else:
            self.turn_direction = 0
            current_pos = self.get_pos()
            if current_pos[1] > (WINDOW_HEIGHT - TILE_SIZE):
                self.flip_rotation()
            self.check_rotation(world_map)

            #move
            move_step = self.walk_direction * self.move_speed
            self.set_velocity(math.cos(self.rotation_angle.value) * move_step, math.sin(self.rotation_angle.value) * move_step)

        self.current_tile = get_tile(self.get_pos()[0], self.get_pos()[1])

    def check_rotation(self, world_map):
        match self.rotation_angle:
            case Rotation.RIGHT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x + 1)] == 1 and
                    get_tile(self.get_pos()[0] + TILE_SIZE / 2, self.get_pos()[1]).x != self.current_tile.x):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.DOWN:
                if (world_map.map[int(self.current_tile.y + 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.get_pos()[0], self.get_pos()[1] + TILE_SIZE / 2).y != self.current_tile.y):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.LEFT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x - 1)] == 1 and
                    get_tile(self.get_pos()[0] - TILE_SIZE / 2, self.get_pos()[1]).x != self.current_tile.x):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.UP:
                if (world_map.map[int(self.current_tile.y - 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.get_pos()[1], self.get_pos()[1] - TILE_SIZE / 2).y != self.current_tile.y):
                    self.rotate()
                    self.check_rotation(world_map)

    def rotate(self):
        self.rotation_angle = Rotation.random()

    def flip_rotation(self):
        match (self.rotation_angle):
            case Rotation.RIGHT:
                self.rotation_angle = Rotation.LEFT
            case Rotation.LEFT:
                self.rotation_angle = Rotation.RIGHT
            case Rotation.UP:
                self.rotation_angle = Rotation.DOWN
            case Rotation.DOWN:
                self.rotation_angle = Rotation.UP

    def check_pause_timer(self):
        #print("do we collide")
        current_time = pygame.time.get_ticks()
        if current_time - self.collision_time > self.collision_pause:
            self.collided = False
            self.flip_rotation()

    def render(self, screen):
        pygame.draw.circle(screen, "blue", (self.get_pos()[0], self.get_pos()[1]), self.radius)

class Rotation(Enum):
    RIGHT = 0
    DOWN = math.pi / 2
    LEFT = math.pi
    UP = 3 * math.pi / 2

    def random():
        return random.choice(list(Rotation))