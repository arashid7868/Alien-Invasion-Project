
"""Manage the player's ship."""

from typing import TYPE_CHECKING

import pygame

from arsenal import Arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:
    """Manage the player's ship."""

    def __init__(self, game: "AlienInvasion", arsenal: Arsenal) -> None:
        """Initialize the ship."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(
            self.settings.ship_file
        ).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h),
        )

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

        self.arsenal = arsenal

    def update(self) -> None:
        """Update ship movement."""
        self._update_ship_movement()

    def _update_ship_movement(self) -> None:
        """Move the ship while keeping it inside the screen."""
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed

        self.rect.x = round(self.x)

        if self.rect.left < self.boundaries.left:
            self.rect.left = self.boundaries.left
            self.x = float(self.rect.x)

        if self.rect.right > self.boundaries.right:
            self.rect.right = self.boundaries.right
            self.x = float(self.rect.x)

    def draw(self) -> None:
        """Draw the player's ship."""
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Request a projectile from the arsenal."""
        return self.arsenal.fire_bullet()
