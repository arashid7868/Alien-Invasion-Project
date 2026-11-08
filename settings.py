
"""Store configuration values for Alien Invasion."""

from pathlib import Path


class Settings:
    """Store the game's static and dynamic configuration."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen settings
        self.name = "Alien Invasion"
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

        # Projectile settings
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        # Alien fleet settings
        self.alien_w = 80
        self.alien_h = 80
        self.alien_speed = 5
        self.alien_drop_speed = 40
        self.alien_direction = 1
        self.alien_spacing_x = 80
        self.alien_top_margin = 80

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

        # Initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change as the game progresses."""
        self.ship_speed = 5
        self.bullet_speed = 7
        self.alien_speed = 5
        self.alien_direction = 1
        self.alien_points = 50

    def increase_speed(self) -> None:
        """Increase game speed and scoring as difficulty rises."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(
            self.alien_points * self.score_scale
        )
