
"""Create and manage the Play button."""

import pygame


class Button:
    """Represent the Play button in Alien Invasion."""

    def __init__(self, game, message: str = "Play") -> None:
        """Initialize the button's properties."""
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        # Create the button rectangle.
        self.rect = pygame.Rect(
            0,
            0,
            self.settings.button_w,
            self.settings.button_h,
        )
        self.rect.center = self.screen.get_rect().center

        # Prepare the button's appearance.
        self.button_color = self.settings.button_color

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.button_font_size,
        )

        self._prep_message(message)

    def _prep_message(self, message: str) -> None:
        """Render the button's text and center it."""
        self.message_image = self.font.render(
            message,
            True,
            self.settings.button_text_color,
        )

        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Draw the button and its message."""
        self.screen.fill(
            self.button_color,
            self.rect,
        )

        self.screen.blit(
            self.message_image,
            self.message_rect,
        )
