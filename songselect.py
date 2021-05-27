import os

import pygame


class SongSelect:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(os.path.join('resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.background_image = pygame.image.load(os.path.join('resources', 'img', 'background.jpg')).convert()

    def render(self):
        self.game.screen.blit(self.background_image, (0, 0))



