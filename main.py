# Example file showing a basic pygame "game loop"
import pygame
from settings import *
from Map import Map
from player import Player
from raycaster import Raycaster
from physics_engine import PhysicsEngine

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# Setup physics engine
physics_engine = PhysicsEngine()

# Setup map
newMap = Map()

# Setup player
player = Player()
raycaster = Raycaster(player)

physics_engine.register_colliding_objects(newMap.get_colliders())
physics_engine.register_moving_colliding_object(player)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # update game here
    player.update()
    raycaster.cast_all_rays()

    # process physics
    physics_engine.process_physics()

    # render here
    newMap.draw(screen)
    player.render(screen)
    raycaster.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
