
"""Manage the heads-up display for Alien Invasion."""

import pygame


class HUD:
    """Display lives, scores, and level information."""

    def __init__(self, game) -> None:
        """Initialize the HUD and its visual resources."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.game_stats = game.game_stats

        self.padding = self.settings.hud_padding

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.hud_font_size,
        )

        self.life_image = pygame.image.load(
            self.settings.ship_file
        ).convert_alpha()

        self.life_image = pygame.transform.scale(
            self.life_image,
            (
                self.settings.ship_w,
                self.settings.ship_h,
            ),
        )

        self.life_rect = self.life_image.get_rect()

        self.update_scores()
        self.update_level()

    def update_scores(self) -> None:
        """Prepare the current score and high-score displays."""

        # Current score: upper-right area.
        score_text = f"Score: {self.game_stats.score:,}"
        self.score_image = self.font.render(
            score_text,
            True,
            self.settings.text_color,
            None,
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.padding
        self.score_rect.right = self.screen_rect.right - self.padding

        # High score: centered at the top.
        hi_score_text = f"Hi-Score: {self.game_stats.hi_score:,}"
        self.hi_score_image = self.font.render(
            hi_score_text,
            True,
            self.settings.text_color,
            None,
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (
            self.screen_rect.centerx,
            self.padding,
        )

        # Maximum score: above the current score.
        max_score_text = (
            f"Max-Score: {self.game_stats.max_score:,}"
        )
        self.max_score_image = self.font.render(
            max_score_text,
            True,
            self.settings.text_color,
            None,
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.screen_rect.right - self.padding
        self.max_score_rect.top = (
            self.score_rect.bottom + 5
        )

    def update_level(self) -> None:
        """Prepare the current level display."""
        level_text = f"Level: {self.game_stats.level}"

        self.level_image = self.font.render(
            level_text,
            True,
            self.settings.text_color,
            None,
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.bottom = (
            self.screen_rect.bottom - self.padding
        )

    def _draw_lives(self) -> None:
        """Draw the remaining ship icons."""
        current_x = self.padding
        current_y = self.padding

        for _ in range(self.game_stats.ships_left):
            self.life_rect = self.life_image.get_rect()

            self.screen.blit(
                self.life_image,
                (current_x, current_y),
            )

            current_x += self.life_rect.width + 10

    def draw(self) -> None:
        """Draw all HUD elements on the game screen."""

        self.screen.blit(
            self.hi_score_image,
            self.hi_score_rect,
        )

        self.screen.blit(
            self.max_score_image,
            self.max_score_rect,
        )

        self.screen.blit(
            self.score_image,
            self.score_rect,
        )

        self.screen.blit(
            self.level_image,
            self.level_rect,
        )

        self._draw_lives()
