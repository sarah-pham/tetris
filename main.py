import pygame
import config

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    
    play_grid = pygame.Surface((config.BOARD_WIDTH, config.BOARD_HEIGHT))
    play_grid.fill(config.GRID_BACKGROUND_COLOR)
    play_grid_center = (
        (config.SCREEN_WIDTH-config.BOARD_WIDTH)/2,
        (config.SCREEN_HEIGHT-config.BOARD_HEIGHT)/2
    )

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw vertical grid lines
        for i in range(config.GRID_COLS):
            x = i * config.BLOCK_SIZE
            pygame.draw.line(play_grid, config.GRID_LINE_COLOR, (x, 0), (x, config.BOARD_HEIGHT), config.GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, config.GRID_LINE_COLOR, (config.BOARD_WIDTH-1, 0), (config.BOARD_WIDTH-1, config.BOARD_HEIGHT), config.GRID_LINE_WIDTH)
        
        # Draw horizontal grid lines
        for j in range(config.GRID_ROWS + 1):
            y = j * config.BLOCK_SIZE
            pygame.draw.line(play_grid, config.GRID_LINE_COLOR, (0, y), (config.BOARD_WIDTH, y), config.GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, config.GRID_LINE_COLOR, (0, config.BOARD_HEIGHT-1), (config.BOARD_WIDTH, config.BOARD_HEIGHT-1), config.GRID_LINE_WIDTH)

        # Update the display
        screen.blit(play_grid, play_grid_center)
        pygame.display.flip()
        
        # Limit frames per second
        pygame.time.Clock().tick(60)

    pygame.quit()
    

if __name__ == '__main__':
    main()