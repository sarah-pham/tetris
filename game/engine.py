import pygame
import random
import time
from typing import Optional
from config import SCREEN_WIDTH, SCREEN_HEIGHT, DROP_INTERVAL
from .grid import Grid
from .tetrimino import Tetrimino
from .gui import GUI


class GameEngine:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.running = True
        self.grid = Grid()
        self.last_drop_time = time.time()
        self.tetrimino: Optional[Tetrimino] = None

    def run(self) -> None:
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Generate a new tetrimino if there is no current one
            if self.tetrimino == None:
                self.tetrimino = GameEngine.generate_tetrimino()

            # Draw the game on the GUI
            GameEngine.draw_game_state(self.gui, self.grid, self.tetrimino)

            # Handle the automatic dropping of the current tetrimino
            self.handle_automatic_dropping(self.tetrimino)

            # Limit frames per second
            pygame.time.Clock().tick(60)

    def handle_automatic_dropping(self, tetrimino: Tetrimino):
        """
        Automatically moves the Tetrimino down every DROP_INTERVAL seconds. If
        it cannot move further, the Tetrimino is placed on the grid, marking its
        final position, and the current tetrimino is reset to None.
        """
        if time.time() - self.last_drop_time >= DROP_INTERVAL:
            if GameEngine.can_move_down(self.grid, tetrimino):
                tetrimino.move_down()
            else:
                GameEngine.put(self.grid, tetrimino)
                self.tetrimino = None

            self.last_drop_time = time.time()

    @staticmethod
    def draw_game_state(gui: GUI, grid: Grid, tetrimino: Tetrimino) -> None:
        """
        Renders the current game state on the GUI.
        """
        # Draw the Tetris grid with existing blocks
        gui.draw_board(grid.grid)

        # Overlay the current tetrimino on the grid
        for (x, y) in tetrimino.coords:
            gui.draw_block(x, y, tetrimino.color)

        # Update the display
        gui.update_display()

    @staticmethod
    def generate_tetrimino() -> Tetrimino:
        """
        Returns a Tetrimino instance of a randomly selected class.
        """
        random_tetrimino_class = random.choice(Tetrimino.__subclasses__())
        tetrimino = random_tetrimino_class()
        return tetrimino

    @staticmethod
    def can_move_down(grid: Grid, tet: Tetrimino) -> bool:
        """
        Returns True if the Tetrimino can move down by one position on the grid
        without overlapping existing blocks, False otherwise.
        """
        for (x, y) in tet.coords:
            if not grid.is_available(x, y + 1):
                return False
        return True

    @staticmethod
    def put(grid: Grid, tet: Tetrimino) -> None:
        """
        Places the Tetrimino on the grid.
        """
        for (x, y) in tet.coords:
            grid.set(x, y, tet.color)