import sys

import pygame

def run_game():
    # initialize the pygame and set a screen mode
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # start the main loop for the game
    while True:
        # monitor events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # make the screen mode to be seen
        pygame.display.flip()

run_game()


