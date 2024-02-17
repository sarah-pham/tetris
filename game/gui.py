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
    TITLE_HEIGHT,
    TITLE_WIDTH,
    PAUSED_WIDTH,
    PAUSED_HEIGHT,
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
        """
        Loads external images into games. Images are saved in 2 lists:
            - active_images = for images to be drawn during gameplay
            - paused_images = for images to be drawn when game is paused
        Images are saved as a tuple (image, position)
        """
        self.load_active_images()
        self.load_paused_images()

    def load_active_images(self):
        self.active_images = [] # images to be drawn when game is active

        # Load and save title image and position
        title_image = pygame.image.load("assets/images/title.png")
        title_image = pygame.transform.scale(title_image, (TITLE_WIDTH, TITLE_HEIGHT))
        title_image_position = (
            (BOARD_WIDTH - TITLE_WIDTH) / 2 + BOARD_X,
            (BOARD_Y - TITLE_HEIGHT) / 2
        )
        self.active_images.append((title_image, title_image_position))

    def load_paused_images(self):
        self.paused_images = [] # images to be drawn when game is paused

        # Load and save 'paused' image and position
        paused_image = pygame.image.load("assets/images/paused.png")
        paused_image = pygame.transform.scale(paused_image, (PAUSED_WIDTH, PAUSED_HEIGHT))
        paused_image_position = (
            (BOARD_WIDTH - PAUSED_WIDTH) / 2,
            (BOARD_HEIGHT) / 4
        )
        self.paused_images.append((paused_image, paused_image_position))

    def draw_board(self, grid):
        """
        Draws Tetris grid on the screen with a border.
        """
        self.board.fill(GRID_BORDER_COLOR)
        self.draw_grid(grid)

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

    def draw_game_images(self):
        """
        Draws images loaded from files.
        Images are saved as tuples in the format (image, position)
        """
        for img in self.active_images:
            self.screen.blit(img[0], img[1])

    def draw_pause(self) -> None:
        """
        Draws a semi-transparent overlay on the grid and updates the display.
        """
        mask = Surface(self.grid_surface.get_size(), SRCALPHA)
        mask.fill(PAUSE_MASK_COLOR)
        mask.set_alpha(PAUSE_MASK_ALPHA)
        self.grid_surface.blit(mask, (0, 0))
        self.draw_paused_elements()
        self.update_display()

    def draw_paused_elements(self) -> None:
        for img in self.paused_images:
            self.grid_surface.blit(img[0], img[1])

    def update_display(self) -> None:
        """
        Blits the grid and board surfaces onto the main screen and refreshes the display.
        """
        self.board.blit(self.grid_surface, self.grid_surface_pos)
        self.screen.blit(self.board, self.board_pos)
        display.flip()