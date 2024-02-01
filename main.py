import tkinter as tk

NUM_GRID_ROWS = 20
NUM_GRID_COLS = 10
BLOCK_SIZE = 30

GRID_BACKGROUND_COLOR = "black"
GRID_LINE_COLOR = "#242424"
GRID_LINE_WIDTH = 1

TIMEOUT = 1


def main():
    # Initialise the main game window
    root = tk.Tk()
    root.geometry('800x600')
    root.title = ("Tetris")


    # Create the playing grid canvas
    play_grid = tk.Canvas(master=root, 
                        width=NUM_GRID_COLS * BLOCK_SIZE,
                        height=NUM_GRID_ROWS * BLOCK_SIZE,
                        bg=GRID_BACKGROUND_COLOR)
    play_grid.pack(anchor=tk.CENTER, expand=True)


    # Draw vertical grid lines
    for i in range(NUM_GRID_COLS):
        x = i * BLOCK_SIZE
        play_grid.create_line((x, 0), 
                                (x, NUM_GRID_ROWS * BLOCK_SIZE),
                                width=GRID_LINE_WIDTH,
                                fill=GRID_LINE_COLOR)
    
    # Draw horizontal grid lines
    for j in range(NUM_GRID_ROWS):
        y = j * BLOCK_SIZE
        play_grid.create_line((0, y), 
                                (NUM_GRID_COLS * BLOCK_SIZE, y),
                                width=GRID_LINE_WIDTH,
                                fill=GRID_LINE_COLOR)

    root.mainloop() # Start the Tkinter event loop


if __name__ == '__main__':
    main()