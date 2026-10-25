
"""Store configuration values for Alien Invasion."""

from pathlib import Path


class Settings:
    """Store configuration values for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.fps: int = 60

        # Ship settings
        self.bg_file = (
            Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        )
        self.ship_file = (
            Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        )
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.ship_limit = 3

        # Projectile settings
        self.bullet_file = (
            Path.cwd() / "Assets" / "images" / "laserBlast.png"
        )
        self.laser_sound = (
            Path.cwd() / "Assets" / "sound" / "laser.mp3"
        )
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        # Alien fleet settings
        self.alien_file = (
            Path.cwd() / "Assets" / "images" / "enemy_4.png"
        )
        self.alien_w = 80
        self.alien_h = 80
        self.alien_speed = 5
        self.alien_drop_speed = 40
        self.alien_direction = 1
        self.alien_spacing_x = 80
        self.alien_top_margin = 80