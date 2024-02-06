import pygame
import config

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.grid = pygame.Surface((config.GRID_WIDTH, config.GRID_HEIGHT))
        self.grid_center = ((config.SCREEN_WIDTH-config.GRID_WIDTH)/2,
                                 (config.SCREEN_HEIGHT-config.GRID_HEIGHT)/2)

    def draw_grid(self):
        # Draw vertical grid lines
        self.grid.fill(config.GRID_BACKGROUND_COLOR)
        for i in range(config.GRID_COLS + 1):
            x = i * config.BLOCK_SIZE
            if x == config.GRID_WIDTH:
                x -= 1 # Ensure that line is drawn within surface boundaries
            pygame.draw.line(self.grid,
                             color=config.GRID_LINE_COLOR,
                             start_pos=(x, 0),
                             end_pos=(x, config.GRID_HEIGHT),
                             width=config.GRID_LINE_WIDTH)

         # Draw horizontal grid lines
        for j in range(config.GRID_ROWS + 1):
            y = j * config.BLOCK_SIZE
            if y == config.GRID_HEIGHT:
                y -= 1 # Ensure that line is drawn within surface boundaries
            pygame.draw.line(self.grid,
                             color=config.GRID_LINE_COLOR,
                             start_pos=(0, y),
                             end_pos=(config.GRID_WIDTH, y),
                             width=config.GRID_LINE_WIDTH)

        self.screen.blit(self.grid, self.grid_center)