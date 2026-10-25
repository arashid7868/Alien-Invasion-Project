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
        spacing = self.settings.alien_spacing_x
        usable_width = screen_w - (2 * spacing)

        if alien_w + spacing <= 0:
            return 0

        return max(
            0,
            (usable_width + spacing) // (alien_w + spacing),
        )

    def create_fleet(self) -> None:
        """Create a centered row of aliens."""
        alien_width = self.settings.alien_w
        screen_width = self.settings.screen_w
        spacing = self.settings.alien_spacing_x

        fleet_size = self.calculate_fleet_size(
            alien_width,
            screen_width,
        )

        if fleet_size == 0:
            return

        fleet_width = (
            fleet_size * alien_width
            + (fleet_size - 1) * spacing
        )
        x_offset = (screen_width - fleet_width) // 2
        y = self.settings.alien_top_margin

        for column in range(fleet_size):
            x = x_offset + column * (alien_width + spacing)
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
            alien.drop_down(self.settings.alien_drop_speed)

    def check_bottom(self) -> bool:
        """Check whether any alien has reached the screen bottom."""
        return any(
            alien.rect.bottom >= self.settings.screen_h
            for alien in self.aliens.sprites()
        )