from config import TETRIMINO_START_COLUMN as START_COL

class Tetrimino:
    def __init__(self, cells=[], color=None):
        self.cells = cells
        self.color = color

    def get_cells(self):
        return self.cells

    def get_color(self):
        return self.color

class IBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL, 1),
                (START_COL+1, 1),
                (START_COL+2, 1),
                (START_COL+3, 1)
            ],
            color = (0, 255, 255) # Cyan
        )

class JBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL, 0),
                (START_COL, 1),
                (START_COL+1, 1),
                (START_COL+2, 1)
            ],
            color=(0, 0, 255) # Blue
        )

class LBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL, 1),
                (START_COL+1, 1),
                (START_COL+2, 1),
                (START_COL+2, 0)
            ],
            color = (255, 165, 0) # Orange
        )

class OBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL+1, 0),
                (START_COL+1, 1),
                (START_COL+2, 1),
                (START_COL+2, 0)
            ],
            color = (255, 255, 0) # Yellow
        )

class SBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL, 1),
                (START_COL+1, 1),
                (START_COL+1, 0),
                (START_COL+2, 0)
            ],
            color = (0, 255, 0) # Green
        )

class TBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL+1, 0),
                (START_COL, 1),
                (START_COL+1, 1),
                (START_COL+2, 1)
            ],
            color = (128, 0, 128) # Purple
        )

class ZBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            cells=[
                (START_COL, 0),
                (START_COL+1, 0),
                (START_COL+1, 1),
                (START_COL+2, 1)
            ],
            color = (255, 0, 0) # Red
        )