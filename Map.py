import settings
import pygame


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

    
    def draw(self, screen):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (j*settings.TILE_SIZE, i*settings.TILE_SIZE, settings.TILE_SIZE-1, settings.TILE_SIZE-1))   # Draw a black square
                
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (j*settings.TILE_SIZE, i*settings.TILE_SIZE, settings.TILE_SIZE-1, settings.TILE_SIZE-1))   # Draw a black square
