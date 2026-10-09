import sys
import pygame


class AlienInvasion:
    """Manage the game window and its main loop."""

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")

        self.background = pygame.image.load(
            "Assets/images/Starbasesnow.png"
        )
        self.background = pygame.transform.scale(
            self.background, (800, 600)
        )

        self.ship = pygame.image.load("Assets/images/ship.png")
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.midbottom = self.screen.get_rect().midbottom

        self.laser_image = pygame.image.load(
            "Assets/images/laserBlast.png"
        )
        self.lasers = []

        self.laser_sound = pygame.mixer.Sound("Assets/sound/laser.mp3")

        self.clock = pygame.time.Clock()
        self.ship_speed = 5
        self.laser_speed = 8

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()
            self._move_ship()
            self._update_lasers()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.moving_left = True
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.moving_right = True
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.moving_up = True
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_laser()

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.moving_left = False
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.moving_right = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.moving_up = False
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.moving_down = False

    def _fire_laser(self):
        """Fire a laser from the ship."""
        laser_rect = self.laser_image.get_rect()
        laser_rect.midbottom = self.ship_rect.midtop
        self.lasers.append(laser_rect)
        self.laser_sound.play()

    def _move_ship(self):
        """Move the ship while keeping it inside the window."""
        if self.moving_left:
            self.ship_rect.x -= self.ship_speed
        if self.moving_right:
            self.ship_rect.x += self.ship_speed
        if self.moving_up:
            self.ship_rect.y -= self.ship_speed
        if self.moving_down:
            self.ship_rect.y += self.ship_speed

        self.ship_rect.clamp_ip(self.screen.get_rect())

    def _update_lasers(self):
        """Move lasers upward and remove off-screen lasers."""
        for laser in self.lasers[:]:
            laser.y -= self.laser_speed
            if laser.bottom < 0:
                self.lasers.remove(laser)

    def _update_screen(self):
        """Draw the background, ship, and lasers."""
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ship, self.ship_rect)

        for laser in self.lasers:
            self.screen.blit(self.laser_image, laser)

        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()