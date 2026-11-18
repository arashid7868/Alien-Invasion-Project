
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Run the M2 alien fleet, return-fire, and collision prototype.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 18, 2026
"""

import sys

import pygame

from alien_fleet import AlienFleet
from arsenal import Arsenal
from enemy_arsenal import EnemyArsenal
from game_stats import GameStats
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage the Milestone 2 alien fleet game."""

    def __init__(self) -> None:
        """Initialize Pygame and create the game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )

        pygame.display.set_caption(
            "Alien Invasion - Track 1: Mechanics - M2"
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

        pygame.mixer.init()

        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(
            self.settings.impact_sound
        )
        self.impact_sound.set_volume(0.7)

        self.stats = GameStats(self)

        self.ship = Ship(self, Arsenal(self))

        self.alien_fleet = AlienFleet(self)

        self.enemy_arsenal = EnemyArsenal(
            self,
            self.alien_fleet,
        )

        print("Milestone 2 prototype started.")
        print(f"Player lives: {self.stats.ships_left}")
        print(f"Aliens in fleet: {len(self.alien_fleet.aliens)}")

    def run_game(self) -> None:
        """Run the main Milestone 2 game loop."""
        while self.running:
            self._check_events()

            if not self.running:
                break

            self.ship.update()
            self.ship.arsenal.update_arsenal()
            self.alien_fleet.update()
            self.enemy_arsenal.update()

            self._check_collisions()

            if self.running:
                self._update_screen()

            self.clock.tick(self.settings.fps)

        pygame.quit()

    def _check_collisions(self) -> None:
        """Check player attacks, enemy attacks, and invasion conditions."""
        self._check_player_bullet_collisions()

        if not self.running:
            return

        if pygame.sprite.spritecollideany(
            self.ship,
            self.enemy_arsenal.projectiles,
        ):
            self._ship_hit()
            return

        if pygame.sprite.spritecollideany(
            self.ship,
            self.alien_fleet.aliens,
        ):
            self._ship_hit()
            return

        if self.alien_fleet.check_bottom():
            self._ship_hit()

    def _check_player_bullet_collisions(self) -> None:
        """Remove aliens and player bullets when they collide."""
        pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.alien_fleet.aliens,
            True,
            True,
        )

        if not self.alien_fleet.aliens:
            print("Fleet destroyed! A new fleet is approaching.")
            self._reset_fleet()

    def _ship_hit(self) -> None:
        """Handle a collision that costs the player one life."""
        self.impact_sound.play()

        has_lives = self.stats.lose_ship()

        print(
            f"Player hit! Lives remaining: "
            f"{self.stats.ships_left}"
        )

        self.ship.arsenal.arsenal.empty()
        self.enemy_arsenal.empty()
        self.ship.center_ship()
        self.space_pressed = False

        if not has_lives:
            print("Game over! No lives remaining.")
            self.running = False
            return

        self._reset_fleet()

        pygame.time.delay(500)

    def _reset_fleet(self) -> None:
        """Create a fresh fleet and reset its movement direction."""
        self.settings.alien_direction = 1
        self.alien_fleet.create_fleet()
        self.enemy_arsenal.empty()

    def _update_screen(self) -> None:
        """Draw the background, fleet, projectiles, and player."""
        self.screen.blit(self.bg, (0, 0))

        self.alien_fleet.draw()
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
        """Respond when the player releases a key."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_SPACE:
            self.space_pressed = False

    @staticmethod
    def _quit_game() -> None:
        """Close Pygame and exit the application."""
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
