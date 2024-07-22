

class GameController:
    def __init__(self, width=3, height=2) -> None:
        # Note to self: board 2d list is formatted so you can do board[x][y]
        self.board = [[0]*height for i in range(width)]
        self.snake = [[0, 1]]
        self.board[0][1] = 1
        self.dir = [1, 0] # Steps for the snake, x, y
    
    def __str__(self) -> str:
        board_str=''
        rows = len(self.board[0])
        for row in range(rows):
            for column in self.board:
                board_str = board_str+str(column[row])+' '
            board_str = board_str+'\n'
        return board_str
    
    def step(self) -> int:
        """Run through one loop of the game, return status
        0 - OK
        1 - Game End"""
        # Get head position
        head = self.snake[0]
        # Get new snake head position
        new_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
        print(not new_head[0] in range(len(self.board)))
        if not (new_head[0] in range(len(self.board)) or not new_head[1] in range(len(self.board[0]))):
            return 1
        self.snake.insert(0, new_head)
        # Update board
        self.board[new_head[0]][new_head[1]] = 1
        # Remove the end of the snake
        self.board[self.snake[-1][0]][self.snake[-1][1]] = 0
        self.snake.pop()
        return 0
    
    def end_game(self) -> list:
        return self.board
    


# test = GameController()

# while True:
#     print(test.snake)
#     print(test)
#     input()
#     print(test.step())