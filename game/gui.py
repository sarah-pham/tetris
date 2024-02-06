import pygame
from config import BOARD_WIDTH, BOARD_HEIGHT, BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, GRID_LINE_WIDTH, GRID_BORDER_WIDTH, GRID_BORDER_COLOR, GRID_LINE_COLOR, GRID_BACKGROUND_COLOR, GRID_COLS, GRID_ROWS, CELL_SIZE

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT)) # Surface containing tetris grid and grid border
        self.board_pos = (BOARD_X, BOARD_Y)
        self.grid_surface = pygame.Surface((GRID_WIDTH, GRID_HEIGHT)) # Surface for Tetris grid
        self.grid_surface_pos = (GRID_BORDER_WIDTH, GRID_BORDER_WIDTH)

    def draw_board(self, grid):
        """Draws Tetris grid on the screen with a border.
        """
        self.board.fill(GRID_BORDER_COLOR)
        self.draw_grid(grid)
        self.screen.blit(self.board, self.board_pos)

    def draw_grid(self, grid):
        """Draws Tetris grid on the board surface.
        """
        self.grid_surface.fill(GRID_BACKGROUND_COLOR)

        # Draw cells in grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != None:
                    self.draw_cell(row, col, grid[row][col])

        self.draw_gridlines()
        self.board.blit(self.grid_surface, self.grid_surface_pos)

    def draw_gridlines(self):
        # Draw vertical grid lines
        for i in range(GRID_COLS):
            x = i * CELL_SIZE
            pygame.draw.line(self.grid_surface,
                             color=GRID_LINE_COLOR,
                             start_pos=(x, 0),
                             end_pos=(x, GRID_HEIGHT),
                             width=GRID_LINE_WIDTH)

         # Draw horizontal grid lines
        for j in range(GRID_ROWS):
            y = j * CELL_SIZE
            pygame.draw.line(self.grid_surface,
                             color=GRID_LINE_COLOR,
                             start_pos=(0, y),
                             end_pos=(GRID_WIDTH, y),
                             width=GRID_LINE_WIDTH)

    def draw_cell(self, row: int, col: int, color):
        """Draws a square cell with given color at the specified grid row and column
        """
        pygame.draw.rect(self.grid_surface,
                         color=color,
                         rect=pygame.Rect((col * CELL_SIZE, row * CELL_SIZE),
                                          (CELL_SIZE, CELL_SIZE))
        )