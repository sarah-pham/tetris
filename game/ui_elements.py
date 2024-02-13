import pygame

class Button:
    def __init__(self, image_path, position, on_click_function):
        self.image = pygame.image.load(image_path)
        self.position = position
        self.rect = self.image.get_rect(topleft=position)
        self.on_click_function = on_click_function

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def on_click(self):
        self.on_click_function()