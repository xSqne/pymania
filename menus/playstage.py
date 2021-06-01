import pygame
import os
from sprites import key


class PlayStage:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(os.path.join('./resources', 'fonts', 'Aller_Bd.ttf'), 48)
        self.stageleft = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-left.png'))
        self.stageright = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-right.png'))
        self.maniakey = pygame.image.load(os.path.join('./resources', 'img', 'mania-key.png'))

        self.note = key.Key()

        self.group = pygame.sprite.Group()
        self.group.add(self.note)

    def render(self):
        self.game.screen.fill((0, 0, 0))

        for i in range(4):
            self.game.screen.blit(self.maniakey, (510 + i * 65, 528))

        self.game.screen.blit(self.stageleft, (487, 0))
        self.game.screen.blit(self.stageright, (770, 0))

        self.group.draw(self.game.screen)

        pygame.display.flip()


