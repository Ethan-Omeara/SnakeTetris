# Snake-Tetris
A python program using Tkinter to run a game inspired by Snake and Tetris
## Installation Instructions
- Download repository and extract into a folder.
- Download Python from [here](https://www.python.org/downloads/).
- Double-click the downloaded file.
- Follow instructions to install Python.

## Playing the Game
- Run game by double-clicking the `run.bat` file.
- Press `Play`.
- Use WASD or arrow keys to control the snake.
- Avoid blockers (black squares).
- Eat apples to increase length (red squares).
- Upon death, the snake will drop down onto the Tetris board below.
- Full lines will be removed and earn you points.
- Try to survive as long as possible, and don't fill up the Tetris board past the blockers!
> **Note:**  run.bat will automatically install the keyboard module, then run the program.

## Developer Notes
Game code uses an event system to communicate with the GUI, current events used are as follows:
| **Event**  | Description |
| ---------- |-------------|
| *draw_board* | Game board should be updated, returns current board. |
| *end_game* | Game has ended. |
| *update_score* | Player score has changed, returns current score. |