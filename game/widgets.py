import pygame

class Button():
    def __init__(self, image_path, position, size, active, on_click_function):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.position = position
        self.active = active
        self.rect = self.image.get_rect(topleft=position)
        self.on_click_function = on_click_function

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False

    def on_click(self):
        self.on_click_function()