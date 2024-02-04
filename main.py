import pygame

GRID_ROWS = 20
GRID_COLS = 10
BLOCK_SIZE = 30

GRID_BACKGROUND_COLOR = (0, 0, 0)
GRID_LINE_COLOR = (36, 36, 36)
GRID_LINE_WIDTH = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOARD_WIDTH = GRID_COLS * BLOCK_SIZE
BOARD_HEIGHT = GRID_ROWS * BLOCK_SIZE

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    
    play_grid = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
    play_grid.fill(GRID_BACKGROUND_COLOR)
    play_grid_center = (
        (SCREEN_WIDTH-BOARD_WIDTH)/2,
        (SCREEN_HEIGHT-BOARD_HEIGHT)/2
    )

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw vertical grid lines
        for i in range(GRID_COLS):
            x = i * BLOCK_SIZE
            pygame.draw.line(play_grid, GRID_LINE_COLOR, (x, 0), (x, BOARD_HEIGHT), GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, GRID_LINE_COLOR, (BOARD_WIDTH-1, 0), (BOARD_WIDTH-1, BOARD_HEIGHT), GRID_LINE_WIDTH)
        
        # Draw horizontal grid lines
        for j in range(GRID_ROWS + 1):
            y = j * BLOCK_SIZE
            pygame.draw.line(play_grid, GRID_LINE_COLOR, (0, y), (BOARD_WIDTH, y), GRID_LINE_WIDTH)
        pygame.draw.line(play_grid, GRID_LINE_COLOR, (0, BOARD_HEIGHT-1), (BOARD_WIDTH, BOARD_HEIGHT-1), GRID_LINE_WIDTH)

        # Update the display
        screen.blit(play_grid, play_grid_center)
        pygame.display.flip()
        
        # Limit frames per second
        pygame.time.Clock().tick(60)

    pygame.quit()
    

if __name__ == '__main__':
    main()