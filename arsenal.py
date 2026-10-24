
import pygame
from typing import TYPE_CHECKING

from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage the player's projectiles."""

    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Update projectiles and remove those off-screen."""
        self.arsenal.update()
        self.remove_bullets_offscreen()

    def draw(self) -> None:
        """Draw all projectiles."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire if the projectile limit has not been reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False

    def remove_bullets_offscreen(self) -> None:
        """Remove projectiles that have left the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
