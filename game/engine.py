import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLS, GRID_ROWS
# from game.tetrimino import ZBlock

from .gui import GUI

class GameEngine:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.running = True

    def run(self) -> None:
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            grid = [[None for col in range(GRID_COLS)] for row in range(GRID_ROWS)]

            # tet = ZBlock()
            # for (col, row) in tet.get_cells():
            #     grid[row][col] = tet.get_color()

            self.gui.draw_board(grid)

            pygame.display.flip()
            pygame.time.Clock().tick(60) # Limit frames per second