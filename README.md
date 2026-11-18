# Alien Invasion — Track 1: Custom Game Mechanics

**Author:** Abdullah Rashid  
**Language:** Python 3.12  
**Game Framework:** Pygame 2.6.1  
**Development Environment:** Visual Studio Code  
**Submission Branch:** `track_1_mechanics`

---

## 1. Project Overview

Alien Invasion is a Python-based 2D space shooter developed using Pygame. The project extends the instructor-provided starter code with custom gameplay mechanics, including player movement, projectile firing, enemy attacks, alien fleet movement, collision detection, and game-state management.

The development is organized into milestones. Each milestone introduces and demonstrates additional gameplay functionality while maintaining a modular project structure.

## 2. Milestone 1 — Core Gameplay Mechanics

Milestone 1 established the initial gameplay prototype, focusing on player controls and targeted enemy return fire.

### Implemented Features

- Player spaceship movement using the left and right arrow keys.
- Player laser firing using the Space key.
- Configurable player projectile speed and projectile limits.
- Enemy projectiles aimed toward the player's current position.
- Configurable enemy firing intervals and projectile limits.
- Collision detection between enemy projectiles and the player.
- Player life reduction and collision response.
- Ship repositioning after being hit.
- Laser and impact sound effects.

### Milestone 1 Demonstration

**YouTube Unlisted Video:** [Insert the actual Milestone 1 video URL]

## 3. Milestone 2 — Alien Fleet and Collision Mechanics

Milestone 2 extends the prototype by integrating the alien fleet and additional gameplay interactions.

### Implemented Features

- Creation and management of multiple alien sprites.
- Alien fleet formation and coordinated movement.
- Horizontal alien movement across the game screen.
- Fleet direction reversal when aliens reach screen boundaries.
- Player projectile interaction with aliens.
- Alien-related collision and gameplay behavior.
- Integration of the alien fleet with the main game controller.
- Game statistics and player-life management.
- Continued support for player and enemy projectile mechanics.

### Main Components

| File | Responsibility |
|---|---|
| `alien.py` | Defines individual alien behavior and properties. |
| `alien_fleet.py` | Creates and manages the alien fleet and its movement. |
| `game_stats.py` | Manages game statistics and player lives. |
| `enemy_arsenal.py` | Controls enemy projectile creation and management. |
| `enemy_bullet.py` | Defines enemy projectile movement and behavior. |
| `alien_invasion.py` | Coordinates the main game loop, events, and gameplay systems. |
| `ship.py` | Manages player spaceship behavior and movement. |
| `arsenal.py` | Manages player projectile creation and updates. |
| `bullet.py` | Defines player projectile behavior. |
| `settings.py` | Stores gameplay, screen, asset, and difficulty settings. |

### Milestone 2 Demonstration

**YouTube Unlisted Video:** [Insert the actual Milestone 2 video URL]

## 4. Technologies and Dependencies

The project uses:

- Python 3.12
- Pygame 2.6.1
- Visual Studio Code
- Git
- GitHub

The required Python dependency is listed in `requirements.txt`.

## 5. Project Structure

```text
Alien-Invasion-Project/
│
├── Assets/
│   ├── Fonts/
│   ├── file/
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
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 6. Installation and Setup

### Prerequisites

Install the following software:

1. Python 3.12
2. Git for Windows
3. Visual Studio Code
4. Microsoft Python extension for Visual Studio Code

### Clone the Repository

Open PowerShell or the VS Code terminal and run:

```powershell
git clone https://github.com/arashid7868/Alien-Invasion-Project.git
```

Navigate into the project directory:

```powershell
cd Alien-Invasion-Project
```

Switch to the project development branch:

```powershell
git checkout track_1_mechanics
```

### Create a Virtual Environment

```powershell
py -3.12 -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the project requirements:

```powershell
python -m pip install -r requirements.txt
```

Verify the Pygame installation:

```powershell
python -c "import pygame; print(pygame.version.ver)"
```

## 7. Running the Game

Make sure the virtual environment is activated and the terminal is located in the project root directory.

Run:

```powershell
python alien_invasion.py
```

The Pygame window should open and display the game.

## 8. Game Controls

| Key | Action |
|---|---|
| Left Arrow | Move the player's spaceship left |
| Right Arrow | Move the player's spaceship right |
| Spacebar | Fire player projectiles |
| Q | Quit the game |

## 9. Configuration

Gameplay settings are maintained in `settings.py`.

These include:

- Screen width and height.
- Frames per second.
- Player movement speed.
- Player projectile speed and limits.
- Enemy projectile speed and limits.
- Enemy firing intervals.
- Alien dimensions and movement speed.
- Fleet spacing and formation settings.
- Player lives and difficulty settings.
- Asset file paths.

This configuration-based approach makes it easier to adjust gameplay without changing the core logic of every class.

## 10. Version Control and Development

The project uses Git for source-code management and GitHub for remote repository hosting.

Development and milestone submissions are maintained on:

```text
track_1_mechanics
```

Meaningful commits are used to document implementation, corrections, integration, and milestone progress.

**Submission Repository:**

https://github.com/arashid7868/Alien-Invasion-Project

**Development Branch:**

https://github.com/arashid7868/Alien-Invasion-Project/tree/track_1_mechanics

## 11. Development Roadmap

| Stage | Development Focus |
|---|---|
| Milestone 1 | Player movement, projectile firing, and targeted enemy return fire. |
| Milestone 2 | Alien fleet integration, fleet movement, and collision mechanics. |
| Final Submission | Complete the remaining required gameplay, interface, scoring, and game-state functionality. |

## 12. Author and Source

**Author:** Abdullah Rashid

**Instructor Starter Repository:**

https://github.com/RedBeard41/alien_Invasion_starter

**Submission Repository:**

https://github.com/arashid7868/Alien-Invasion-Project

---

*This project is developed as part of the Python Pygame Alien Invasion course assignment.*