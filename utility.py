from settings import *
import pygame

def get_tile(x,y):
    return pygame.Vector2(x // TILE_SIZE, y // TILE_SIZE)