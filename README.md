# 6 in 1 Game Arcade

A fun-packed 6-in-1 arcade game application built using Python's `tkinter` module. Play classic games, track your scores, and challenge your memory and reflexes — all in one interface.

---

## Included Games

1. **Memory Game** 
2. **Tic-Tac-Toe** .
3. **Number Sliding Puzzle (15 Puzzle)**
4. **Snake**
5. **Single Player Pong** 
6. **Color Shooter**

## Features

- **Login System**
  - Create a new user or log in with an existing one.
  - User credentials stored securely in `.dat` files using Python's `pickle` module.

- **Score Tracking**
  - Each game tracks a high score and its user.
  - Scores are saved for each game and loaded on login.

- **Modular Structure**
  - Each game is contained in its own module for clarity and reuse.
  - Run the main app to launch any game.

## Dependencies

- python 3.x
- keyboard (if not installed, install using `pip install keyboard`)
- PIL 11.2.1 (if not installed, install using `pip install pillow`)

## How To run

1. Clone the repository
2. Go to root folder
3. run command `python __main__.py`
