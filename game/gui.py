import pygame
import config

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.Surface((config.BOARD_WIDTH, config.BOARD_HEIGHT)) # Surface containing tetris grid and grid border
        self.board_pos = (config.BOARD_X, config.BOARD_Y)
        self.grid_surface = pygame.Surface((config.GRID_WIDTH, config.GRID_HEIGHT)) # Surface for Tetris grid
        self.grid_surface_pos = (config.GRID_BORDER_WIDTH, config.GRID_BORDER_WIDTH)

    def draw_board(self):
        """Draws Tetris grid on the screen with a border.
        """
        self.board.fill(config.GRID_BORDER_COLOR)
        self.draw_grid()
        self.screen.blit(self.board, self.board_pos)


    def draw_grid(self):
        """Draws Tetris grid on the board surface.
        """
        # Draw vertical grid lines
        self.grid_surface.fill(config.GRID_BACKGROUND_COLOR)
        for i in range(config.GRID_COLS):
            x = i * config.CELL_SIZE
            pygame.draw.line(self.grid_surface,
                             color=config.GRID_LINE_COLOR,
                             start_pos=(x, 0),
                             end_pos=(x, config.GRID_HEIGHT),
                             width=config.GRID_LINE_WIDTH)

         # Draw horizontal grid lines
        for j in range(config.GRID_ROWS):
            y = j * config.CELL_SIZE
            pygame.draw.line(self.grid_surface,
                             color=config.GRID_LINE_COLOR,
                             start_pos=(0, y),
                             end_pos=(config.GRID_WIDTH, y),
                             width=config.GRID_LINE_WIDTH)

        self.board.blit(self.grid_surface, self.grid_surface_pos)