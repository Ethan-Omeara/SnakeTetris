"""
Author: Ethan O'Meara
Date: 25/06/2024
Description: A python program using Tkinter to run 
             a game inspired by Snake and Tetris
"""
# Get relevant dictionaries
from tkinter import *
from tkinter import ttk

from game import GameController
import gui
import time
import keyboard

# Constants
GRID_X = 10
GRID_Y = 20
DIVIDER = 9 # Where to place the divider between the snake and tetris regions

game = None
game_screen = None
active = False

def key_down(event: keyboard.KeyboardEvent):
    if event.name in ["w", "up"]:
        game.dir = [0, -1]
    elif event.name in ["s", "down"]:
        game.dir = [0, 1]
    elif event.name in ["a", "left"]:
        game.dir = [-1, 0]
    elif event.name in ["d", "right"]:
        game.dir = [1, 0]

def end_game():
    global active
    active = False
    game_screen.end_game(game.score)

def play():
    # Declare board and gui
    global game
    global game_screen
    global active
    active = True
    game = GameController(GRID_X, GRID_Y, DIVIDER)
    game_screen = gui.GameScreen(GRID_X, GRID_Y, DIVIDER)

    # Set events
    game.create_event("draw_board", game_screen.update_gamespace)
    game.create_event("end_game", end_game)
    game.create_event("update_score", game_screen.update_score)
    game_screen.update_gamespace(game.board)

    keyboard.on_press(key_down)
    
    # Run the game
    time.sleep(1)
    while active:
        start_time = time.time()
        game.step()
        process_time = time.time()
        sleep_time = start_time+0.25-process_time
        if sleep_time > 0:
            time.sleep(sleep_time)


gui.Menu(exit, play)