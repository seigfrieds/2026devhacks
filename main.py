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

# Setup physics engine
physics_engine = PhysicsEngine()

# Setup map
newMap = Map()

# Setup player
player = Player(physics_engine)
raycaster = Raycaster(player)


# Setup enemies
spawn_locations = [(1,4), (6,2), (5,4)]
enemies = [Enemy(physics_engine,x) for x in spawn_locations]

physics_engine.register_colliders(newMap.get_colliders())
physics_engine.register_collider(player.get_collider())
for enemy in enemies:
    physics_engine.register_collider(enemy.get_collider())
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
    for enemy in enemies:
        enemy.update(newMap)
    raycaster.cast_all_rays()

    # render here
    newMap.draw(screen)
    player.render(screen)
    for enemy in enemies:
        enemy.render(screen)
    raycaster.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
