from config import TETRIMINO_START_COLUMN as START_COL

class Tetrimino:
    def __init__(self, coords=[], color=None):
        self.coords = coords
        self.color = color

    def move_down(self):
        """Increments the y-value of each tetrimino block.
        """
        for i in range(len(self.coords)):
            self.coords[i][1] += 1
        # should also implement hard drop

    def move_left(self):

        for i in range(len(self.coords)):
            self.coords[i][0] -= 1

        return 0

    def move_right(self):

        for i in range(len(self.coords)):
            self.coords[i][0] += 1

        return 0

class IBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL, 1],
                [START_COL+1, 1],
                [START_COL+2, 1],
                [START_COL+3, 1]
            ],
            color = (0, 255, 255) # Cyan
        )

class JBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL, 0],
                [START_COL, 1],
                [START_COL+1, 1],
                [START_COL+2, 1]
            ],
            color=(0, 0, 255) # Blue
        )

class LBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL, 1],
                [START_COL+1, 1],
                [START_COL+2, 1],
                [START_COL+2, 0]
            ],
            color = (255, 165, 0) # Orange
        )

class OBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL+1, 0],
                [START_COL+1, 1],
                [START_COL+2, 1],
                [START_COL+2, 0]
            ],
            color = (255, 255, 0) # Yellow
        )

class SBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL, 1],
                [START_COL+1, 1],
                [START_COL+1, 0],
                [START_COL+2, 0]
            ],
            color = (0, 255, 0) # Green
        )

class TBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL+1, 0],
                [START_COL, 1],
                [START_COL+1, 1],
                [START_COL+2, 1]
            ],
            color = (128, 0, 128) # Purple
        )

class ZBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            coords=[
                [START_COL, 0],
                [START_COL+1, 0],
                [START_COL+1, 1],
                [START_COL+2, 1]
            ],
            color = (255, 0, 0) # Red
        )