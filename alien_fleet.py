
"""Manage the alien fleet and its formation."""

import pygame

from alien import Alien


class AlienFleet:
    """Create, manage, and draw the alien fleet."""

    def __init__(self, game) -> None:
        """Initialize the fleet and create its aliens."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def calculate_fleet_size(
        self,
        alien_w: int,
        screen_w: int,
    ) -> int:
        """Calculate how many aliens fit across the screen."""
        if alien_w <= 0:
            return 0

        available_space_x = screen_w - (2 * alien_w)

        return max(
            0,
            available_space_x // (2 * alien_w),
        )

    def calculate_fleet_rows(
        self,
        alien_h: int,
        screen_h: int,
    ) -> int:
        """Calculate how many alien rows fit on the screen."""
        if alien_h <= 0:
            return 0

        ship_height = self.game.ship.rect.height

        available_space_y = (
            screen_h - (3 * alien_h) - ship_height
        )

        return max(
            0,
            available_space_y // (2 * alien_h),
        )

    def create_fleet(self) -> None:
        """Create the full fleet of aliens."""
        alien_width = self.settings.alien_w
        alien_height = self.settings.alien_h

        columns = self.calculate_fleet_size(
            alien_width,
            self.settings.screen_w,
        )

        rows = self.calculate_fleet_rows(
            alien_height,
            self.settings.screen_h,
        )

        for row_number in range(rows):
            for alien_number in range(columns):
                x = alien_width + (
                    2 * alien_width * alien_number
                )
                y = alien_height + (
                    2 * alien_height * row_number
                )

                alien = Alien(self, x, y)
                self.aliens.add(alien)

    def update(self) -> None:
        """Update the position of every alien."""
        self.aliens.update()

    def draw(self) -> None:
        """Draw every alien in the fleet."""
        for alien in self.aliens.sprites():
            alien.draw_alien()

    def check_edges(self) -> bool:
        """Return True if any alien has reached a screen edge."""
        return any(
            alien.check_edges()
            for alien in self.aliens.sprites()
        )

    def change_direction(self) -> None:
        """Reverse fleet movement and move every alien down."""
        self.settings.alien_direction *= -1

        for alien in self.aliens.sprites():
            alien.drop_down(
                self.settings.alien_drop_speed
            )

    def check_bottom(self) -> bool:
        """Check whether any alien has reached the screen bottom."""
        return any(
            alien.rect.bottom >= self.settings.screen_h
            for alien in self.aliens.sprites()
        )