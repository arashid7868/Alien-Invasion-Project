# Alien Invasion — Track 1: Custom Game Mechanics

## Project Overview

Alien Invasion is a Python-based space shooter game developed using Pygame. This version extends the original starter project with custom enemy movement, enemy formations, targeted enemy projectiles, player lives, scoring, and progressive difficulty.

The player controls a spaceship, fires laser projectiles at approaching enemies, avoids incoming enemy attacks, and attempts to survive increasingly challenging levels.

## Features

- Player spaceship movement using the left and right arrow keys.
- Player laser firing using the Space key.
- Five-enemy V-shaped formation.
- Continuous downward enemy advancement.
- Horizontal enemy movement with automatic direction reversal at screen edges.
- Enemy projectiles aimed toward the player's spaceship.
- Configurable enemy firing intervals and projectile limits.
- Collision detection between player projectiles and enemies.
- Collision detection between enemy projectiles and the player.
- Ship lives and collision response.
- Scoring system with persistent high-score storage using JSON.
- Multiple levels with progressively increasing difficulty.
- Heads-up display showing score, high score, maximum score, and level.
- Play button and restart functionality.
- Laser and impact sound effects.

## Technologies and Requirements

- Python 3.12
- Pygame 2.6.1
- Visual Studio Code (recommended)
- Git and GitHub
- Supplied game assets in the `Assets` directory

## Project Structure

```text
alien_Invasion_starter/
│
├── Assets/
│   ├── file/
│   │   └── scores.json
│   ├── images/
│   └── sound/
│
├── alien.py
├── alien_fleet.py
├── alien_invasion.py
├── arsenal.py
├── bullet.py
├── button.py
├── enemy_arsenal.py
├── enemy_bullet.py
├── game_stats.py
├── hud.py
├── settings.py
├── ship.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Install Python 3.12.
2. Clone the repository:

```powershell
git clone https://github.com/arashid7868/Alien-Invasion-Project.git
```

3. Navigate into the project directory:

```powershell
cd Alien-Invasion-Project
```

4. Install the required dependency:

```powershell
py -3.12 -m pip install -r requirements.txt
```

## Running the Game

Launch the game using:

```powershell
py -3.12 alien_invasion.py
```

## Game Controls

| Key | Action |
|---|---|
| Left Arrow | Move spaceship left |
| Right Arrow | Move spaceship right |
| Spacebar | Fire laser |
| Enter / P | Start or restart the game |
| Mouse Click | Activate the Play button |
| Q | Quit the game |

## Gameplay

The player must destroy incoming enemies while avoiding their targeted projectiles. Enemies continuously advance toward the player's area while moving horizontally and reversing direction when they reach the screen boundaries.

Destroying all enemies advances the game to the next level. Each new level increases gameplay difficulty, including enemy movement speed, enemy projectile speed, and firing frequency.

The player has a limited number of lives. Collisions reduce the remaining lives, and losing all available lives ends the current game. The player can then restart using the Play button or the keyboard controls.

## Version Control

The project uses Git for version control and GitHub for source-code management. Changes are organized into meaningful commits to document development progress.

## Author

**Abdullah Rashid**

## Starter Code

https://github.com/RedBeard41/alien_Invasion_starter

## Submission Repository

https://github.com/arashid7868/Alien-Invasion-Project