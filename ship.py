"""Define the player's ship."""

from pathlib import Path

import pygame


class Ship:
    """Manage the player's ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        image_path = (
            Path(__file__).resolve().parent
            / "Assets"
            / "images"
            / "ship.png"
        )

        self.image = pygame.image.load(
            str(image_path)
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.midbottom = (
            self.screen_rect.centerx,
            self.screen_rect.bottom - 10,
        )

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

        

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = round(self.x)

        if self.rect.left < 0:
            self.rect.left = 0
            self.x = float(self.rect.x)

        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.x = float(self.rect.x)

    def blitme(self):
        """Draw the player's ship on the screen."""
        self.screen.blit(self.image, self.rect)

        
