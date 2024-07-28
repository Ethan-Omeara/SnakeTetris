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

game = GameController(GRID_X, GRID_Y)

def up(): game.dir = [0, -1]
def down(): game.dir = [0, 1]
def left(): game.dir = [-1, 0]
def right(): game.dir = [1, 0]

keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)
keyboard.add_hotkey('a', left)
keyboard.add_hotkey('d', right)


def play():
    game_screen = gui.GameScreen(GRID_X, GRID_Y)

    game.create_event("draw_board", game_screen.update_gamespace)
    game_screen.update_gamespace(game.board)

    while True:
        time.sleep(0.5)
        game.step()


gui.Menu(exit, play)