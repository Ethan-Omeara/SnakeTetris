"""This file contains and controls the GUI for Snake-Tetris."""

from tkinter import Tk, Frame, Label, Button, Toplevel, StringVar
root = Tk()
# Constants
MENU_CELL_SIZE = 50
GAME_CELL_SIZE = 20

# Colours
WHITE = "#FFFFFF"
GREY = "#7F7F7F"
BLACK = "#000000"
GREEN = "#34DE34"
RED = "#FF0000"
BLUE = "#1515B9"

class Menu:
    """Represents the GUI for the menu."""

    def __init__(self, func_exit: callable, func_play: callable) -> None:
        """Initialise and generate the main menu."""
        root.title("Snake-Tetris")

        root.columnconfigure(list(range(0, 8)), minsize=MENU_CELL_SIZE)
        root.rowconfigure(list(range(0, 11)), minsize=MENU_CELL_SIZE)
        # Draw Tetris
        Frame(root, bg=BLUE).grid(row=3, column=3, rowspan=2,
                                       columnspan=2, sticky="NSEW")
        Label(root, bg=BLUE, fg=WHITE, text="T E T R I S",
              font=("System", 40, "bold")).grid(row=1, column=1, rowspan=2,
                                                columnspan=6, sticky="NSEW")

        # Draw Snake
        Label(root, bg=GREEN, text=".        .",
              font=("System", 15, "bold")).grid(
                    row=7, column=6, rowspan=1, columnspan=1, sticky="NSEW")
        Button(root, bg=RED, fg=WHITE, text="X",
               font=("System", 20, "bold"), command=func_exit).grid(
                    row=9, column=6, rowspan=1, columnspan=1, sticky="NSEW")
        Label(root, bg=GREEN, fg=BLACK, text="S N A K E",
              font=("System", 30, "bold")).grid(
                    row=6, column=1, rowspan=1, columnspan=6, sticky="NSEW")

        # Buttons
        Button(root, bg=GREY, fg=WHITE, text="PLAY",
               font=("System", 20, "bold"), command=func_play).grid(
                   row=8, column=1, columnspan=4, sticky="NSEW")
        Button(root, bg=GREY, fg=WHITE, text="SCORES",
               font=("System", 15, "bold")).grid(
                   row=9, column=1, columnspan=2, sticky="NSEW")
        Button(root, bg=GREY, fg=WHITE, text="CREDITS",
               font=("System", 15, "bold")).grid(
                   row=9, column=3, columnspan=2, sticky="NSEW")

        root.minsize(50*8, 50*11)
        root.maxsize(50*8, 50*11)

        root.mainloop()


class GameScreen:
    """Represents the game GUI and relevant functions."""

    def __init__(self, size_x: int, size_y: int) -> None:
        """Initialise the game GUI with a given size."""
        self.win = Toplevel(root)
        self.win.grab_set()
        self.win.title("Play Game")

        self.gamespace = Frame(self.win, highlightbackground=BLACK,
                               highlightthickness=2)
        self.gamespace.grid(column=0, row=0, padx=5, pady=5)

        self.gamegrid = []
        for x in range(size_x):
            self.gamegrid.append([])
            for y in range(size_y):
                cell = Frame(self.gamespace, background=GREY,
                             highlightbackground=BLACK, highlightthickness=1,
                             height=GAME_CELL_SIZE, width=GAME_CELL_SIZE)
                cell.grid(column=x, row=y)
                self.gamegrid[x].append(cell)

        # Setup score
        self.score_var = StringVar(root, "Score: 0")
        Label(self.win, textvariable=self.score_var,
              font=("System", 20, "bold")).grid(
                  row=size_y+1, column=0, rowspan=size_x)

    def update_score(self, score: int) -> None:
        """Update score label."""
        self.score_var.set("Score: " + str(score))

    def end_game(self, score: int) -> None:
        """Display game end to user."""
        self.score_var.set("GAME ENDED\nFINAL SCORE: " + str(score))

    def update_gamespace(self, grid: list) -> None:
        """Update the board with a given grid."""
        size_x = len(grid)
        size_y = len(grid[0])

        for x in range(size_x):
            for y in range(size_y):
                if grid[x][y] == 0:
                    self.gamegrid[x][y].configure(background=GREY)
                elif grid[x][y] == 1:
                    self.gamegrid[x][y].configure(background=GREEN)
                elif grid[x][y] == 2:
                    self.gamegrid[x][y].configure(background=RED)
                elif grid[x][y] == 3:
                    self.gamegrid[x][y].configure(background=BLACK)

        root.update()
