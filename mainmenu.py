import os.path
import pygame


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(os.path.join('resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.background_image = pygame.image.load(os.path.join('resources', 'img', 'background.jpg')).convert()

        self.options = [
            ("Play", self.play),
            ("Settings", self.settings),
            ("Exit", self.exit)
        ]

        self.choice = 0

    def render(self, key):
        if key == "down" and self.choice < len(self.options) - 1:
            self.choice += 1

        elif key == "up" and self.choice > 0:
            self.choice -= 1

        elif key == "enter":
            text, handler = self.options[self.choice]
            handler()

        self.game.screen.blit(self.background_image, (0, 0))

        label_title = self.font.render("Welcome to pymania", False, (0, 0, 0))
        label_arrow = self.font.render(">", False, (0, 0, 0))

        self.game.screen.blit(label_title, (100, 230))

        for i, option in enumerate(self.options):
            text, handler = option

            label_option = self.font.render(text, False, (0, 0, 0))

            self.game.screen.blit(label_option, (850, 300 + 100 * i))

        self.game.screen.blit(label_arrow, (800, 300 + 100 * self.choice))

        pygame.display.flip()

    def play(self):
        self.game.songselect_handler()

    def settings(self):
        pass

    def exit(self):
        pygame.quit()
        exit()
