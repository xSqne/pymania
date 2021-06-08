import os
import pygame


class Tutorial:
    def __init__(self, game):
        self.game = game

        # Load in images
        self.stage_left = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-left.png'))
        self.stage_right = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-right.png'))
        self.mania_key = pygame.image.load(os.path.join('./resources', 'img', 'mania-key.png'))

        # Load in text
        self.keys = [self.game.titlefont.render("D", True, self.game.color),
                     self.game.titlefont.render("F", True, self.game.color),
                     self.game.titlefont.render("J", True, self.game.color),
                     self.game.titlefont.render("K", True, self.game.color)
                     ]

        self.tutorial = [self.game.textfont.render("Use the arrow keys to navigate the menus", True, self.game.color),
                         self.game.textfont.render("Press the Enter to select", True, self.game.color),
                         self.game.textfont.render("Press Esc to go back", True, self.game.color),
                         self.game.textfont.render("The game controls are at the right", True, self.game.color),
                         self.game.textfont.render("Press the correct keys when the notes hit the line", True, self.game.color),
                         self.game.textfont.render("Have fun!", True, self.game.color)
                         ]

    def render(self, event):
        self.game.screen.fill((0, 0, 0))

        # Render Keys & Letters
        for i in range(4):
            self.game.screen.blit(self.mania_key, (810 + i * 65, 528))
            self.game.screen.blit(self.keys[i], (830 + i * 65, 650))

        # Render Sides
        self.game.screen.blit(self.stage_left, (787, 0))
        self.game.screen.blit(self.stage_right, (1070, 0))

        # Text
        for i in range(5):
            self.game.screen.blit(self.tutorial[i], (50, 230 + i * 50))

        # Key detection
        if event == "esc":
            self.game.mainmenu_handler()

        # Update display
        pygame.display.flip()
