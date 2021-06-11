import os
import pygame
import subprocess
import yaml


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
        label_title = self.game.titlefont.render("Welcome to pymania", True, self.game.color)
        self.game.screen.blit(label_title, (50, 230))

        # Selection Arrow
        label_arrow = self.game.titlefont.render(">", True, self.game.color)
        self.game.screen.blit(label_arrow, (800, 300 + 100 * self.choice))

        # Options
        for i, option in enumerate(self.options):
            text, handler = option

            label_option = self.game.titlefont.render(text, True, self.game.color)

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
        # Check if settings file exist
        if not os.path.exists('./settings.txt'):
            default = {
                "fullscreen": False,
                "fps": 60,
                "speed": 1
            }

            # Create new one
            with open('./settings.yml', "w") as f:
                f.write("# This is a YAML config file. Make sure to follow the format or the program will break!\n"
                        "# If you somehow misconfigure it, you can delete this file to generate a new one.\n"
                        "# For the changes to apply, please restart your game!\n\n")
                yaml.dump(default, f, indent=4, sort_keys=True)

            # Catch Errors just in case
            try:
                subprocess.run(["notepad", "./settings.json"])
            except Exception as e:
                print("An execption has occured. Please report this on our GitHub\n Execption:")
                print(e)
        else:
            try:
                subprocess.run(["notepad", "./settings.json"])
            except Exception as e:
                print("An execption has occured. Please report this on our GitHub\n Execption:")
                print(e)

    def tutorial(self):
        # Tutorial
        self.game.tutorial_handler()

    def exit(self):
        pygame.quit()
        exit()
