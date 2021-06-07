import pygame


class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((65, 25))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)