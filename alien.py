
"""Define the alien sprite."""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Alien(Sprite):
    """A class to represent a single alien."""

    def __init__(
        self,
        game: "AlienInvasion",
        x: float,
        y: float,
    ) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h),
        )

        self.rect = self.image.get_rect()
        self.rect.x = round(x)
        self.rect.y = round(y)

        self.x = float(self.rect.x)
        self.direction = 1

    def update(self) -> None:
        """Move the alien horizontally and reverse at screen edges."""
        self.x += self.settings.alien_speed * self.direction
        self.rect.x = round(self.x)

        if self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.x = float(self.rect.x)
            self.direction = -1
        elif self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left
            self.x = float(self.rect.x)
            self.direction = 1

    def draw_alien(self) -> None:
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)

    @classmethod
    def create_aliens_row(
        cls,
        game: "AlienInvasion",
        aliens: pygame.sprite.Group,
        y: int,
    ) -> None:
        """Create one row of aliens across the screen."""
        settings = game.settings

        alien_width = settings.alien_w
        alien_height = settings.alien_h
        horizontal_spacing = alien_width

        x = 0
        while x + alien_width <= settings.screen_w:
            alien = cls(game, x, y)
            aliens.add(alien)
            x += alien_width + horizontal_spacing
