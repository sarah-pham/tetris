import pygame
import random
import time
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    DROP_INTERVAL,
    SINGLE_LINE_CLEAR_PTS,
    DOUBLE_LINE_CLEAR_PTS,
    TRIPLE_LINE_CLEAR_PTS,
    FOUR_LINE_CLEAR_PTS,
    TETRIMINO_SHADOW_COLOR,
)
from .grid import Grid
from .tetrimino import (
    Tetrimino,
    TETRIMINO_CLASSES
)
from .gui import GUI
from .event_handler import Action, EventHandler


class GameEngine:
    def __init__(self) -> None:
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.event_handler = EventHandler()
        self.grid = Grid()

        self.active_game = False
        self.paused = False
        self.tetrimino = None
        self.points = 0

        self.tetrimino_action_map = {
            Action.LEFT: self.move_tetrimino_left,
            Action.RIGHT: self.move_tetrimino_right,
            Action.DOWN: self.handle_soft_drop,
            Action.DROP: self.handle_hard_drop,
            Action.ROTATE_RIGHT: self.rotate_right,
            Action.ROTATE_LEFT: self.rotate_left,
            Action.START: self.reset_game
        }

        print("Press RETURN to start :)")

    def run(self) -> None:
        while self.running:
            self.handle_events()
            if not self.paused:
                if self.active_game:
                    self.update_game_state()
                self.draw_game_state()
            pygame.time.Clock().tick(FPS)

    def handle_events(self):
        for action in self.event_handler.get_actions():
            if action == Action.QUIT:
                self.handle_quit_game()
            elif action == Action.TOGGLE_PAUSE:
                self.toggle_pause()
            elif action in self.tetrimino_action_map:
                if action == Action.START:
                    if not self.active_game:
                        self.tetrimino_action_map[action]()
                elif not self.paused and self.tetrimino is not None:
                    self.tetrimino_action_map[action]()

    def handle_quit_game(self) -> None:
        self.running = False

    def update_game_state(self) -> None:
        if self.tetrimino is None:
            self.generate_tetrimino()

        self.handle_automatic_dropping()
        self.update_tetrimino_shadow()
        self.check_and_handle_game_over()

    def reset_game(self) -> None:
        """
        Resets the game state to start a new session.
        """
        self.active_game = True
        self.paused = False
        self.generate_tetrimino()
        self.tetrimino_shadow_coords = []
        self.last_drop_time = time.time()
        self.points = 0

    def handle_automatic_dropping(self) -> None:
        if self.tetrimino is None:
            return

        if time.time() - self.last_drop_time >= DROP_INTERVAL:
            move_success = self.move_tetrimino_down()
            if not move_success:
                self.handle_lock_tetrimino()
            self.last_drop_time = time.time()

    def draw_game_state(self) -> None:
        """
        Renders the current game state on the GUI.
        """
        # Draw the Tetris grid with existing blocks
        self.gui.draw_board(self.grid.grid)

        # Overlay the current tetrimino and show on the grid
        if self.tetrimino is not None:
            for x, y in self.tetrimino_shadow_coords:
                self.gui.draw_block(x, y, TETRIMINO_SHADOW_COLOR)

            for x, y in self.tetrimino.absolute_coords:
                self.gui.draw_block(x, y, self.tetrimino.color)

        self.gui.draw_gridlines()
        self.gui.draw_points(self.points)

        # Update the display
        self.gui.update_display()

    def generate_tetrimino(self) -> None:
        """
        Returns a Tetrimino instance of a randomly selected class.
        """
        RandomTetriminoClass = random.choice(TETRIMINO_CLASSES)
        self.tetrimino = RandomTetriminoClass()
        self.drop_points = 0

    def check_and_handle_game_over(self) -> None:
        """
        Checks and handles game over.
        """
        if self.tetrimino is not None:
            return

        if self.check_game_over():
            self.active_game = False
            self.grid = Grid()
            print("You lose! Press RETURN to start a new game :)")

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
        assert self.tetrimino is not None

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
        self.tetrimino_drop_distance = 0
        while self.move_tetrimino_down():
            self.drop_points += 2
            continue

    def handle_soft_drop(self) -> None:
        self.move_tetrimino_down()
        self.drop_points += 1

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

    def toggle_pause(self) -> None:
        self.paused = not self.paused
        if self.paused:
            self.gui.draw_pause()

    def handle_lock_tetrimino(self) -> None:
        assert self.tetrimino is not None

        for x, y in self.tetrimino.absolute_coords:
            self.grid.set(x, y, self.tetrimino.color)

        y_coords = set(y for _, y in self.tetrimino.absolute_coords)
        lines_cleared = 0

        for y in y_coords:
            if self.grid.check_row_full(y):
                self.grid.clear_line(y)
                lines_cleared += 1

        # Add points for line clears
        if lines_cleared == 1:
            self.points += SINGLE_LINE_CLEAR_PTS
        elif lines_cleared == 2:
            self.points += DOUBLE_LINE_CLEAR_PTS
        elif lines_cleared == 3:
            self.points += TRIPLE_LINE_CLEAR_PTS
        elif lines_cleared == 4:
            self.points += FOUR_LINE_CLEAR_PTS

        # Add points for soft/ hard drop
        if lines_cleared > 0:
            self.points += self.drop_points

        self.tetrimino = None

    def update_tetrimino_shadow(self) -> None:
        if self.tetrimino is None:
            return

        distance = 0

        can_move_down = True
        while can_move_down:
            for x, y in self.tetrimino.absolute_coords:
                if not self.grid.is_available(x, y + distance + 1):
                    can_move_down = False

            if can_move_down:
                distance += 1

        self.tetrimino_shadow_coords = [[x, y + distance] for x, y in self.tetrimino.absolute_coords]