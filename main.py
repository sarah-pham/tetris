import pygame
import settings

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    
    play_grid = pygame.Surface((settings.BOARD_WIDTH, settings.BOARD_HEIGHT))
    play_grid.fill(settings.GRID_BACKGROUND_COLOR)
    play_grid_center = (
        (settings.SCREEN_WIDTH-settings.BOARD_WIDTH)/2,
        (settings.SCREEN_HEIGHT-settings.BOARD_HEIGHT)/2
    )

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw vertical grid lines
        for i in range(settings.GRID_COLS):
            x = i * settings.BLOCK_SIZE
            pygame.draw.line(play_grid, settings.GRID_LINE_COLOR, (x, 0), (x, settings.BOARD_HEIGHT), settings.GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, settings.GRID_LINE_COLOR, (settings.BOARD_WIDTH-1, 0), (settings.BOARD_WIDTH-1, settings.BOARD_HEIGHT), settings.GRID_LINE_WIDTH)
        
        # Draw horizontal grid lines
        for j in range(settings.GRID_ROWS + 1):
            y = j * settings.BLOCK_SIZE
            pygame.draw.line(play_grid, settings.GRID_LINE_COLOR, (0, y), (settings.BOARD_WIDTH, y), settings.GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, settings.GRID_LINE_COLOR, (0, settings.BOARD_HEIGHT-1), (settings.BOARD_WIDTH, settings.BOARD_HEIGHT-1), settings.GRID_LINE_WIDTH)

        # Update the display
        screen.blit(play_grid, play_grid_center)
        pygame.display.flip()
        
        # Limit frames per second
        pygame.time.Clock().tick(60)

    pygame.quit()
    

if __name__ == '__main__':
    main()