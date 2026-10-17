
# Alien Invasion — Part 1

## Project Overview

This project follows the instructor's Alien Invasion tutorial using Python and Pygame. Part 1 focuses on creating the game window, displaying the background and player ship, handling keyboard input, implementing ship movement, and firing laser projectiles with sound.

## Features

- Pygame game window and background image
- Player ship positioned at the bottom of the screen
- Left and right arrow-key movement
- Screen-boundary checks for the ship
- Laser projectile firing with the Space key
- Sound effect when firing lasers
- Main game loop with frame-rate control

## Requirements

- Python 3.12
- Pygame 2.6.1
- The supplied game assets in the `Assets/` directory

## Installation

Open a terminal in the project directory and install the dependencies:

```powershell
py -3.12 -m pip install -r requirements.txt
```

## Run the Game

Start the game with:

```powershell
py -3.12 alien_invasion.py
```

Use the left and right arrow keys to move the ship. Press Space to fire lasers. Close the game window to exit.

## Project Structure

```text
Alien-Invasion-Tutorial/
├── Assets/
├── alien_invasion.py
├── settings.py
├── ship.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Code Organization

- `alien_invasion.py` manages the game window, event handling, game loop, background, laser projectiles, and sound.
- `settings.py` stores the screen dimensions, frame rate, ship speed, and laser speed.
- `ship.py` defines the player ship, movement, boundary checks, and drawing.
- `Assets/` contains the images and sound files used by the game.
- `requirements.txt` specifies the Python dependency.
- `.gitignore` excludes local environment and generated Python files.

## Tutorial Scope

This repository documents the Part 1 implementation. Additional gameplay features should be added only as the corresponding tutorial sections are covered.
