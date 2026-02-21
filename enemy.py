import pygame
import math
import random
from settings import *
from utility import *
from enum import Enum

class Enemy:
    def __init__(self, spawn_tile):
        self.x = spawn_tile[0] * TILE_SIZE + TILE_SIZE / 2
        self.y = spawn_tile[1] * TILE_SIZE + TILE_SIZE / 2
        self.current_tile = get_tile(self.x, self.y)
        self.radius = 8
        self.turn_direction = 0
        self.walk_direction = 1
        self.rotation_angle = Rotation.RIGHT
        self.move_speed = 1

    def update(self, world_map):
        self.turn_direction = 0
        self.check_rotation(world_map)

        #move
        move_step = self.walk_direction * self.move_speed
        self.x += math.cos(self.rotation_angle.value) * move_step
        self.y += math.sin(self.rotation_angle.value) * move_step

        self.current_tile = get_tile(self.x, self.y)

    def check_rotation(self, world_map):
        match self.rotation_angle:
            case Rotation.RIGHT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x + 1)] == 1 and
                    get_tile(self.x + TILE_SIZE / 2, self.y).x != self.current_tile.x):
                    self.rotation_angle = Rotation.random()
                    self.check_rotation(world_map)
            case Rotation.DOWN:
                if (world_map.map[int(self.current_tile.y + 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.x, self.y + TILE_SIZE / 2).y != self.current_tile.y):
                    self.rotation_angle = Rotation.random()
                    self.check_rotation(world_map)
            case Rotation.LEFT:
                if (world_map.map[int(self.current_tile.y)][int(self.current_tile.x - 1)] == 1 and
                    get_tile(self.x - TILE_SIZE / 2, self.y).x != self.current_tile.x):
                    self.rotation_angle = Rotation.random()
                    self.check_rotation(world_map)
            case Rotation.UP:
                if (world_map.map[int(self.current_tile.y - 1)][int(self.current_tile.x)] == 1 and
                    get_tile(self.y, self.y - TILE_SIZE / 2).y != self.current_tile.y):
                    self.rotation_angle = Rotation.random()
                    self.check_rotation(world_map)

    def render(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), self.radius)

class Rotation(Enum):
    RIGHT = 0
    DOWN = math.pi / 2
    LEFT = math.pi
    UP = 3 * math.pi / 2

    def random():
        return random.choice(list(Rotation))