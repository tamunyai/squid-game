# JBS Programming Bootcamp: Squid Game Assessment

This project simulates the "Red Light, Green Light" game from the popular TV series Squid Game. The game is played with multiple players who move during the "Green Light" and are eliminated if they move during the "Red Light."

## Table of Contents

- Overview
- Classes
  - Player
  - SquidGame
- How It Works
- Running the Game
- Customization
- License

## Overview

This program implements the simulation of the "Red Light, Green Light" game, where a group of players must move during "Green Light" and stop moving during "Red Light." Players who move during "Red Light" are eliminated from the game. The game continues for a set duration or until all players are eliminated.

### Key Features

- Players are randomly selected to move during each "Green Light" interval.
- Players are eliminated if they move during "Red Light."
- The game alternates between "Green Light" and "Red Light" until the specified game duration ends.
- The game tracks the movement of players and their eliminations.
- Remaining players are printed after the game ends, showing their final positions.

## Classes

### Player

The `Player` class represents an individual player in the game. Each player has:

- **id**: A unique identifier for the player (e.g., "001", "002").
- **position**: The player's current position in the game (starts at 0).
- **eliminated**: A boolean indicating whether the player has been eliminated from the game (starts as False).

Methods:

- `move()`: Increments the player's position by 1 if not eliminated.
- `eliminate()`: Marks the player as eliminated when they move during "Red Light."

### SquidGame

The `SquidGame` class simulates the overall game. It manages a group of players and controls the flow of the game.

Methods:

- `__init__(self, total_players: int = 456)`: Initializes the game with a given number of players (default 456).
- `_create_players(self, total_players: int)`: Creates a list of Player objects.
- `start(self, light_interval: int = 5, game_duration: int = 30)`: Simulates the "Red Light, Green Light" game.
- `reset()`: Resets the game to its initial state, with all players starting at position 0 and marked as not eliminated.
- `_print_players(self, label: str, players: list[Player])`: Helper function to print the players who moved or stayed still.
- `_print_eliminated(self, moving_players: list[Player], current_light: str)`: Helper function to print eliminated players.

## How It Works

1. The game starts with a specified number of players (456 by default).
2. The game alternates between "Green Light" and "Red Light."
3. During "Green Light," a random percentage of players move.
4. During "Red Light," players who move are eliminated.
5. The game continues for a given duration, or until all players are eliminated.
6. The remaining players are printed, showing their ID and position.

### Running the Game

1. Clone this repository or download the script.
2. Ensure Python 3.x is installed on your system.
3. Run the script:

```bash
python squid_game.py
```

### Example Output

```bash
Round 1: Green Light
Moved: 001, 002, 003, 004, 005
Static: 006, 007, 008, 009, 010
Eliminated: None.

Round 2: Red Light
Moved: 001, 002, 003, 004, 005
Static: 006, 007, 008, 009, 010
Eliminated: 001, 002, 003, 004, 005.

...
```

## Customization

You can customize the game by modifying the following parameters in the `start()` method:

- `light_interval`: The interval (in seconds) between light changes.
- `game_duration`: The total duration (in seconds) of the game.

### Example Customization

```python
game = SquidGame(total_players=100)
remaining_players = game.start(light_interval=3, game_duration=60)
```

This example will create a game with 100 players, with a light interval of 3 seconds and a game duration of 60 seconds.

## License

This project is licensed under the MIT License. See the [LICENSE](license) file for more details.
