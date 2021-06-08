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
        self.keys = [self.game.font.render("D", True, self.game.color),
                     self.game.font.render("F", True, self.game.color),
                     self.game.font.render("J", True, self.game.color),
                     self.game.font.render("K", True, self.game.color)
                     ]

        self.tutorial = self.game.font.render("")

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
        

        # Update display
        pygame.display.flip()
