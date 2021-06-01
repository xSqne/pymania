import os
import pygame


class SongSelect:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(os.path.join('./resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.background_image = pygame.image.load(os.path.join('./resources', 'img', 'background.jpg')).convert()

        self.choice = 0

        self.songs = [
            ("Song 1", self.song),
            ("Song 2", self.song),
            ("Song 3", self.song)
        ]

    def render(self, key):
        self.game.screen.blit(self.background_image, (0, 0))

        arrow = self.font.render(">", False, (0, 0, 0))

        for i, option in enumerate(self.songs):
            text, handler = option

            song = self.font.render(text, False, (0, 0, 0))
            self.game.screen.blit(song, (1000, 300 + 100 * i))
        if key == "down" and self.choice < 2:
            self.choice += 1

        elif key == "up" and self.choice > 0:
            self.choice -= 1

        elif key == "enter":
            text, handler = self.songs[self.choice]
            handler(self.choice)

        self.game.screen.blit(arrow, (900, 300 + 100 * self.choice))

        pygame.display.flip()

    def song(self, song):
        self.game.game_handler(song)

