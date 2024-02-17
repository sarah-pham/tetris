import pygame

class Button():
    def __init__(self, image_path, position, size, draw_on_active):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.position = position
        self.draw_on_active = draw_on_active
        self.rect = self.image.get_rect(topleft=position)

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False

    def on_click(self):
        self.on_click_function()