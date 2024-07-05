"""
Author: Ethan O'Meara
Date: 25/06/2024
Description: A python program using Tkinter to run 
             a game inspired by Snake and Tetris

Changes:
Version 1 - Basic Menu Design
"""

from tkinter import *
from tkinter import ttk

import game

CELL_SIZE = 50

root = Tk()
root.title("Snake-Tetris")

root.columnconfigure(list(range(0, 8)), minsize=CELL_SIZE)
root.rowconfigure(list(range(0, 11)), minsize=CELL_SIZE)

# Draw Tetris
Frame(root, bg="#1515B9").grid(row=3, column=3, rowspan=2, columnspan=2, sticky="NSEW")
Label(root, bg="#1515B9", fg="#FFFFFF", text="T E T R I S", font=("System", 40, "bold")).grid(row=1, column=1, rowspan=2, columnspan=6, sticky="NSEW")

# Draw Snake
Label(root, bg="#34DE34", text=".        .", font=("System", 15, "bold")).grid(row=7, column=6, rowspan=1, columnspan=1, sticky="NSEW")
Button(root, bg="#FF0000", fg="#FFFFFF", text="X", font=("System", 20, "bold"), command=exit).grid(row=9, column=6, rowspan=1, columnspan=1, sticky="NSEW")
Label(root, bg="#34DE34", fg="#000000", text="S N A K E", font=("System", 30, "bold")).grid(row=6, column=1, rowspan=1, columnspan=6, sticky="NSEW")

# Buttons
Button(root, bg="#7F7F7F", fg="#FFFFFF", text="PLAY", font=("System", 20, "bold")).grid(row=8, column=1, columnspan=4, sticky="NSEW")
Button(root, bg="#7F7F7F", fg="#FFFFFF", text="SCORES", font=("System", 15, "bold")).grid(row=9, column=1, columnspan=2, sticky="NSEW")
Button(root, bg="#7F7F7F", fg="#FFFFFF", text="CREDITS", font=("System", 15, "bold")).grid(row=9, column=3, columnspan=2, sticky="NSEW")

root.minsize(50*8, 50*11)
root.maxsize(50*8, 50*11)

root.mainloop()