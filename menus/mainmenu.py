import json
import os
import pygame
import subprocess


class MainMenu:
    def __init__(self, game):
        self.game = game

        self.options = [
            ("Play", self.play),
            ("Settings", self.settings),
            ("Tutorial", self.tutorial),
            ("Exit", self.exit)
        ]

        self.choice = 0

    def render(self, key):
        # Background Image
        self.game.screen.blit(self.game.background_image, (0, 0))

        # Title
        label_title = self.game.font.render("Welcome to pymania", True, self.game.color)
        self.game.screen.blit(label_title, (50, 230))

        # Selection Arrow
        label_arrow = self.game.font.render(">", True, self.game.color)
        self.game.screen.blit(label_arrow, (800, 300 + 100 * self.choice))

        # Options
        for i, option in enumerate(self.options):
            text, handler = option

            label_option = self.game.font.render(text, True, self.game.color)

            self.game.screen.blit(label_option, (850, 300 + 100 * i))

        # Move selection arrow
        if key == "down" and self.choice < len(self.options) - 1:
            self.choice += 1

        elif key == "up" and self.choice > 0:
            self.choice -= 1

        elif key == "enter":
            text, handler = self.options[self.choice]
            handler()

        # Update Display
        pygame.display.flip()

    def play(self):
        # Song Selection Menu
        self.game.songselect_handler()

    def settings(self):
        # TODO: Add other OS compatibility & Create GUI
        if not os.path.exists('./settings.txt'):
            default = '{"fullscreen":False}'
            json.dump(default, open('./settings.txt'))
        else:
            subprocess.run(["notepad", "settings.txt"])

    def tutorial(self):
        # Tutorial
        self.game.tutorial_handler()

    def exit(self):
        pygame.quit()
        exit()
