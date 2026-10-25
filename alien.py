"""Define the alien sprite."""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represent a single alien in the fleet."""

    def __init__(
        self,
        fleet: "AlienFleet",
        x: float,
        y: float,
    ) -> None:
        """Initialize the alien and set its position."""
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

    def update(self) -> None:
        """Move the alien horizontally with the fleet."""
        self.x += (
            self.settings.alien_speed
            * self.settings.alien_direction
        )
        self.rect.x = round(self.x)

    def check_edges(self) -> bool:
        """Return True if the alien has reached a screen edge."""
        return (
            self.rect.right >= self.screen_rect.right
            or self.rect.left <= self.screen_rect.left
        )

    def drop_down(self, distance: int) -> None:
        """Move the alien down by the specified distance."""
        self.rect.y += distance

    def draw_alien(self) -> None:
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)