import pygame
import config

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.play_grid = pygame.Surface((config.BOARD_WIDTH, config.BOARD_HEIGHT))
        self.play_grid_center = ((config.SCREEN_WIDTH-config.BOARD_WIDTH)/2, 
                                 (config.SCREEN_HEIGHT-config.BOARD_HEIGHT)/2)

    def draw_grid(self):
        # Draw vertical grid lines
        self.play_grid.fill(config.GRID_BACKGROUND_COLOR)
        for i in range(config.GRID_COLS):
            x = i * config.BLOCK_SIZE
            pygame.draw.line(self.play_grid, config.GRID_LINE_COLOR, (x, 0), (x, config.BOARD_HEIGHT), config.GRID_LINE_WIDTH)
        pygame.draw.line(self.play_grid, config.GRID_LINE_COLOR, (config.BOARD_WIDTH-1, 0), (config.BOARD_WIDTH-1, config.BOARD_HEIGHT), config.GRID_LINE_WIDTH)

         # Draw horizontal grid lines
        for j in range(config.GRID_ROWS + 1):
            y = j * config.BLOCK_SIZE
            pygame.draw.line(self.play_grid, config.GRID_LINE_COLOR, (0, y), (config.BOARD_WIDTH, y), config.GRID_LINE_WIDTH)
        pygame.draw.line(self.play_grid, config.GRID_LINE_COLOR, (0, config.BOARD_HEIGHT-1), (config.BOARD_WIDTH, config.BOARD_HEIGHT-1), config.GRID_LINE_WIDTH)

        self.screen.blit(self.play_grid, self.play_grid_center)
