from typing import NamedTuple, Optional, Tuple, List
from config import GRID_COLS, GRID_ROWS
from .tetrimino import Tetrimino

class Grid:
    def __init__(self, rows=GRID_ROWS, cols=GRID_COLS) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def is_available(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False

        return self.grid[y][x] == None

    def set(self, x: int, y: int, color) -> None:
        self.grid[y][x] = color