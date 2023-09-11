import sys
import pygame
from settings import Settings

def run_game():
    # initialize the pygame, settings and screen mode
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # set the color of backgroud
    bg_color = (230, 230, 230)
    # start the main loop for the game
    while True:
        # monitor events of the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the screen in everyloops
        screen.fill(bg_color)
        # make the screen mode to be seen
        pygame.display.flip()

run_game()