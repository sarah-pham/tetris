import random
from config import GRID_COLS, GRID_ROWS
from .tetrimino import Tetrimino

class Grid:
    def __init__(self, rows=GRID_ROWS, cols=GRID_COLS) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def spawn_tetrimino(self) -> None:
        """Creates a Tetrimino of a random class and it adds to the grid.
        """
        random_tetrimino_class = random.choice(Tetrimino.__subclasses__())
        tet = random_tetrimino_class()

        for (x, y) in tet.get_cells():
            self.grid[y][x] = tet.get_color()