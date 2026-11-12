
"""
Program Name: Alien Invasion - Enemy Arsenal
Author: Abdullah Rashid
Purpose: Manage the M1 enemy shooter, targeted projectiles,
firing intervals, and projectile limits.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 12, 2026
"""

from typing import TYPE_CHECKING

import pygame

from enemy_bullet import EnemyBullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class EnemyArsenal:
    """Manage the prototype enemy shooter and its projectiles."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the enemy shooter and projectile group."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.projectiles = pygame.sprite.Group()

        # Create one stationary enemy for the M1 prototype.
        self.shooter_image = pygame.image.load(
            self.settings.alien_file
        ).convert_alpha()

        self.shooter_image = pygame.transform.scale(
            self.shooter_image,
            (
                self.settings.alien_w,
                self.settings.alien_h,
            ),
        )

        self.shooter = pygame.sprite.Sprite()
        self.shooter.image = self.shooter_image
        self.shooter.rect = self.shooter_image.get_rect()

        self.shooter.rect.midtop = (
            self.settings.screen_w // 2,
            35,
        )

        self.last_fire_time = pygame.time.get_ticks()

    def update(self) -> None:
        """Update enemy projectiles and control enemy firing."""
        self.projectiles.update()
        self._remove_offscreen_projectiles()
        self._check_enemy_firing()

    def _check_enemy_firing(self) -> None:
        """Fire targeted projectiles at the player."""
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

        # Pass the shooter's firing coordinates to EnemyBullet.
        projectile = EnemyBullet(
            self.game,
            float(self.shooter.rect.centerx),
            float(self.shooter.rect.bottom),
        )

        self.projectiles.add(projectile)
        self.last_fire_time = current_time

    def _remove_offscreen_projectiles(self) -> None:
        """Remove enemy projectiles outside the screen."""
        for projectile in self.projectiles.copy():
            if projectile.is_off_screen():
                self.projectiles.remove(projectile)

    def draw(self) -> None:
        """Draw the prototype enemy and its projectiles."""
        self.screen.blit(
            self.shooter.image,
            self.shooter.rect,
        )

        for projectile in self.projectiles:
            projectile.draw_bullet()

    def empty(self) -> None:
        """Remove all active enemy projectiles."""
        self.projectiles.empty()
