import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # initialize the pygame, settings and screen mode
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #set a ship
    ship = Ship(screen)
    # set the color of backgroud
    bg_color = (230, 230, 230)
    # start the main loop for the game
    while True:
        # monitor events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the screen in everyloops
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # make the screen mode to be seen
        pygame.display.flip()

run_game()