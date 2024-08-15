import random
import time
import copy

class GameController:
    def __init__(self, width, height, divider) -> None:
        # Note to self: board 2d list is formatted so you can do board[x][y]
        # Initialise variables
        self.last_dir = [0, 0]
        self._dir = [0, 0]
        self.events = []
        self.board = [[0]*height for i in range(width)]
        self.divider = divider

        # Setup board
        self.spawn_snake(animate=False)
        for column in self.board:
            column[divider] = 3
        self.create_apple() # Create first apple
    
    def __str__(self) -> str:
        board_str=''
        rows = len(self.board[0])
        for row in range(rows):
            for column in self.board:
                board_str = board_str+str(column[row])+' '
            board_str = board_str+'\n'
        return board_str
    
    # Create a "getter" for the dir property
    @property
    def dir(self) -> list:
        return self._dir
    
    # Create a "setter" for dir
    @dir.setter
    def dir(self, new_direction):
        # Only allow the direction to be changed if it is
        # *not* the complete reverse direction
        reverse_dir = [i*-1 for i in self.last_dir]
        if not new_direction == reverse_dir:
            self._dir = new_direction
        else:
            print("Direction Not Permitted")
    
    def create_apple(self) -> None:
        """Create an apple randomly on the board"""
        while True:
            # Get a random space on the board
            x = random.choice(range(len(self.board)))
            y = random.choice(range(len(self.board[1])))

            # Check if space is blank
            if self.board[x][y] == 0 and y < self.divider:
                print(f"New apple at {x}, {y}")
                self.board[x][y] = 2
                break

    def spawn_snake(self, animate=True) -> None:
        width = len(self.board)
        # Pick starting position and direction
        # Note corners will not be chosen due to ambiguity with directions
        # ---------2---------
        # |                 |
        # |                 |
        # 1                 3
        # |                 |
        # |                 |
        start_pos = None
        valid = False
        while not valid:
            side = random.randint(1, 3)
            if side == 1:
                self.dir = [1, 0]
                self.last_dir = [1, 0]
                start_pos = [0, random.choice(range(1, self.divider-1))]
            elif side == 2:
                self.dir = [0, 1]
                self.last_dir = [0, 1]
                start_pos = [random.choice(range(1, width-1)), 0]
            elif side == 3:
                self.dir = [-1, 0]
                self.last_dir = [-1, 0]
                start_pos = [width-1, random.choice(range(1, self.divider-1))]
            # Check if spawn space is blank
            valid = self.board[start_pos[0]][start_pos[1]] == 0

        self.snake = [start_pos for i in range(4)]
        self.board[start_pos[0]][start_pos[1]] = 1
        if animate:
            # Animate start
            for i in range(3):
                self.board[start_pos[0]][start_pos[1]] = 0
                self.call_event("draw_board", self.board)
                time.sleep(0.2)
                self.board[start_pos[0]][start_pos[1]] = 1
                self.call_event("draw_board", self.board)
                time.sleep(0.2)
    
    def drop_snake(self) -> None:
        """Display animation to drop snake to the tetris board"""
        # Remove snake on the board
        for cell in self.snake:
            self.board[cell[0]][cell[1]] = 0
        
        while True:
            # Check all spots directly below snake for something to block it
            for cell in self.snake:
                if cell[1]+1 >= len(self.board[0]):
                    print("Snake below board")
                    return self.snake
                if self.board[cell[0]][cell[1]+1] == 1:
                    print("Cell found below snake")
                    return self.snake
            # If code has reached this point, the snake needs to move down 1
            # Create new snake on a temporary board (for animation)
            temp_board = copy.deepcopy(self.board)
            for i, cell in enumerate(self.snake):
                new_cell = [cell[0], cell[1]+1]
                self.snake[i] = new_cell
                temp_board[new_cell[0]][new_cell[1]] = 1
            
            self.call_event("draw_board", temp_board)
            time.sleep(0.05)

    def check_tetris(self) -> None:
        """Check the board below the divider and adjust for tetris rules"""
        
        # Check if any piece goes above the divider
        for cell in self.snake:
            if cell[1] <= self.divider:
                print("Snake above tetris board, game ended")
                self.call_event("end_game")
                return

        # Check for full rows
        full_rows = list(range(self.divider+1, len(self.board[0])))
        for column in self.board:
            for row, cell in enumerate(column):
                if row > self.divider and cell == 0 and row in full_rows:
                    full_rows.remove(row)
        # Remove all full rows, and shuffle everything else down
        for removed_row in full_rows:
            for column, _ in enumerate(self.board):
                # Loop from the bottom up
                rows = len(self.board[0])-1
                for row in range(rows, -1, -1):
                    if row == removed_row:
                        self.board[column][row] = 0
                    elif row < removed_row and row > self.divider:
                        self.board[column][row+1] = self.board[column][row]


    def kill_snake(self) -> None:
        """Run through code to kill the snake and respawn"""
        dropped_snake = self.drop_snake()
        for cell in dropped_snake:
            self.board[cell[0]][cell[1]] = 1
        self.check_tetris()
        # Find the apple and make it a "tree", blocking the snake
        for x, column in enumerate(self.board):
            for y, cell in enumerate(column):
                if cell == 2:
                    self.board[x][y] = 3
        self.create_apple()

        self.spawn_snake()
            

    def step(self) -> None:
        """Run through one loop of the game"""
        # Get head position
        head = self.snake[0]
        # Get new snake head position
        new_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
        # Check if a wall is hit
        if (not new_head[0] in range(len(self.board)) or not (new_head[1] in range(len(self.board[0])))):
            print("Game Ended - Snake hit wall")
            self.kill_snake()
            return
        # Check if the snake itself is hit
        # Note: Last element is omitted as that is about to be removed
        for cell in self.snake[:-1]:
            # Check if coordinates match
            if new_head == cell:
                print("Game Ended - Snake hit self")
                self.kill_snake()
                return
        # Check if a blocker has been hit
        if self.board[new_head[0]][new_head[1]] == 3:
            print("Game Ended - Snake hit blocker")
            self.kill_snake()
            return
        # Check if apple is hit, if it isn't then skip taking off the end
        # (causing the snake to get longer)
        if self.board[new_head[0]][new_head[1]] != 2:
            # Remove the end of the snake (checking no other part of the snake is there)
            if not self.snake[-1] in self.snake[:-1]:
                self.board[self.snake[-1][0]][self.snake[-1][1]] = 0
            self.snake.pop()
        else:
            self.create_apple()

        # Add head
        self.snake.insert(0, new_head)
        self.board[new_head[0]][new_head[1]] = 1
        # Update last direction
        self.last_dir = self.dir
        
        self.call_event("draw_board", self.board)
    
    def create_event(self, event: str, func: callable) -> None:
        """Create a game event to be called on certain conditions.
        Current events:
            draw_board - Sends a copy of the snake board to draw
            end_snake - Ends the snake portion of the game"""
        self.events.append([event, func])
    
    def call_event(self, event_name: str, arg=None) -> None:
        for event in self.events:
            if event[0] == event_name:
                if arg == None:
                    event[1]()
                else:
                    event[1](arg)