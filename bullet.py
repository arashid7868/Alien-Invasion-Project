
"""Define a single projectile."""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Manage a single projectile."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the projectile at the ship's position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            self.settings.bullet_file
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.bullet_w,
                self.settings.bullet_h,
            ),
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the projectile upward."""
        self.y -= self.settings.bullet_speed
        self.rect.y = round(self.y)

    def draw_bullet(self) -> None:
        """Draw the projectile."""
        self.screen.blit(self.image, self.rect)
