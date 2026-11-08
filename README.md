# Alien Invasion — Part 2

## Project Overview

This project extends the Alien Invasion game developed in Part 1 using Python and Pygame. Part 2 introduces alien fleet management, horizontal movement, edge detection, downward movement, projectile collisions, ship collision handling, and gameplay management.

The project also includes a scoring system, persistent high scores, multiple levels, a heads-up display, and a Play button with restart functionality.

## Features

- Pygame game window with a background image.
- Player ship movement using the left and right arrow keys.
- Laser firing using the Space key.
- Laser and impact sound effects.
- Alien fleet creation with multiple rows and columns.
- Horizontal fleet movement and edge detection.
- Automatic fleet direction reversal and downward movement.
- Projectile-alien collision detection.
- Ship-alien collision detection.
- Ship lives and collision response.
- Game-over handling and restart functionality.
- Play button and game-state management.
- Current score, high score, maximum score, and level display.
- Persistent high-score storage using JSON.
- Increasing difficulty and scoring as levels progress.

## Requirements

- Python 3.12
- Pygame 2.6.1
- Supplied assets in the Assets directory.

## Installation

Install the required dependency:

```powershell
py -3.12 -m pip install -r requirements.txt