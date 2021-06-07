import os

import pygame


class Game:
    def __init__(self):
        pygame.init()

        # Setting Resolution
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Clock & 60 fps
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        # Background & Font
        self.font = pygame.font.Font(os.path.join('./resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.background_image = pygame.image.load(os.path.join('./resources', 'img', 'background.jpg')).convert()

        # Finished Initializing
        self.game_running = True

        # Set Menu to Main Menu
        self.currentstate = "Main Menu"

        self.song = 0

    def events(self):
        for event in pygame.event.get():
            # Closing if pressed X on the game window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "up"
                if event.key == pygame.K_DOWN:
                    return "down"
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return "enter"
                if event.key == pygame.K_d:
                    return "d"
                if event.key == pygame.K_f:
                    return "f"
                if event.key == pygame.K_j:
                    return "j"
                if event.key == pygame.K_k:
                    return "k"

    def mainmenu_handler(self):
        self.currentstate = "Main Menu"

    def songselect_handler(self):
        self.currentstate = "Song Select"

    def game_handler(self, song):
        self.currentstate = "Game"
        self.song = song





