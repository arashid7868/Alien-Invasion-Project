
# Alien Invasion — Part 2

## Project Overview

This project follows the instructor's Alien Invasion tutorial using Python and Pygame. Part 2 extends the existing game by adding an alien sprite, horizontal fleet movement, edge detection, downward fleet movement, bullet-alien collision detection, and a condition that stops gameplay when an alien reaches the bottom of the screen.

## Features

- Game window with a background image
- Player ship movement using the left and right arrow keys
- Laser firing using the Space key
- Laser firing sound effect
- A row of evenly spaced aliens
- Horizontal alien fleet movement
- Fleet direction reversal at screen edges
- Downward fleet movement when an edge is reached
- Bullet-alien collision detection
- Removal of bullets and aliens after a collision
- Game termination when an alien reaches the bottom of the screen
- Frame-rate control using Pygame

## Requirements

- Python 3.12
- Pygame 2.6.1
- Supplied images and sound files in the `Assets/` directory

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

## Controls

- **Left arrow:** Move the ship left.
- **Right arrow:** Move the ship right.
- **Space:** Fire a laser.
- **Q:** Quit the game.
- **Window close button:** Close the game.

## Project Structure

```text
alien_Invasion_starter/
├── Assets/
│   ├── images/
│   └── sound/
├── alien_invasion.py
├── alien.py
├── arsenal.py
├── bullet.py
├── ship.py
├── settings.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Code Organization

- `alien_invasion.py` initializes the game, manages the main loop, handles keyboard input, coordinates fleet movement, checks collisions, and updates the screen.
- `alien.py` defines the alien sprite, its image, horizontal movement, edge detection, downward movement, and row creation.
- `ship.py` manages the player's ship and its movement.
- `arsenal.py` manages laser projectiles, firing limits, projectile updates, and removal of off-screen projectiles.
- `bullet.py` defines the projectile behavior.
- `settings.py` stores screen dimensions, movement speeds, asset paths, fleet spacing, and other configuration values.
- `Assets/` contains the images and sounds used by the game.
- `requirements.txt` specifies the Python dependency.

## Testing

The following behaviors were tested during development:

- Aliens move horizontally together.
- The fleet reverses direction at the screen edges.
- The fleet moves downward when it reaches an edge.
- Bullets destroy aliens on collision.
- Gameplay stops when an alien reaches the bottom of the screen.

## Tutorial Scope

This repository builds on the Part 1 implementation and adds the alien fleet and collision behaviors covered in Part 2. Features such as scoring, levels, a play button, and a restart system are outside the current documented implementation.
