import os
import pygame

from menus import mainmenu, songselect, stagerandom, end, tutorial


class Game:
    def __init__(self):
        pygame.init()
        # Setting resolution
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Clock & 240 fps
        self.clock = pygame.time.Clock()
        self.clock.tick(240)

        # Background & Font & Color
        self.titlefont = pygame.font.Font(os.path.join('./resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.textfont = pygame.font.Font(os.path.join('./resources', 'fonts', 'Aller_Lt.ttf'), 32)
        self.background_image = pygame.image.load(os.path.join('./resources', 'img', 'background.jpg')).convert()
        self.color = (0, 128, 255)

        # Instantiating menu classes
        self.mm = mainmenu.MainMenu(self)
        self.ss = songselect.SongSelect(self)
        self.sr = stagerandom.StageRandom(self)
        self.e = end.End(self)
        self.t = tutorial.Tutorial(self)

        # Finished initializing
        self.game_running = True

        # Set state to Main Menu
        self.currentstate = "Main Menu"

        # Define accuracy
        self.accuracy = 100

    # Function for handling events
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
                if event.key == pygame.K_ESCAPE:
                    return "esc"

    def mainmenu_handler(self):
        self.currentstate = "Main Menu"

    def tutorial_handler(self):
        self.currentstate = "Tutorial"

    def songselect_handler(self):
        self.currentstate = "Song Select"

    def game_handler(self):
        self.currentstate = "Game"

    def end_handler(self, accuracy):
        self.currentstate = "End"
        self.accuracy = accuracy
