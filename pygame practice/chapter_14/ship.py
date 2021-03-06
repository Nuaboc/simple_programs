import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        # self.images = list([pygame.image.load('images/ani_test{0}.png'.format(i)) for i in range(1, 5)])
        self.anim_test = list(pygame.image.load('images/ani_test{0}.png'.format(i)).convert_alpha() for i in range(1, 5))
        self.test_frames = 4
        self.rect = self.anim_test[0].get_rect()
        self.screen_rect = screen.get_rect()
        self.image = self.anim_test[1]

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False

        self.frames = 4
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self, x):
        """Draw the ship at its current location."""
        self.screen.blit(self.anim_test[x], self.rect)
