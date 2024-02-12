from typing import Callable
from config import TETRIMINO_START_COLUMN as START_COL

class Tetrimino:
    def __init__(
        self,
        relative_coords: list,
        color: tuple,
        rotate_left_fn: Callable,
        rotate_right_fn: Callable,
        x: int = START_COL,
        y: int = 0
    ):
        self.x = x
        self.y = y
        self.relative_coords = relative_coords
        self.color=color
        self.rotate_left_fn = rotate_left_fn
        self.rotate_right_fn = rotate_right_fn
        self.update_absolute_coords()

    def update_absolute_coords(self):
        self.absolute_coords = [
            [self.x + coord[0], self.y + coord[1]] for coord in self.relative_coords
        ]

    def move_down(self) -> None:
        """
        Increments the y-value of each tetrimino block.
        """
        self.y += 1
        for i in range(len(self.absolute_coords)):
            self.absolute_coords[i][1] += 1

    def move_left(self) -> None:
        """
        Decrements the x-value of each tetrimino block.
        """
        self.x -= 1
        for i in range(len(self.absolute_coords)):
            self.absolute_coords[i][0] -= 1

    def move_right(self) -> None:
        """
        Increments the x-value of each tetrimino block.
        """
        self.x += 1
        for i in range(len(self.absolute_coords)):
            self.absolute_coords[i][0] += 1

    def calculate_rotate_right_2x2(self):
        pass

    def calculate_rotate_left_2x2(self):
        pass

    def calculate_rotate_right_3x3(self):
        pass

    def calculate_rotate_left_3x3(self):
        pass

    def calculate_rotate_right_4x4(self):
        pass

    def calculate_rotate_left_4x4(self):
        pass

class IBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [0, 1],
                [1, 1],
                [2, 1],
                [3, 1]
            ],
            color=(0, 255, 255), # Cyan
            rotate_left_fn=self.calculate_rotate_left_4x4,
            rotate_right_fn=self.calculate_rotate_right_4x4
        )

class JBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [0, 0],
                [0, 1],
                [1, 1],
                [2, 1]
            ],
            color=(0, 0, 255), # Blue
            rotate_left_fn=self.calculate_rotate_left_3x3,
            rotate_right_fn=self.calculate_rotate_right_3x3
        )

class LBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [0, 1],
                [1, 1],
                [2, 1],
                [2, 0]
            ],
            color=(255, 165, 0), # Orange
            rotate_left_fn=self.calculate_rotate_left_3x3,
            rotate_right_fn=self.calculate_rotate_right_3x3
        )

class OBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [1, 0],
                [1, 1],
                [2, 1],
                [2, 0]
            ],
            color=(255, 255, 0), # Yellow
            rotate_left_fn=self.calculate_rotate_left_2x2,
            rotate_right_fn=self.calculate_rotate_right_2x2
        )

class SBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [0, 1],
                [1, 1],
                [1, 0],
                [2, 0]
            ],
            color=(0, 255, 0), # Green
            rotate_left_fn=self.calculate_rotate_left_3x3,
            rotate_right_fn=self.calculate_rotate_right_3x3
        )

class TBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [1, 0],
                [0, 1],
                [1, 1],
                [2, 1]
            ],
            color=(128, 0, 128), # Purple
            rotate_left_fn=self.calculate_rotate_left_3x3,
            rotate_right_fn=self.calculate_rotate_right_3x3
        )

class ZBlock(Tetrimino):
    def __init__(self):
        super().__init__(
            relative_coords=[
                [0, 0],
                [1, 0],
                [1, 1],
                [2, 1]
            ],
            color=(255, 0, 0), # Red
            rotate_left_fn=self.calculate_rotate_left_3x3,
            rotate_right_fn=self.calculate_rotate_right_3x3
        )

TETRIMINO_CLASSES = [IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock]