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

# Constants
GRID_X = 10
GRID_Y = 20

def play():
    game = GameController(GRID_X, GRID_Y)
    print(game) # Print initial board

    game.step() # Move right 1
    print(game)

    game.dir = [0, 1] # Move down 1 (Note: y value increases going down the board)
    game.step()
    print(game)

    game.dir = [-1, 0] # Move left 1
    game.step()
    print(game)

    game.dir = [0, -1] # Move up 1
    game.step()
    print(game)

    game_screen = gui.GameScreen(GRID_X, GRID_Y)
    game.create_event("draw_board", game_screen.update_gamespace)


gui.Menu(exit, play)