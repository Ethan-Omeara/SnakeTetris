class GameController:
    def __init__(self, width=3, height=2) -> None:
        # Note to self: board 2d list is formatted so you can do board[x][y]
        self.board = [[0]*height for i in range(width)]
        self.snake = [[0, 10],[0, 9],[0, 8],[0, 7],[0, 6],[0, 5],[0, 4],[0, 3],[0, 2],[0, 1]]
        for cell in self.snake:
            self.board[cell[0]][cell[1]] = 1
        self.dir = [1, 0] # Steps for the snake, x, y
        self.events = []
    
    def __str__(self) -> str:
        board_str=''
        rows = len(self.board[0])
        for row in range(rows):
            for column in self.board:
                board_str = board_str+str(column[row])+' '
            board_str = board_str+'\n'
        return board_str
    
    def step(self) -> None:
        """Run through one loop of the game"""
        # Get head position
        head = self.snake[0]
        # Get new snake head position
        new_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
        # Check if a wall is hit
        if (not new_head[0] in range(len(self.board)) or not (new_head[1] in range(len(self.board[0])))):
            print("Game Ended - Snake hit wall")
            self.call_event("end_game")
            return
        # Check if the snake itself is hit
        # Note: Last element is omitted as that is about to be removed
        for cell in self.snake[:-1]:
            # Check if coordinates match
            if new_head == cell:
                print("Game Ended - Snake hit self")
                self.call_event("end_game")
                return

        # Remove the end of the snake
        self.board[self.snake[-1][0]][self.snake[-1][1]] = 0
        self.snake.pop()

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