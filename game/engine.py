import pygame
from pygame.event import Event
import random
import time
from typing import Optional
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    DROP_INTERVAL,
    AUTO_RESTART,
)
from .grid import Grid
from .tetrimino import (
    Tetrimino,
    TETRIMINO_CLASSES
)
from .gui import GUI


class GameEngine:
    def __init__(self) -> None:
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.reset_game()

    def run(self) -> None:
        while self.running:
            self.handle_events()
            if not self.paused:
                self.update_game_state()
                self.draw_game_state()
            pygame.time.Clock().tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_pressed(event)

    def handle_key_pressed(self, event: Event) -> None:

        tetrimino_key_actions = {
            pygame.K_LEFT: self.move_tetrimino_left,
            pygame.K_RIGHT: self.move_tetrimino_right,
            pygame.K_DOWN: self.move_tetrimino_down,
            pygame.K_SPACE: self.handle_hard_drop,
            pygame.K_UP: self.rotate_right,
            pygame.K_z: self.rotate_left
        }

        system_key_actions = {
            pygame.K_ESCAPE: self.toggle_pause
        }

        if event.key in tetrimino_key_actions and not self.paused:
            tetrimino_key_actions[event.key]()

        if event.key in system_key_actions:
            system_key_actions[event.key]()

    def update_game_state(self) -> None:
        if not self.active_game:
            self.reset_game()

        if self.tetrimino is None:
            self.tetrimino = GameEngine.generate_tetrimino()

        self.handle_automatic_dropping()
        self.check_and_handle_game_over()

    def reset_game(self) -> None:
        """
        Resets the game state to start a new session.
        """
        self.active_game = True
        self.paused = False
        self.grid = Grid()
        self.tetrimino: Optional[Tetrimino] = None
        self.last_drop_time = time.time()

    def handle_automatic_dropping(self) -> None:
        """
        Automatically moves the current Tetrimino down every DROP_INTERVAL
        seconds. If it cannot move further, the Tetrimino is placed on the grid,
        marking its final position, and the current tetrimino is reset to None.
        """
        assert self.tetrimino is not None

        if time.time() - self.last_drop_time >= DROP_INTERVAL:
            move_success = self.move_tetrimino_down()
            if not move_success:
                self.place_tetrimino_on_grid()
                self.tetrimino = None

            self.last_drop_time = time.time()

    def draw_game_state(self) -> None:
        """
        Renders the current game state on the GUI.
        """
        # Draw the Tetris grid with existing blocks
        self.gui.draw_board(self.grid.grid)

        # Overlay the current tetrimino on the grid
        if self.tetrimino is not None:
            for x, y in self.tetrimino.absolute_coords:
                self.gui.draw_block(x, y, self.tetrimino.color)

        self.gui.draw_gridlines()
        self.gui.draw_game_images()

        # Update the display
        self.gui.update_display()

    @staticmethod
    def generate_tetrimino() -> Tetrimino:
        """
        Returns a Tetrimino instance of a randomly selected class.
        """
        RandomTetriminoClass = random.choice(TETRIMINO_CLASSES)
        tetrimino = RandomTetriminoClass()
        return tetrimino

    def check_and_handle_game_over(self) -> None:
        """
        Checks and handles game over.
        """
        if self.check_game_over():
            self.active_game = False
            if not AUTO_RESTART:
                self.running = False

    def check_game_over(self) -> bool:
        for x in self.grid.grid[0]:
            if x is not None:
                return True
        return False

    def move_tetrimino_down(self) -> bool:
        """
        Moves the current Tetrimino down one block if the grid space below is
        unoccupied.

        Returns:
            bool: True if the Tetrimino is successfully moved down; False
                  otherwise.
        """
        if self.tetrimino is None:
            return False

        # Check if any cells of the Tetrimino are blocked from below
        for x, y in self.tetrimino.absolute_coords:
            if not self.grid.is_available(x, y + 1):
                return False  # Immediately return False if blocked

        self.tetrimino.move_down()
        return True

    def move_tetrimino_left(self) -> bool:
        """
        Moves the current Tetrimino left one block if the adjacent grid space is
        unoccupied.

        Returns:
            bool: True if the Tetrimino is successfully moved left; False
                  otherwise.
        """
        if self.tetrimino is None:
            return False

        for x, y in self.tetrimino.absolute_coords:
            if not self.grid.is_available(x - 1, y):
                return False

        self.tetrimino.move_left()
        return True

    def move_tetrimino_right(self) -> bool:
        """
        Moves the current Tetrimino right one block if the adjacent grid space
        is unoccupied.

        Returns:
            bool: True if the Tetrimino is successfully moved right; False
                  otherwise.
        """
        if self.tetrimino is None:
            return False

        for x, y in self.tetrimino.absolute_coords:
            if not self.grid.is_available(x + 1, y):
                return False

        self.tetrimino.move_right()
        return True

    def handle_hard_drop(self) -> None:
        """
        Drops the current tetrimino to the lowest possible position on the grid.
        """
        while self.move_tetrimino_down():
            pass

    def rotate_right(self):
        """
        Rotates the tetrimino right, and gets new relative coordinates and kick data
        Updates rotate state if rotation is successful
        """
        if self.tetrimino is None:
            return

        new_relative_coords, kicks = self.tetrimino.rotate_right_fn()
        if self.kick_tetrimino(new_relative_coords, kicks):
            self.tetrimino.rotate_state = (self.tetrimino.rotate_state + 1) % 4

    def rotate_left(self):
        """
        Rotates the tetrimino left, and checks kick positions
        Updates rotate state if rotation is successful
        """
        if self.tetrimino is None:
            return

        new_relative_coords, kicks = self.tetrimino.rotate_left_fn()
        if self.kick_tetrimino(new_relative_coords, kicks):
            self.tetrimino.rotate_state = (self.tetrimino.rotate_state - 1) % 4

    def kick_tetrimino(self, new_relative_coords: list, kicks: list) -> bool:
        """
        Checks each set of kicks to see where rotated tetrimino can be placed

        Returns:
            bool: True if the tetrimino is successfully rotated and placed;
                  False otherwise
        """
        if self.tetrimino is None:
            return False

        # loop through each kick to see if any are successful
        for kick_x, kick_y in kicks:
            can_rotate = True
            for rel_x, rel_y in new_relative_coords:
                if not self.grid.is_available(
                    self.tetrimino.x + kick_x + rel_x,
                    self.tetrimino.y + kick_y + rel_y
                ):
                    can_rotate = False

            # rotate tetrimino if kick is successful
            if can_rotate:
                self.tetrimino.update_position_and_coords(
                    kick_x, kick_y, new_relative_coords
                )
                break

        return can_rotate

    def place_tetrimino_on_grid(self) -> None:
        """
        Places the current Tetrimino on the grid.
        """
        assert self.tetrimino is not None

        for x, y in self.tetrimino.absolute_coords:
            self.grid.set(x, y, self.tetrimino.color)

    def toggle_pause(self) -> None:
        self.paused = not self.paused
        if self.paused:
            self.gui.draw_pause()
