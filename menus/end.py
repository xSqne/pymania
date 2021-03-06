import pygame


class End:
    def __init__(self, game):
        self.game = game

    def render(self, event):
        # Background Image
        self.game.screen.blit(self.game.background_image, (0, 0))

        # Good Job text
        goodjob_text = self.game.titlefont.render("Great Job!", True, self.game.color)
        self.game.screen.blit(goodjob_text, (50, 230))

        # Esc text 1
        esc_text = self.game.titlefont.render("Press Esc to go back", True, self.game.color)
        self.game.screen.blit(esc_text, (50, 325))

        # Esc text 2
        esc_text = self.game.titlefont.render("to the Main Menu", True, self.game.color)
        self.game.screen.blit(esc_text, (50, 400))

        # Accuracy text
        acc_text = self.game.titlefont.render("Accuracy: " + str(self.game.accuracy) + "%", True, self.game.color)
        self.game.screen.blit(acc_text, (800, 500))

        # Detect Esc key
        if event == "esc":
            self.game.mainmenu_handler()

        # Update display
        pygame.display.flip()
