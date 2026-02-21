import math
import pygame

FOV = 60*math.pi/180
TILE_SIZE = 64

# Rows
row = 8
col = 8

WINDOW_WIDTH = col * TILE_SIZE * 2
WINDOW_HEIGHT = row * TILE_SIZE

RESOLUTION = 4 #higher = more rays
NUM_RAYS = WINDOW_WIDTH // RESOLUTION

GAME_OVER = pygame.event.custom_type()
GAME_OVER_PARAMETERS = {}




