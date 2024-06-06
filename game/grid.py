from config import GRID_COLS, GRID_ROWS

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

    def check_row_full(self, row: int) -> bool:
        return all(cell is not None for cell in self.grid[row])

    def clear_line(self, row_idx: int) -> None:
        self.grid.pop(row_idx)
        self.grid.insert(0, [None for _ in range(self.cols)])