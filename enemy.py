import pygame
import math
import random
from settings import *
from utility import *
from enum import Enum
from collider import Collider
from physics_engine import PhysicsEngine

class Enemy:
    def __init__(self, phys_engine: PhysicsEngine, spawn_tile):
        self.x = spawn_tile[0] * TILE_SIZE + TILE_SIZE / 2
        self.y = spawn_tile[1] * TILE_SIZE + TILE_SIZE / 2
        self.current_tile = get_tile(self.x, self.y)
        self.radius = 8
        self.turn_direction = 0
        self.walk_direction = 1
        self.rotation_angle = Rotation.RIGHT
        self.move_speed = 1
        self.collider = Collider(self.x, self.y, self.radius, self.radius)
        self.physics_engine = phys_engine
        self.collided = False
        self.collision_time = 0
        self.collision_pause = 1000 # 1 second pause before rotating

    def get_collider(self):
        return self.collider
    
    def update(self, world_map):
        if self.collided:
            self.check_pause_timer()
        else:
            self.turn_direction = 0
            self.check_rotation(world_map)

            #move
            move_step = self.walk_direction * self.move_speed
            new_x = self.x + math.cos(self.rotation_angle.value) * move_step
            new_y = self.y + math.sin(self.rotation_angle.value) * move_step
            self.collider.change_collider_position(new_x, new_y)
            if self.physics_engine.collider_is_colliding(self.collider):
                self.collider.change_collider_position(self.x, self.y)
                self.collided = True
                self.collision_time = pygame.time.get_ticks()
            else:
                self.x = new_x
                self.y = new_y
        self.current_tile = get_tile(self.x, self.y)

    def check_rotation(self, world_map):
        match self.rotation_angle:
            case Rotation.RIGHT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x + 1)] == 1 and
                    get_tile(self.x + TILE_SIZE / 2, self.y).x != self.current_tile.x):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.DOWN:
                if (world_map.map[int(self.current_tile.y + 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.x, self.y + TILE_SIZE / 2).y != self.current_tile.y):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.LEFT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x - 1)] == 1 and
                    get_tile(self.x - TILE_SIZE / 2, self.y).x != self.current_tile.x):
                    self.rotate()
                    self.check_rotation(world_map)
            case Rotation.UP:
                if (world_map.map[int(self.current_tile.y - 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.y, self.y - TILE_SIZE / 2).y != self.current_tile.y):
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
        current_time = pygame.time.get_ticks()
        if current_time - self.collision_time > self.collision_pause:
            self.collided = False
            self.flip_rotation()

    def render(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), self.radius)

class Rotation(Enum):
    RIGHT = 0
    DOWN = math.pi / 2
    LEFT = math.pi
    UP = 3 * math.pi / 2

    def random():
        return random.choice(list(Rotation))