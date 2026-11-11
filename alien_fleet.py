
"""
Program Name: Alien Invasion - Incoming Enemy Formation
Author: Abdullah Rashid
Purpose: Create and manage small advancing enemy formations.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 11, 2026
"""

import pygame

from alien import Alien


class AlienFleet:
    """Create and manage small groups of advancing enemies."""

    def __init__(self, game) -> None:
        """Initialize the enemy formation."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def create_fleet(self) -> None:
        """Create a compact five-enemy V-shaped formation."""
        self.aliens.empty()

        alien_width = self.settings.alien_w
        alien_height = self.settings.alien_h

        group_size = self.settings.enemy_group_size

        center_x = self.settings.screen_w // 2

        spacing = (
            alien_width + self.settings.alien_spacing_x
        )

        # Vertical positions create a shallow V formation.
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
        """Advance every enemy toward the player's ship."""
        self.aliens.update()

    def draw(self) -> None:
        """Draw all active enemies."""
        for alien in self.aliens.sprites():
            alien.draw_alien()

    def check_edges(self) -> bool:
        """Check whether any enemy has reached a screen edge."""
        return any(
            alien.check_edges()
            for alien in self.aliens.sprites()
        )

    def change_direction(self) -> None:
        """Reverse horizontal movement without stopping advancement."""
        self.settings.alien_direction *= -1

    def check_bottom(self) -> bool:
        """Check whether an enemy has reached the player's area."""
        return any(
            alien.rect.bottom >= self.settings.screen_h
            for alien in self.aliens.sprites()
        )
