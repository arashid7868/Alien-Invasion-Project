
"""
Program Name: Alien Invasion - Advancing Enemy
Author: Abdullah Rashid
Purpose: Define an enemy that advances toward the player's ship
while moving horizontally with its formation.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 11, 2026
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represent an advancing enemy spaceship."""

    def __init__(
        self,
        fleet: "AlienFleet",
        x: float,
        y: float,
    ) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fleet.settings

        self.image = pygame.image.load(
            self.settings.alien_file
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.alien_w,
                self.settings.alien_h,
            ),
        )

        self.rect = self.image.get_rect()
        self.rect.x = round(x)
        self.rect.y = round(y)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Advance the alien downward and move it horizontally."""
        self.x += (
            self.settings.alien_speed
            * self.settings.alien_direction
        )

        self.y += self.settings.alien_approach_speed

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def check_edges(self) -> bool:
        """Return True when the alien reaches a screen edge."""
        return (
            self.rect.right >= self.screen_rect.right
            or self.rect.left <= self.screen_rect.left
        )

    def drop_down(self, distance: int) -> None:
        """Move the alien downward by a specified distance."""
        self.y += distance
        self.rect.y = round(self.y)

    def draw_alien(self) -> None:
        """Draw the enemy spaceship."""
        self.screen.blit(self.image, self.rect)
