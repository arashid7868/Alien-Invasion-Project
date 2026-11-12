
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Configure player, enemy, projectile, asset, and gameplay settings.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 12, 2026
"""

from pathlib import Path


class Settings:
    """Store the game's static and dynamic configuration."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen settings
        self.name = "Alien Invasion - Track 1: Mechanics"
        self.screen_w = 1200
        self.screen_h = 800
        self.fps = 60

        # Asset paths
        self.bg_file = (
            Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        )
        self.ship_file = (
            Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        )
        self.alien_file = (
            Path.cwd() / "Assets" / "images" / "enemy_4.png"
        )
        self.bullet_file = (
            Path.cwd() / "Assets" / "images" / "laserBlast.png"
        )
        self.enemy_bullet_file = (
            Path.cwd() / "Assets" / "images" / "beams.png"
        )
        self.laser_sound = (
            Path.cwd() / "Assets" / "sound" / "laser.mp3"
        )
        self.impact_sound = (
            Path.cwd() / "Assets" / "sound" / "impactSound.mp3"
        )
        self.font_file = (
            Path.cwd()
            / "Assets"
            / "Fonts"
            / "Silkscreen"
            / "Silkscreen-Regular.ttf"
        )

        # Persistent score storage
        self.scores_file = (
            Path.cwd() / "Assets" / "file" / "scores.json"
        )

        # Ship settings
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.ship_limit = 3

        # Player projectile settings
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        # Enemy projectile settings
        self.enemy_bullet_speed = 4
        self.enemy_bullet_w = 20
        self.enemy_bullet_h = 40
        self.enemy_bullet_amount = 8
        self.base_enemy_fire_interval = 1500
        self.minimum_enemy_fire_interval = 350

        # Alien fleet settings
        self.alien_w = 80
        self.alien_h = 80
        self.alien_speed = 5
        self.alien_approach_speed = 0.5
        self.alien_drop_speed = 40
        self.alien_direction = 1
        self.alien_spacing_x = 80
        self.alien_top_margin = 80

        # Enemy formation settings
        self.enemy_group_size = 5

        # Scoring settings
        self.alien_points = 50
        self.score_scale = 1.5

        # Difficulty settings
        self.speedup_scale = 1.1

        # HUD settings
        self.hud_font_size = 24
        self.text_color = (0, 255, 80)
        self.hud_padding = 20

        # Button settings
        self.button_w = 200
        self.button_h = 60
        self.button_color = (0, 255, 80)
        self.button_text_color = (0, 0, 0)
        self.button_font_size = 32

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Reset settings that change as gameplay progresses."""
        self.ship_speed = 5
        self.bullet_speed = 7
        self.enemy_bullet_speed = 4
        self.enemy_fire_interval = self.base_enemy_fire_interval
        self.alien_speed = 5
        self.alien_approach_speed = 0.5
        self.alien_direction = 1
        self.alien_points = 50

    def increase_speed(self) -> None:
        """Increase difficulty and scoring as levels progress."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_approach_speed *= self.speedup_scale

        self.enemy_fire_interval = max(
            self.minimum_enemy_fire_interval,
            int(
                self.enemy_fire_interval
                / self.speedup_scale
            ),
        )

        self.alien_points = int(
            self.alien_points * self.score_scale
        )
