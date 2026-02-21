from settings import *
import pygame

def get_tile(x,y):
    return pygame.Vector2(x // TILE_SIZE, y // TILE_SIZE)

def get_tile_coords(tile_x, tile_y):
    return pygame.Vector2(tile_x * TILE_SIZE + TILE_SIZE / 2, tile_y * TILE_SIZE + TILE_SIZE / 2)