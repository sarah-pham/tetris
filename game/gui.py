import pygame
from pygame import draw, display, SRCALPHA
from pygame import Surface, Rect
from config import (
    BOARD_WIDTH,
    BOARD_HEIGHT,
    BOARD_X,
    BOARD_Y,
    GRID_WIDTH,
    GRID_HEIGHT,
    GRID_LINE_WIDTH,
    GRID_BORDER_WIDTH,
    GRID_BORDER_COLOR,
    GRID_LINE_COLOR,
    GRID_BACKGROUND_COLOR,
    GRID_COLS,
    GRID_ROWS,
    BLOCK_SIZE,
    PAUSE_MASK_COLOR,
    PAUSE_MASK_ALPHA,
    TITLE_X,
    TITLE_Y,
)


class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.board = Surface((BOARD_WIDTH, BOARD_HEIGHT))  # Surface for tetris grid and border
        self.board_pos = (BOARD_X, BOARD_Y)
        self.grid_surface = Surface((GRID_WIDTH, GRID_HEIGHT))  # Surface for Tetris grid
        self.grid_surface_pos = (GRID_BORDER_WIDTH, GRID_BORDER_WIDTH)
        self.load_images()

    def load_images(self):
        self.graphics = {}
        self.graphics["title"] = pygame.image.load('assets/images/title.png')

    def draw_board(self, grid):
        """
        Draws Tetris grid on the screen with a border.
        """
        self.board.fill(GRID_BORDER_COLOR)
        self.draw_grid(grid)
        self.draw_title()

    def draw_grid(self, grid):
        """
        Draws Tetris grid on the board surface.
        """
        self.grid_surface.fill(GRID_BACKGROUND_COLOR)

        # Draw cells in grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != None:
                    self.draw_block(x, y, grid[y][x])

    def draw_gridlines(self):
        # Draw vertical grid lines
        for i in range(GRID_COLS):
            x = i * BLOCK_SIZE
            draw.line(self.grid_surface, GRID_LINE_COLOR, (x, 0), (x, GRID_HEIGHT), GRID_LINE_WIDTH)

        # Draw horizontal grid lines
        for j in range(GRID_ROWS):
            y = j * BLOCK_SIZE
            draw.line(self.grid_surface, GRID_LINE_COLOR, (0, y), (GRID_WIDTH, y), GRID_LINE_WIDTH)

    def draw_block(self, x: int, y: int, color) -> None:
        """
        Draws a square at (x, y) which has length BLOCK_SIZE and given color.
        """
        draw.rect(
            self.grid_surface,
            color=color,
            rect=Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        )

    def draw_title(self):
        self.screen.blit(self.graphics['title'], (TITLE_X, TITLE_Y));

    def draw_pause(self) -> None:
        """
        Draws a semi-transparent overlay on the grid and updates the display.
        """
        mask = Surface(self.grid_surface.get_size(), SRCALPHA)
        mask.fill(PAUSE_MASK_COLOR)
        mask.set_alpha(PAUSE_MASK_ALPHA)
        self.grid_surface.blit(mask, (0, 0))
        self.update_display()

    def update_display(self) -> None:
        """
        Blits the grid and board surfaces onto the main screen and refreshes the display.
        """
        self.board.blit(self.grid_surface, self.grid_surface_pos)
        self.screen.blit(self.board, self.board_pos)
        display.flip()