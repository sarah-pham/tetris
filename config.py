# Display settings
SCREEN_WIDTH = 600 # Width of the entire game screen (pixels)
SCREEN_HEIGHT = 800 # Height of the entire game screen (pixels)

# Tetris grid configuration
GRID_ROWS = 20 # Number of rows in the Tetris grid
GRID_COLS = 10 # Number of columns in the Tetris grid
CELL_SIZE = 30 # Size of each cell within the grid (pixels)
GRID_LINE_WIDTH = 1 # Width of the grid lines (pixels)
GRID_BORDER_WIDTH = 3 # Width of the border around the Tetris grid (pixels)

# Calculated grid size
GRID_WIDTH = GRID_COLS * CELL_SIZE # Total width of grid (pixels)
GRID_HEIGHT = GRID_ROWS * CELL_SIZE # Total height of grid (pixels)
BOARD_WIDTH = GRID_WIDTH + (2 * GRID_BORDER_WIDTH) # Total width of grid with border (pixels)
BOARD_HEIGHT = GRID_HEIGHT + (2 * GRID_BORDER_WIDTH) # Total height of grid with border (pixels)

# Board position
BOARD_X = (SCREEN_WIDTH - BOARD_WIDTH)/2
BOARD_Y = (SCREEN_HEIGHT - BOARD_HEIGHT)/2

# Grid colors
GRID_BACKGROUND_COLOR = (0, 0, 0) # Color of the Tetris grid background
GRID_LINE_COLOR = (36, 36, 36) # Color of the grid lines
GRID_BORDER_COLOR = GRID_LINE_COLOR # Colour of Tetris grid border

# Tetrimino configuration
TETRIMINO_START_COLUMN = 3 # Initial grid column of new tetriminos