
"""
Program Name: Alien Invasion - Targeted Enemy Projectile
Author: Abdullah Rashid
Purpose: Define enemy projectiles that aim toward the player's ship.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 11, 2026
"""

import math
from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from alien import Alien


class EnemyBullet(Sprite):
    """Represent an enemy projectile aimed at the player's ship."""

    def __init__(
        self,
        game: "AlienInvasion",
        alien: "Alien",
    ) -> None:
        """Initialize a projectile aimed at the player's position."""
        super().__init__()

        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        original_image = pygame.image.load(
            self.settings.enemy_bullet_file
        ).convert_alpha()

        original_image = pygame.transform.scale(
            original_image,
            (
                self.settings.enemy_bullet_w,
                self.settings.enemy_bullet_h,
            ),
        )

        # Calculate the direction from the alien to the ship.
        start_x = float(alien.rect.centerx)
        start_y = float(alien.rect.bottom)

        target_x = float(game.ship.rect.centerx)
        target_y = float(game.ship.rect.centery)

        difference_x = target_x - start_x
        difference_y = target_y - start_y

        distance = math.hypot(difference_x, difference_y)

        if distance == 0:
            self.velocity_x = 0.0
            self.velocity_y = self.settings.enemy_bullet_speed
        else:
            self.velocity_x = (
                difference_x / distance
                * self.settings.enemy_bullet_speed
            )
            self.velocity_y = (
                difference_y / distance
                * self.settings.enemy_bullet_speed
            )

        # Rotate the projectile to follow its travel direction.
        angle = -math.degrees(
            math.atan2(self.velocity_x, self.velocity_y)
        )

        self.image = pygame.transform.rotate(
            original_image,
            angle,
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = alien.rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the projectile toward the player's ship."""
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def is_off_screen(self) -> bool:
        """Return True when the projectile leaves the screen."""
        screen_rect = self.screen.get_rect()

        return (
            self.rect.bottom < screen_rect.top
            or self.rect.top > screen_rect.bottom
            or self.rect.right < screen_rect.left
            or self.rect.left > screen_rect.right
        )

    def draw_bullet(self) -> None:
        """Draw the enemy projectile."""
        self.screen.blit(self.image, self.rect)
