"""This file runs the Snake-Tetris game and GUI.

Author: Ethan O'Meara
Date: 25/06/2024
Description: A python program using Tkinter to run
a game inspired by Snake and Tetris.
"""
# Get relevant dictionaries
from game import GameController
import gui
# Get base modules
from time import time, sleep
import keyboard

# Constants
GRID_X = 10
GRID_Y = 20
DIVIDER = 9  # Where to place the divider between the snake and tetris regions

Game = None
GameScreen = None
active = False


def key_down(event: keyboard.KeyboardEvent):
    """Handle keyboard events and communicate with game controller."""
    if event.name in ["w", "up"]:
        Game.dir = [0, -1]
    elif event.name in ["s", "down"]:
        Game.dir = [0, 1]
    elif event.name in ["a", "left"]:
        Game.dir = [-1, 0]
    elif event.name in ["d", "right"]:
        Game.dir = [1, 0]


def end_game():
    """Stop the game loop and display final score."""
    global active
    active = False
    GameScreen.end_game(Game.score)


def play():
    """Run the Tetris-Snake game."""
    # Declare board and gui
    global Game
    global GameScreen
    global active
    active = True
    Game = GameController(GRID_X, GRID_Y, DIVIDER)
    GameScreen = gui.GameScreen(GRID_X, GRID_Y)

    # Set events
    Game.create_event("draw_board", GameScreen.update_gamespace)
    Game.create_event("end_game", end_game)
    Game.create_event("update_score", GameScreen.update_score)
    GameScreen.update_gamespace(Game.board)

    keyboard.on_press(key_down)

    # Run the game
    sleep(1)
    while active:
        start_time = time()
        Game.step()
        process_time = time()
        sleep_time = start_time+0.25-process_time
        if sleep_time > 0:
            print("Frame took too long!")
            sleep(sleep_time)


gui.Menu(exit, play)
