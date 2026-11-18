
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Create and manage a coordinated advancing alien formation.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 18, 2026
"""

from typing import TYPE_CHECKING

import pygame

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Create and control a coordinated group of advancing aliens."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the fleet and create its starting formation."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def create_fleet(self) -> None:
        """Create a compact five-alien V-shaped formation."""
        self.aliens.empty()

        alien_width = self.settings.alien_w
        group_size = self.settings.enemy_group_size

        center_x = self.settings.screen_w // 2

        spacing = (
            alien_width
            + self.settings.alien_spacing_x
        )

        vertical_offsets = [100, 65, 30, 65, 100]

        first_offset = -(group_size - 1) // 2

        for index in range(group_size):
            horizontal_offset = (
                first_offset + index
            ) * spacing

            x = (
                center_x
                + horizontal_offset
                - alien_width // 2
            )

            y = vertical_offsets[index] if index < len(
                vertical_offsets
            ) else 30

            alien = Alien(self, x, y)
            self.aliens.add(alien)

    def update(self) -> None:
        """Move the fleet and handle horizontal boundary changes."""
        if self.check_edges():
            self.change_direction()
            self.drop_fleet()

        self.aliens.update()

    def check_edges(self) -> bool:
        """Check whether any alien has reached a screen edge."""
        return any(
            alien.check_edges()
            for alien in self.aliens.sprites()
        )

    def change_direction(self) -> None:
        """Reverse the fleet's horizontal movement direction."""
        self.settings.alien_direction *= -1

    def drop_fleet(self) -> None:
        """Move every alien downward when the fleet reaches an edge."""
        for alien in self.aliens.sprites():
            alien.drop_down(
                self.settings.alien_drop_speed
            )

    def check_bottom(self) -> bool:
        """Check whether an alien has reached the bottom boundary."""
        return any(
            alien.rect.bottom >= self.settings.screen_h
            for alien in self.aliens.sprites()
        )

    def draw(self) -> None:
        """Draw every active alien in the formation."""
        for alien in self.aliens.sprites():
            alien.draw_alien()
