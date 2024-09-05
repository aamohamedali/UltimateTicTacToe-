# Tic-Tac-Toe Game App Logic Documentation

## Overview
This document outlines the logic behind a Tic-Tac-Toe game application. The application is designed using Python and employs object-oriented programming principles. It includes a `Game` class responsible for managing the game state and logic, as well as additional functions for managing game instances.

[UML diagram](Diagram 2024-02-17 09-36-57.png)
## Game Class
The `Game` class encapsulates the core logic of the Tic-Tac-Toe game. It maintains the game state, validates moves, checks for winning conditions, and determines the winner.

### Attributes
- `state`: A 2D list representing the game board. Each element represents a cell on the board, initialized to 'E' (Empty).
- `ustate`: A list representing the state of each subgrid. Each element can be 'NC' (Not Claimed), 'X', or 'O'.
- `next_subgrid`: Index of the next subgrid where the player can make a move.
- `next_player`: The player ('x' or 'o') who has the next turn.
- `outcome`: Indicates the outcome of the game (0 for pending, 1 for a win).

### Methods

#### `__init__(self)`
-  Initializes the game with an empty board, unclaimed subgrids, and sets the starting player and outcome.

### `getGameState(self)`
-  Retrieves the current state of the game, including the matrix and the list of subgrid statuses.

### `setGameState(self, matrix, list)`
-  Sets the state of the game with a new matrix and list of subgrid statuses.
   
   

#### `next_move(self, index1, index2, user)`
-  Implements the next move, validates it, updates the board, and checks for winning conditions.
- Parameters:
  - `index1`: Index of the subgrid.
  - `index2`: Index of the position in the subgrid.
  - `user`: Player making the move ('X' or 'O').

#### `winning_condition(self, index1, user)`
- Checks if the game satisfies any winning conditions after a move.
- Parameters:
  - `index1`: Index of the subgrid.
  - `user`: Player who made the move.
- If a winning condition is met, calls `subgrid_winner()`.

#### `subgrid_win(self, index1, user)`
- Declares a winner for the subgrid.
- Parameters:
  - `index1`: Index of the subgrid.
  - `user`: Player who won ('X' or 'O').
- Updates the state of the subgrid accordingly.

#### `referee(self)`
- Checks all subgrids for winning conditions to determine the ultimate winner.

#### `_validate(self, index1, index2,user)`
- Validates each move made by a player, ensuring it's legal and adheres to game rules.
- Parameters:
  - `index1`: Index of the subgrid being validated.
  - `index2`: Position in the subgrid being validated.
  - `user` : the user being validated
- Checks if the move is legal (empty cell and unclaimed subgrid).

## Usage
To use the `Game` class:
1. Create an instance of the `Game` class.
2. Use the `next_move` method to make moves.
3. Check for winners using the `refree` method.
4. Access the game state using the `getGameState` method.

### Example
python
Create a new instance of the game
game = Game()

Make a move
game.next_move(0, 0, 'x')

Print the game state
print(game)

Check for winners
game.refree()

## Conclusion
The Game class provides a comprehensive implementation of the Ultimate Tic-Tac-Toe game, allowing players to make moves, validating them, and determining winners. With detailed documentation, users can easily understand and utilize the class for playing the game
