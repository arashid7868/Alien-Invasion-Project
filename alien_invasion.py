
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Demonstrate player controls and targeted enemy return fire.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 12, 2026
"""

import sys

import pygame

from arsenal import Arsenal
from enemy_arsenal import EnemyArsenal
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage the Milestone 1 game prototype."""

    def __init__(self) -> None:
        """Initialize the game and create its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(
            "Alien Invasion - Track 1: Mechanics - M1"
        )

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
        self.ships_left = self.settings.ship_limit

        pygame.mixer.init()

        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(
            self.settings.impact_sound
        )
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        self.enemy_arsenal = EnemyArsenal(self)

        print("Milestone 1 prototype started.")
        print(f"Player lives: {self.ships_left}")

    def run_game(self) -> None:
        """Run the Milestone 1 game loop."""
        while self.running:
            self._check_events()

            if not self.running:
                break

            self.ship.update()
            self.ship.arsenal.update_arsenal()
            self.enemy_arsenal.update()

            self._check_enemy_bullet_collision()

            if self.running:
                self._update_screen()

            self.clock.tick(self.settings.fps)

        pygame.quit()

    def _check_enemy_bullet_collision(self) -> None:
        """Respond when an enemy projectile hits the player."""
        if pygame.sprite.spritecollideany(
            self.ship,
            self.enemy_arsenal.projectiles,
        ):
            self._ship_hit()

    def _ship_hit(self) -> None:
        """Reduce player lives and respond to an enemy projectile hit."""
        self.impact_sound.play()
        self.ships_left -= 1

        print(f"Enemy projectile hit! Lives remaining: {self.ships_left}")

        self.ship.arsenal.arsenal.empty()
        self.enemy_arsenal.empty()
        self.ship.center_ship()
        self.space_pressed = False

        if self.ships_left <= 0:
            print("Game over!")
            self.running = False
            return

        pygame.time.delay(500)

    def _update_screen(self) -> None:
        """Draw the background, projectiles, and player."""
        self.screen.blit(self.bg, (0, 0))

        self.ship.arsenal.draw()
        self.enemy_arsenal.draw()
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
        """Respond to keyboard presses."""
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
        """Respond when keyboard keys are released."""
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
    game = AlienInvasion()
    game.run_game()
