import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class for managing bullets which were shot on ship"""
    def __init__(self, ai_settings, screen, ship):
        """set a bullet object in the location of ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        #set a rectangle as a bullet in(0, 0) and set correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullet location by float number
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """move bullets up"""
        # update mean use float number to express the location of bullets
        self.y -= self.speed_factor
        # update mean the location of bullets'rect 
        self.rect.y = self.y


    def draw_bullet(self):
        """draw bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
