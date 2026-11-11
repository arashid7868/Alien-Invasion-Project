
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Run the space shooter game and manage player and enemy attacks.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 11, 2026
"""

import sys

import pygame

from alien_fleet import AlienFleet
from arsenal import Arsenal
from button import Button
from enemy_arsenal import EnemyArsenal
from game_stats import GameStats
from hud import HUD
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

        # Initialize sounds.
        pygame.mixer.init()

        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(
            self.settings.impact_sound
        )
        self.impact_sound.set_volume(0.7)

        # Create game objects.
        self.game_stats = GameStats(self)
        self.ship = Ship(self, Arsenal(self))
        self.fleet = AlienFleet(self)
        self.enemy_arsenal = EnemyArsenal(self)

        # Create interface components.
        self.play_button = Button(self)
        self.hud = HUD(self)

    def run_game(self) -> None:
        """Run the main game loop."""
        while self.running:
            self._check_events()

            if self.game_stats.game_active:
                self.ship.update()
                self.ship.arsenal.update_arsenal()

                if self.fleet.check_edges():
                    self.fleet.change_direction()

                self.fleet.update()

                # Update enemy attacks.
                self.enemy_arsenal.update()

                self._check_ship_alien_collision()
                self._check_enemy_bullet_collision()
                self._check_bullet_alien_collisions()

                if (
                    self.game_stats.game_active
                    and self.fleet.check_bottom()
                ):
                    self._ship_hit()

            self._update_screen()
            self.clock.tick(self.settings.fps)

        pygame.quit()

    def _start_game(self) -> None:
        """Start a new game or restart after game over."""
        if self.game_stats.game_active:
            return

        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()

        self.ship.center_ship()
        self.ship.arsenal.arsenal.empty()
        self.enemy_arsenal.empty()

        self.fleet.aliens.empty()
        self.fleet.create_fleet()

        self.space_pressed = False

        self.hud.update_scores()
        self.hud.update_level()

        self.game_stats.game_active = True
        pygame.mouse.set_visible(False)

    def _ship_hit(self) -> None:
        """Respond to a collision between the ship and an alien or projectile."""
        if not self.game_stats.game_active:
            return

        self.impact_sound.play()

        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1

            self.ship.arsenal.arsenal.empty()
            self.enemy_arsenal.empty()
            self.fleet.aliens.empty()

            self.ship.center_ship()
            self.fleet.create_fleet()

            self.space_pressed = False

            self.hud.update_scores()

            pygame.time.delay(500)

        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
            print("Game over!")

    def _check_ship_alien_collision(self) -> None:
        """Check whether an alien has collided with the ship."""
        if pygame.sprite.spritecollideany(
            self.ship,
            self.fleet.aliens,
        ):
            self._ship_hit()

    def _check_enemy_bullet_collision(self) -> None:
        """Check whether an enemy projectile has hit the ship."""
        if pygame.sprite.spritecollideany(
            self.ship,
            self.enemy_arsenal.projectiles,
        ):
            self._ship_hit()

    def _check_bullet_alien_collisions(self) -> None:
        """Check projectile collisions and update the score."""
        collisions = pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.fleet.aliens,
            True,
            True,
        )

        if collisions:
            aliens_destroyed = sum(
                len(aliens)
                for aliens in collisions.values()
            )

            self.game_stats.score += (
                self.settings.alien_points * aliens_destroyed
            )

            self.game_stats.check_high_score()
            self.hud.update_scores()

        if not self.fleet.aliens and self.game_stats.game_active:
            self.ship.arsenal.arsenal.empty()
            self.enemy_arsenal.empty()

            self.game_stats.level += 1
            self.settings.increase_speed()

            self.fleet.create_fleet()

            self.hud.update_scores()
            self.hud.update_level()

    def _update_screen(self) -> None:
        """Draw the current game screen."""
        self.screen.blit(self.bg, (0, 0))

        if self.game_stats.game_active:
            self.ship.arsenal.draw()
            self.enemy_arsenal.draw()
            self.fleet.draw()
            self.ship.draw()
            self.hud.draw()

        else:
            self.play_button.draw_button()

        pygame.display.flip()

    def _check_events(self) -> None:
        """Respond to keyboard, mouse, and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if (
                    self.play_button.rect.collidepoint(mouse_position)
                    and not self.game_stats.game_active
                ):
                    self._start_game()

    def _check_keydown_events(
        self,
        event: pygame.event.Event,
    ) -> None:
        """Respond to keyboard presses."""
        if event.key == pygame.K_q:
            self._quit_game()

        if not self.game_stats.game_active:
            if event.key in (pygame.K_RETURN, pygame.K_p):
                self._start_game()
            return

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            if not self.space_pressed:
                self.space_pressed = True

                if self.ship.fire():
                    self.laser_sound.play()

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
