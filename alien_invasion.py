
"""Run the Alien Invasion game using Pygame."""

import sys

import pygame

from alien import Alien
from arsenal import Arsenal
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage the game resources and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(
            self.settings.bg_file
        ).convert()
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h),
        )

        self.running = True
        self.clock = pygame.time.Clock()
        self.space_pressed = False

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))

        # Create the initial row of aliens.
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self) -> None:
        """Create a row of aliens."""
        Alien.create_aliens_row(
            self,
            self.aliens,
            y=self.settings.alien_top_margin,
        )

    def run_game(self) -> None:
        """Run the main game loop."""
        while self.running:
            self._check_events()

            if not self.running:
                break

            self.ship.update()
            self.ship.arsenal.update_arsenal()

            self._check_fleet_edges()
            self.aliens.update()

            self._check_bullet_alien_collisions()
            self._check_aliens_bottom()

            if self.running:
                self._update_screen()

            self.clock.tick(self.settings.fps)

        pygame.quit()

    def _check_fleet_edges(self) -> None:
        """Reverse and lower the fleet when an alien reaches an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Move the fleet down and reverse its horizontal direction."""
        self.settings.alien_direction *= -1

        for alien in self.aliens.sprites():
            alien.drop_down(self.settings.alien_drop_speed)

    def _check_aliens_bottom(self) -> None:
        """Stop gameplay if an alien reaches the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_h:
                self.running = False
                break

    def _check_bullet_alien_collisions(self) -> None:
        """Remove hit aliens and recreate the fleet when it is empty."""
        pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.aliens,
            True,
            True,
        )

        if not self.aliens:
            self._create_fleet()

    def _update_screen(self) -> None:
        """Draw the background, bullets, aliens, and ship."""
        self.screen.blit(self.bg, (0, 0))

        self.ship.arsenal.draw()

        for alien in self.aliens.sprites():
            alien.draw_alien()

        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(
        self, event: pygame.event.Event
    ) -> None:
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            if not self.space_pressed:
                self.space_pressed = True

                if self.ship.fire():
                    self.laser_sound.play()

        elif event.key == pygame.K_q:
            self._quit_game()

    def _check_keyup_events(
        self, event: pygame.event.Event
    ) -> None:
        """Respond when keys are released."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_SPACE:
            self.space_pressed = False

    @staticmethod
    def _quit_game() -> None:
        """Shut down Pygame and exit."""
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
