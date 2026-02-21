# Example file showing a basic pygame "game loop"
import pygame
from settings import *
from Map import Map
from player import Player
from enemy import Enemy
from raycaster import Raycaster
from physics_engine import PhysicsEngine

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
game_over = False

# Setup physics engine
physics_engine = PhysicsEngine()

# Setup map
newMap = Map()

# Setup player
player = Player()
raycaster = Raycaster(player)

# Setup enemies
spawn_locations = [(1,4), (5,1), (11,1), (12,6), (7,1), (4,3)]
enemies = [Enemy(x) for x in spawn_locations]

physics_engine.register_colliding_objects(newMap.get_colliders())
physics_engine.register_moving_colliding_object(player)
for enemy in enemies:
    physics_engine.register_moving_colliding_object(enemy)

# text display
font = pygame.font.SysFont(None, 48)
text_surface = font.render("Good Game!", True, "BLUE")
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - TILE_SIZE / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            running = False
        if event.type == GAME_OVER:
            game_over = True
        if event.type == VICTORY:
            game_over = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #pygame.display.flip()

    # update game here
    player.update()
    for enemy in enemies:
        enemy.update(newMap)
    raycaster.cast_all_rays()

    # process physics
    physics_engine.process_physics()

    # render here
    newMap.draw(screen)
    if (game_over):
        screen.blit(text_surface, text_rect)   
    else:
        player.render(screen)
        for enemy in enemies:
            enemy.render(screen)
        raycaster.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
