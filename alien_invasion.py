"""Run the Alien Invasion game using Pygame."""

import sys

import pygame

from alien_fleet import AlienFleet
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
        self.fleet = AlienFleet(self)

    def run_game(self) -> None:
        """Run the main game loop."""
        while self.running:
            self._check_events()

            if not self.running:
                break

            self.ship.update()
            self.ship.arsenal.update_arsenal()

            if self.fleet.check_edges():
                self.fleet.change_direction()

            self.fleet.update()

            self._check_bullet_alien_collisions()

            if self.fleet.check_bottom():
                self.running = False

            if self.running:
                self._update_screen()

            self.clock.tick(self.settings.fps)

        pygame.quit()

    def _check_bullet_alien_collisions(self) -> None:
        """Remove aliens hit by projectiles."""
        pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.fleet.aliens,
            True,
            True,
        )

        if not self.fleet.aliens:
            self.fleet.create_fleet()

    def _update_screen(self) -> None:
        """Draw the background, projectiles, aliens, and ship."""
        self.screen.blit(self.bg, (0, 0))

        self.ship.arsenal.draw()
        self.fleet.draw()
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
        self,
        event: pygame.event.Event,
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
        self,
        event: pygame.event.Event,
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