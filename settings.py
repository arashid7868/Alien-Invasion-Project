
"""Store settings for the Alien Invasion game."""


class Settings:
    """Store configuration values for the game."""

    def __init__(self):
        """Initialize the game settings."""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.frame_rate = 60
        self.ship_speed = 1.5
        self.laser_speed = 8
