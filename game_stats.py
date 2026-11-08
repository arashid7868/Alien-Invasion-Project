
"""Track game statistics and manage persistent high scores."""

import json

from settings import Settings


class GameStats:
    """Track the statistics and state of Alien Invasion."""

    def __init__(self, game) -> None:
        """Initialize the game's statistics."""
        self.game = game
        self.settings: Settings = game.settings

        self.game_active = False

        self._load_scores()
        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset statistics that change during a new game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.max_score = 0

    def _load_scores(self) -> None:
        """Load the saved high score from the JSON file."""
        self.settings.scores_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        try:
            with self.settings.scores_file.open(
                "r",
                encoding="utf-8",
            ) as score_file:
                scores = json.load(score_file)

            self.hi_score = int(scores.get("hi_score", 0))

        except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError):
            self.hi_score = 0

    def save_scores(self) -> None:
        """Save the high score to the JSON file."""
        self.settings.scores_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        scores = {
            "hi_score": self.hi_score,
        }

        with self.settings.scores_file.open(
            "w",
            encoding="utf-8",
        ) as score_file:
            json.dump(scores, score_file, indent=4)

    def check_high_score(self) -> None:
        """Update and save the high score when necessary."""
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()

        if self.score > self.max_score:
            self.max_score = self.score
