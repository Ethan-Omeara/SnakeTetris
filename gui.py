from tkinter import *
root = Tk()
# Constants
MENU_CELL_SIZE = 50
GAME_CELL_SIZE = 20

class Menu:
    def __init__(self, func_exit: callable, func_play: callable) -> None:
        root.title("Snake-Tetris")

        root.columnconfigure(list(range(0, 8)), minsize=MENU_CELL_SIZE)
        root.rowconfigure(list(range(0, 11)), minsize=MENU_CELL_SIZE)
        # Draw Tetris
        Frame(root, bg="#1515B9").grid(row=3, column=3, rowspan=2, columnspan=2, sticky="NSEW")
        Label(root, bg="#1515B9", fg="#FFFFFF", text="T E T R I S", font=("System", 40, "bold")).grid(row=1, column=1, rowspan=2, columnspan=6, sticky="NSEW")

        # Draw Snake
        Label(root, bg="#34DE34", text=".        .", font=("System", 15, "bold")).grid(row=7, column=6, rowspan=1, columnspan=1, sticky="NSEW")
        Button(root, bg="#FF0000", fg="#FFFFFF", text="X", font=("System", 20, "bold"), command=func_exit).grid(row=9, column=6, rowspan=1, columnspan=1, sticky="NSEW")
        Label(root, bg="#34DE34", fg="#000000", text="S N A K E", font=("System", 30, "bold")).grid(row=6, column=1, rowspan=1, columnspan=6, sticky="NSEW")

        # Buttons
        Button(root, bg="#7F7F7F", fg="#FFFFFF", text="PLAY", font=("System", 20, "bold"), command=func_play).grid(row=8, column=1, columnspan=4, sticky="NSEW")
        Button(root, bg="#7F7F7F", fg="#FFFFFF", text="SCORES", font=("System", 15, "bold")).grid(row=9, column=1, columnspan=2, sticky="NSEW")
        Button(root, bg="#7F7F7F", fg="#FFFFFF", text="CREDITS", font=("System", 15, "bold")).grid(row=9, column=3, columnspan=2, sticky="NSEW")

        root.minsize(50*8, 50*11)
        root.maxsize(50*8, 50*11)

        root.mainloop()

class GameScreen:
    def __init__(self, size_x, size_y) -> None:
        self.win = Toplevel(root)
        self.win.grab_set()
        self.win.title("Play Game")

        self.gamespace = Frame(self.win, highlightbackground="black", highlightthickness=2)
        self.gamespace.grid(column=0, row=0, padx=5, pady=5)

        self.gamegrid = []
        for x in range(size_x):
            self.gamegrid.append([])
            for y in range(size_y):
                cell = Frame(self.gamespace, background="gray", highlightbackground="black", highlightthickness=1, height=GAME_CELL_SIZE, width=GAME_CELL_SIZE)
                cell.grid(column=x, row=y)
                self.gamegrid[x].append(cell)
        #self.win.minsize(GAME_CELL_SIZE*size_x, GAME_CELL_SIZE*size_y)
        #self.win.maxsize(GAME_CELL_SIZE*size_x, GAME_CELL_SIZE*size_y)

    def update_gamespace(self, grid):
        size_x = len(grid)
        size_y = len(grid[0])

        for x in range(size_x):
            for y in range(size_y):
                if grid[x][y] == 0:
                    self.gamegrid[x][y].configure(background="gray")
                elif grid[x][y] == 1:
                    self.gamegrid[x][y].configure(background="light green")