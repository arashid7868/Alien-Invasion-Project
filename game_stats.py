
"""
Program Name: Alien Invasion - Track 1: Custom Game Mechanics
Author: Abdullah Rashid
Purpose: Track player lives and the active state during gameplay.
Starter Code: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 18, 2026
"""


class GameStats:
    """Track the gameplay state and remaining player lives."""

    def __init__(self, game) -> None:
        """Initialize game statistics using the game settings."""
        self.game = game
        self.settings = game.settings

        self.game_active = True

        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset the player's remaining lives."""
        self.ships_left = self.settings.ship_limit

    def lose_ship(self) -> bool:
        """Remove one life and return whether the player has lives left."""
        if self.ships_left > 0:
            self.ships_left -= 1

        if self.ships_left <= 0:
            self.game_active = False
            return False

        return True
