import settings
import pygame
from settings import *
from collider import Collider

class Map:
    map = []
    def __init__(self):
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

        #register boxes and colliders (these are static..)
        self.boxes = [[0 for j in range(col)] for i in range(row)]
        self.colliders = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                rect = pygame.Rect(j*settings.TILE_SIZE, i*settings.TILE_SIZE, settings.TILE_SIZE-1, settings.TILE_SIZE-1)

                if self.map[i][j] == 1: # if one.. should be collider as well
                    self.boxes[i][j] = rect
                    self.colliders.append(Collider(rect.left, rect.top, rect.width, rect.height))
                else:
                    self.boxes[i][j] = rect
    
    def get_colliders(self):
        return self.colliders
    
    def draw(self, screen):
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                color = "black" if self.map[i][j] == 1 else "white"

                pygame.draw.rect(screen, color, self.boxes[i][j])
