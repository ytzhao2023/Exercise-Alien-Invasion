import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """initialize the ship and set the original location of the ship"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load the image of the ship and get the rectangle outside the image
        self.image = pygame.transform.scale_by(
            pygame.image.load("/Users/YT/Downloads/ship.bmp"), 0.2)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # put every new ship in the middle position at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # store float number in the center attribute of the ship
        self.center = float(self.rect.centerx)
        
        # moving signal
        self.moving_right = False
        self.moving_left = False
    
    
    def update(self):
        """according to moving signal to adjust the location of the ship """
        # update the center value of the ship, rather than rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # update rect according to self.center
        self.rect.centerx = self.center


    def blitme(self):
        """draw the ship at pointed location """
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """make the ship in the center of screen"""  
        self.center = self.screen_rect.centerx  