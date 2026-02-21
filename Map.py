import settings
import pygame
from settings import *
from collider import Collider
from physics_objects import CollidingObject, NO_LAYER

class Map:
    map = []
    def __init__(self):
        #map grid
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        ]

        #register boxes and colliders from the map grid
        self.boxes = [[0 for j in range(col)] for i in range(row)]
        self.colliders = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                rect = pygame.Rect(j*settings.TILE_SIZE, i*settings.TILE_SIZE, settings.TILE_SIZE-1, settings.TILE_SIZE-1)
                self.boxes[i][j] = rect

                if self.map[i][j] == 1: # 1 means its a wall -> should be a collider
                    self.colliders.append(CollidingObject(Collider(rect.left, rect.top, rect.width, rect.height), NO_LAYER))
    
    def get_colliders(self):
        return self.colliders
    
    def draw(self, screen):
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                color = "black" if self.map[i][j] == 1 else "white"

                pygame.draw.rect(screen, color, self.boxes[i][j])
