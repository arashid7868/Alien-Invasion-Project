
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Manage targeted return-fire from the advancing alien fleet.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 18, 2026
"""

import random
from typing import TYPE_CHECKING

import pygame

from enemy_bullet import EnemyBullet

if TYPE_CHECKING:
    from alien_fleet import AlienFleet
    from alien_invasion import AlienInvasion


class EnemyArsenal:
    """Manage targeted enemy projectiles fired by the alien fleet."""

    def __init__(
        self,
        game: "AlienInvasion",
        fleet: "AlienFleet",
    ) -> None:
        """Initialize the enemy projectile system."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.fleet = fleet

        self.projectiles = pygame.sprite.Group()
        self.last_fire_time = pygame.time.get_ticks()

    def update(self) -> None:
        """Update enemy projectiles and control fleet firing."""
        self.projectiles.update()
        self._remove_offscreen_projectiles()
        self._check_enemy_firing()

    def _check_enemy_firing(self) -> None:
        """Allow an active alien to fire toward the player's ship."""
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

        active_aliens = self.fleet.aliens.sprites()

        if not active_aliens:
            return

        shooter = random.choice(active_aliens)

        projectile = EnemyBullet(
            self.game,
            float(shooter.rect.centerx),
            float(shooter.rect.bottom),
        )

        self.projectiles.add(projectile)
        self.last_fire_time = current_time

    def _remove_offscreen_projectiles(self) -> None:
        """Remove projectiles that have left the screen."""
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
        self.last_fire_time = pygame.time.get_ticks()
