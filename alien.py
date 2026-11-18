
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Define an advancing alien that moves with its fleet.
Starter Code: https://github.com/RedBeard41/alien_Invasion_Project
Date Updated: November 18, 2026
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represent an individual advancing enemy spaceship."""

    def __init__(
        self,
        fleet: "AlienFleet",
        x: float,
        y: float,
    ) -> None:
        """Initialize an alien at its assigned fleet position."""
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
        self.x = float(x)
        self.y = float(y)

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def update(self) -> None:
        """Move the alien horizontally and advance it downward."""
        self.x += (
            self.settings.alien_speed
            * self.settings.alien_direction
        )

        self.y += self.settings.alien_approach_speed

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def check_edges(self) -> bool:
        """Return True when the alien reaches a horizontal screen edge."""
        return (
            self.rect.right >= self.screen_rect.right
            or self.rect.left <= self.screen_rect.left
        )

    def drop_down(self, distance: int) -> None:
        """Move the alien downward when the fleet changes direction."""
        self.y += distance
        self.rect.y = round(self.y)

    def draw_alien(self) -> None:
        """Draw the alien on the game screen."""
        self.screen.blit(self.image, self.rect)
