
from pathlib import Path


class Settings:
    """Store configuration values for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name: str = "Alien Invasion"
        self.screen_w: int = 900
        self.screen_h: int = 600
        self.fps: int = 60

        # Background and ship assets
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        # Bullet assets and settings
        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        # Alien settings will be added in the relevant Part 2 tutorial.
