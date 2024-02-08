import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.tetrimino import ZBlock
from game.grid import Grid

from .gui import GUI

class GameEngine:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.running = True
        self.grid = Grid()
        self.awaiting_new_tet = True

    def run(self) -> None:
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.awaiting_new_tet:
                self.grid.spawn_tetrimino()
                self.awaiting_new_tet = False

            self.gui.draw_board(self.grid.grid)

            pygame.display.flip()
            pygame.time.Clock().tick(60) # Limit frames per second