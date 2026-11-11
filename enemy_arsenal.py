
"""
Program Name: Alien Invasion - Enemy Arsenal
Author: Abdullah Rashid
Purpose: Manage enemy projectiles, sequential firing intervals,
and projectile limits.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 11, 2026
"""

from typing import TYPE_CHECKING

import pygame

from enemy_bullet import EnemyBullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class EnemyArsenal:
    """Manage projectiles fired by the enemy fleet."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the enemy projectile group and firing timer."""
        self.game = game
        self.settings = game.settings

        self.projectiles = pygame.sprite.Group()
        self.last_fire_time = pygame.time.get_ticks()
        self.next_firing_index = 0

    def update(self) -> None:
        """Update enemy projectiles and control enemy firing."""
        self.projectiles.update()
        self._remove_offscreen_projectiles()
        self._check_enemy_firing()

    def _check_enemy_firing(self) -> None:
        """Fire sequentially from left to right across the formation."""
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

        aliens = sorted(
            self.game.fleet.aliens.sprites(),
            key=lambda alien: alien.rect.centerx,
        )

        if not aliens:
            return

        self.next_firing_index %= len(aliens)

        firing_alien = aliens[self.next_firing_index]

        projectile = EnemyBullet(
            self.game,
            firing_alien,
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
