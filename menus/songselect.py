import pygame


class SongSelect:
    def __init__(self, game):
        self.game = game

        self.choice = 0

        self.songs = [
            ("Random Song", self.random_song),
            ("Song 1 (WIP)", self.song),
            ("Song 2 (WIP)", self.song)
        ]

    def render(self, key):
        # Background Image
        self.game.screen.blit(self.game.background_image, (0, 0))

        # Title Text 1
        select_text1 = self.game.font.render("Select a Song using", True, self.game.color)
        self.game.screen.blit(select_text1, (50, 230))

        # Title Text 2
        select_text2 = self.game.font.render("the arrow keys!", True, self.game.color)
        self.game.screen.blit(select_text2, (50, 300))

        # Selection Arrow
        arrow = self.game.font.render(">", True, self.game.color)
        self.game.screen.blit(arrow, (800, 400 + 100 * self.choice))

        # Song Options
        for i, option in enumerate(self.songs):
            text, handler = option
            song = self.game.font.render(text, True, self.game.color)
            self.game.screen.blit(song, (900, 400 + 100 * i))

        # Move selection arrow
        if key == "down" and self.choice < 2:
            self.choice += 1

        elif key == "up" and self.choice > 0:
            self.choice -= 1

        elif key == "enter":
            text, handler = self.songs[self.choice]
            handler()

        elif key == "esc":
            self.game.currentstate = "Main Menu"

        # Update Display
        pygame.display.flip()

    def random_song(self):
        # Game menu
        self.game.game_handler()

    def song(self):
        print("Work In Progress!")
        return

