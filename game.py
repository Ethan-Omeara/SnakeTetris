

class GameController:
    def __init__(self, width=3, height=2) -> None:
        self.board = [[0]*width]*height
        self.snake = [[0, 0]]
        self.dir = [1, 0] # Steps for the snake, x, y
    
    def __str__(self) -> str:
        print(self.board)
        board_str=''
        for row in self.board:
            for column in row:
                board_str = board_str+str(row[column])+' '
            board_str = board_str+'\n'
        return board_str
    
    def step(self) -> None:
        """Run through one loop of the game"""
        print(self.snake)
        # Get head position
        head = self.snake[0]
        # Get new snake head position
        new_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
        self.snake.insert(0, new_head)
        # Update board
        self.board[new_head[1]][new_head[0]] = 1
        # Remove the end of the snake
        
        self.board[self.snake[-1]][new_head[0]] = 1
        self.snake.pop()
        print(self.snake)
        
    


test = GameController()
print(test)

while True:
    input()
    test.step()