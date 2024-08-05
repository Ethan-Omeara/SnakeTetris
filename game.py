import random
import time

class GameController:
    def __init__(self, width, height, divider) -> None:
        # Note to self: board 2d list is formatted so you can do board[x][y]
        self.board = [[0]*height for i in range(width)]
        self.snake = [[0, 4],[0, 3],[0, 2],[0, 1]]
        for cell in self.snake:
            self.board[cell[0]][cell[1]] = 1
        self.dir = [1, 0] # Steps for the snake, x, y
        self.events = []

        self.divider = divider
        for column in self.board:
            column[divider] = 3

        self.create_apple() # Create first apple
        print(self)
    
    def __str__(self) -> str:
        board_str=''
        rows = len(self.board[0])
        for row in range(rows):
            for column in self.board:
                board_str = board_str+str(column[row])+' '
            board_str = board_str+'\n'
        return board_str
    
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

    def kill_snake(self) -> None:
        """Display an animation for killing the snake, and reset program"""
        snake_stop = False
        while snake_stop == False:
            # Check all spots directly below snake for something to block it
            for cell in self.snake:
                print(cell[1]+1, len(self.board[1]))
                if cell[1]+1 >= len(self.board[1]):
                    print("Snake below board")
                    snake_stop = True
                    break
                if self.board[cell[0]][cell[1]+1] == 1:
                    # Check if cell is a part of existing snake
                    if not [cell[0], cell[1]+1] in self.snake:
                        print("Cell found below snake")
                        snake_stop = True
                        break
            if snake_stop: break
            # If code has reached this point, the snake needs to move down 1
            # Remove previous snake
            for cell in self.snake:
                self.board[cell[0]][cell[1]] = 0
                if cell[1] == self.divider:
                    self.board[cell[0]][cell[1]] = 3
            # Create new snake
            for i, cell in enumerate(self.snake):
                new_cell = [cell[0], cell[1]+1]
                self.snake[i] = new_cell
                self.board[new_cell[0]][new_cell[1]] = 1
            
            self.call_event("draw_board", self.board)
            time.sleep(0.5)
        # Reset board
        self.snake = [[0, 4],[0, 3],[0, 2],[0, 1]]
        for cell in self.snake:
            self.board[cell[0]][cell[1]] = 1
        self.dir = [1, 0] # Steps for the snake, x, y
            

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
            # Remove the end of the snake
            self.board[self.snake[-1][0]][self.snake[-1][1]] = 0
            self.snake.pop()
        else:
            self.create_apple()

        # Add head
        self.snake.insert(0, new_head)
        self.board[new_head[0]][new_head[1]] = 1
        
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