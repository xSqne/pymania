import time

import pygame
import os
from sprites import note, key


class PlayStage:
    def __init__(self, game):
        self.game = game
        self.stage_left = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-left.png'))
        self.stage_right = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-right.png'))
        self.mania_key = pygame.image.load(os.path.join('./resources', 'img', 'mania-key.png'))

        self.key_group = pygame.sprite.Group()
        for i in range(4):
            self.key = key.Key(510 + i * 65, 563)
            self.key_group.add(self.key)

        self.note_group = pygame.sprite.Group()

        for a in range(20):
            notes = note.Note()
            pygame.sprite.spritecollide(notes, self.note_group, True)
            self.note_group.add(notes)

    def render(self):
        self.game.screen.fill((0, 0, 0))

        for i in range(4):
            self.game.screen.blit(self.mania_key, (510 + i * 65, 528))

        self.game.screen.blit(self.stage_left, (487, 0))
        self.game.screen.blit(self.stage_right, (770, 0))

        self.key_group.draw(self.game.screen)

        self.note_group.update()
        self.note_group.draw(self.game.screen)
        pygame.display.flip()



