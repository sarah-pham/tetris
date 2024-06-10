import os
AUTO_RESTART = os.getenv('AUTO_RESTART', 'false').lower() == 'true'

# Display settings
SCREEN_WIDTH = 600 # Width of the entire game screen (pixels)
SCREEN_HEIGHT = 800 # Height of the entire game screen (pixels)
FPS = 60 # Frame rate per second limit

# Tetris grid configuration
GRID_ROWS = 20 # Number of rows in the Tetris grid
GRID_COLS = 10 # Number of columns in the Tetris grid
BLOCK_SIZE = 30 # Size of each block within the grid (pixels)
GRID_LINE_WIDTH = 1 # Width of the grid lines (pixels)
GRID_BORDER_WIDTH = 5 # Width of the border around the Tetris grid (pixels)

# Calculated grid size
GRID_WIDTH = GRID_COLS * BLOCK_SIZE # Total width of grid (pixels)
GRID_HEIGHT = GRID_ROWS * BLOCK_SIZE # Total height of grid (pixels)
BOARD_WIDTH = GRID_WIDTH + (2 * GRID_BORDER_WIDTH) # Total width of grid with border (pixels)
BOARD_HEIGHT = GRID_HEIGHT + (2 * GRID_BORDER_WIDTH) # Total height of grid with border (pixels)

# Board position
BOARD_X = (SCREEN_WIDTH - BOARD_WIDTH)/2
BOARD_Y = (SCREEN_HEIGHT - BOARD_HEIGHT)/2

# Grid colors
GRID_BACKGROUND_COLOR = (0, 0, 0) # Color of the Tetris grid background
GRID_LINE_COLOR = (36, 36, 36) # Color of the grid lines
GRID_BORDER_COLOR = GRID_LINE_COLOR # Colour of Tetris grid border

# config.py
PAUSE_MASK_COLOR = (150, 150, 150)
PAUSE_MASK_ALPHA = 110

# Tetrimino configuration
TETRIMINO_START_COLUMN = 3 # Initial grid column of new tetriminos
DROP_INTERVAL = 0.5 # Time taken in seconds for tetrimino to drop down by 1 position
INTIAL_REPEAT_INTERVAL = 0.19 # Delay between the first and second pygame.KEYDOWN events when keys are held down (seconds)
REPEAT_INTERVAL = 0.11 # Time interval between pygame.KEYDOWN events when keys are held down (seconds)

# Graphics
TITLE_HEIGHT = 50 # Height of TETRIS Title on screen (in pixels)
TITLE_WIDTH = 330 # Width of TETRIS Title on screen (in pixels)
PAUSED_ASPECT_RATIO = 6.5 # Aspect ratio of PAUSED graphic
PAUSED_HEIGHT = 30 # Height of PAUSED graphic (in pixels)
PAUSED_WIDTH = PAUSED_HEIGHT * PAUSED_ASPECT_RATIO # Width of PAUSED graphic (in pixels)

# Points for clearing lines
SINGLE_LINE_CLEAR_PTS = 40
DOUBLE_LINE_CLEAR_PTS = 100
TRIPLE_LINE_CLEAR_PTS = 300
FOUR_LINE_CLEAR_PTS = 1200