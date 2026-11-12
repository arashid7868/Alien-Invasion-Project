
"""
Program Name: Alien Invasion - Enemy Arsenal
Author: Abdullah Rashid
Purpose: Manage enemy projectiles, firing intervals,
and projectile limits independently of the enemy fleet.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 12, 2026
"""

from typing import TYPE_CHECKING

import pygame

from enemy_bullet import EnemyBullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class EnemyArsenal:
    """Manage projectiles fired from enemy launch positions."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the enemy projectile group and firing timer."""
        self.game = game
        self.settings = game.settings

        self.projectiles = pygame.sprite.Group()
        self.last_fire_time = pygame.time.get_ticks()
        self.next_firing_index = 0

        self.firing_positions = self._create_firing_positions()

    def _create_firing_positions(self) -> list[tuple[float, float]]:
        """Create evenly spaced launch positions across the screen."""
        position_count = self.settings.enemy_group_size
        screen_width = self.settings.screen_w

        spacing = screen_width / (position_count + 1)
        launch_y = 80.0

        return [
            (spacing * (index + 1), launch_y)
            for index in range(position_count)
        ]

    def update(self) -> None:
        """Update enemy projectiles and control enemy firing."""
        self.projectiles.update()
        self._remove_offscreen_projectiles()
        self._check_enemy_firing()

    def _check_enemy_firing(self) -> None:
        """Fire sequentially from left to right across launch positions."""
        current_time = pygame.time.get_ticks()

        if (
            current_time - self.last_fire_time
            < self.settings.enemy_fire_interval
        ):
            return

        if (
            len(self.projectiles)
            >= self.settings.enemy_bullet_amount
        ):
            return

        if not self.firing_positions:
            return

        self.next_firing_index %= len(self.firing_positions)

        start_x, start_y = self.firing_positions[
            self.next_firing_index
        ]

        projectile = EnemyBullet(
            self.game,
            start_x,
            start_y,
        )

        self.projectiles.add(projectile)

        self.next_firing_index += 1
        self.last_fire_time = current_time

    def _remove_offscreen_projectiles(self) -> None:
        """Remove enemy projectiles that have left the screen."""
        for projectile in self.projectiles.copy():
            if projectile.is_off_screen():
                self.projectiles.remove(projectile)

    def draw(self) -> None:
        """Draw all active enemy projectiles."""
        for projectile in self.projectiles:
            projectile.draw_bullet()

    def empty(self) -> None:
        """Remove all active enemy projectiles."""
        self.projectiles.empty()
        self.next_firing_index = 0
        self.last_fire_time = pygame.time.get_ticks()
