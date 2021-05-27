import pygame
from mainmenu import MainMenu
from songselect import SongSelect


class Game:
    def __init__(self):
        pygame.init()

        # Setting Resolution
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Clock
        self.clock = pygame.time.Clock()

        self.mm = MainMenu(self)
        self.ss = SongSelect(self)

        # Finished Initializing
        self.game_running = True

        self.currentstate = "Main Menu"

    def events(self):
        for event in pygame.event.get():
            # Closing if pressed X on the game window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "up"
                if event.key == pygame.K_DOWN:
                    return "down"
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return "enter"

    def mainmenu_handler(self, key):
        self.currentstate = "Main Menu"
        self.mm.render(key)

    def songselect_handler(self):
        self.currentstate = "Song Select"
        self.ss.render()

    def game_handler(self):
        pass





