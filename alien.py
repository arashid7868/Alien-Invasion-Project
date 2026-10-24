
"""Define the alien sprite."""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

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
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h),
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        """Keep the alien stationary during the initial tutorial stage."""
        pass

    def draw_alien(self) -> None:
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)
