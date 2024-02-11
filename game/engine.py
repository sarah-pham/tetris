import pygame
import random
import time
from typing import Optional
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, DROP_INTERVAL, AUTO_RESTART
from .grid import Grid
from .tetrimino import Tetrimino
from .gui import GUI


class GameEngine:
    def __init__(self) -> None:
        self.running = True
        self.game_over = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.reset_game_state()

    def run(self) -> None:
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.handle_key_pressed(event)

            # Generate a new tetrimino if there is no current one
            if self.tetrimino == None:
                self.tetrimino = GameEngine.generate_tetrimino()

            # Draw the game on the GUI
            GameEngine.draw_game_state(self.gui, self.grid, self.tetrimino)

            # Handle the automatic dropping of the current tetrimino
            self.handle_automatic_dropping(self.tetrimino)

            # Check and handle game over
            if GameEngine.check_game_over(self.grid):
                self.game_over = True
                if AUTO_RESTART:
                    self.reset_game_state()
                else:
                    self.running = False

            # Limit frames per second
            pygame.time.Clock().tick(60)
        
    def handle_key_pressed(self, event):
        if self.tetrimino == None:
            return
        if event.key == pygame.K_LEFT:
            if GameEngine.can_move_left(self.grid, self.tetrimino):
                self.tetrimino.move_left()
        if event.key == pygame.K_RIGHT:
            if GameEngine.can_move_right(self.grid, self.tetrimino):
                self.tetrimino.move_right()
        if event.key == pygame.K_DOWN:
            if GameEngine.can_move_down(self.grid, self.tetrimino):
                self.tetrimino.move_down()
        if event.key == pygame.K_SPACE:
            while GameEngine.can_move_down(self.grid, self.tetrimino):
                self.tetrimino.move_down()

    def reset_game_state(self) -> None:
        """
        Resets the game state to start a new session.
        """
        self.grid = Grid()
        self.tetrimino: Optional[Tetrimino] = None
        self.last_drop_time = time.time()

    def handle_automatic_dropping(self, tetrimino: Tetrimino) -> None:
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
    def check_game_over(grid: Grid) -> bool:
        for x in grid.grid[0]:
            if x != None:
                return True
        return False

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
    def can_move_left(grid: Grid, tet: Tetrimino) -> bool:
        """
        Returns True if the Tetrimino can move left by one position on the grid
        without overlapping existing blocks, False otherwise.
        """
        for (x, y) in tet.coords:
            if not grid.is_available(x - 1, y):
                return False
        return True
    
    @staticmethod
    def can_move_right(grid: Grid, tet: Tetrimino) -> bool:
        """
        Returns True if the Tetrimino can move right by one position on the grid
        without overlapping existing blocks, False otherwise.
        """
        for (x, y) in tet.coords:
            if not grid.is_available(x + 1, y):
                return False
        return True

    @staticmethod
    def can_move_left(grid: Grid, tet: Tetrimino) -> bool:
        """
        Returns True if the Tetrimino can move left by one position on the grid
        without overlapping existing blocks, False otherwise.
        """
        for (x, y) in tet.coords:
            if not grid.is_available(x - 1, y):
                return False
        return True
    
    @staticmethod
    def can_move_right(grid: Grid, tet: Tetrimino) -> bool:
        """
        Returns True if the Tetrimino can move right by one position on the grid
        without overlapping existing blocks, False otherwise.
        """
        for (x, y) in tet.coords:
            if not grid.is_available(x + 1, y):
                return False
        return True

    @staticmethod
    def put(grid: Grid, tet: Tetrimino) -> None:
        """
        Places the Tetrimino on the grid.
        """
        for (x, y) in tet.coords:
            grid.set(x, y, tet.color)