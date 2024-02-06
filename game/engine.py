import pygame
import config
from .gui import GUI

class GameEngine:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.gui = GUI(self.screen)
        self.running = True
        
    def run(self) -> None:
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.gui.draw_board()
            pygame.display.flip()
            pygame.time.Clock().tick(60) # Limit frames per second