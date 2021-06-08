import pygame
import os
from sprites import note, key


class StageRandom:
    def __init__(self, game):
        self.game = game
        self.missed = 0

        # Load in images
        self.stage_left = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-left.png'))
        self.stage_right = pygame.image.load(os.path.join('./resources', 'img', 'mania-stage-right.png'))
        self.mania_key = pygame.image.load(os.path.join('./resources', 'img', 'mania-key.png'))

        # Key Sprite
        self.key_group = pygame.sprite.Group()
        self.key_list = []
        for i in range(4):
            self.key = key.Key(510 + i * 65, 563)

            self.key_list.append(self.key)
            self.key_group.add(self.key)

        # Note Sprite
        self.note_group = pygame.sprite.Group()
        self.note_list = []
        self.note_coords = []
        for a in range(100):
            notes = note.Note(self)
            pygame.sprite.spritecollide(notes, self.note_group, True)

            self.note_group.add(notes)
            self.note_list.append(notes)
            self.note_coords.append(notes.rect.topleft)

        # Total amount of notes
        self.total_notes = len(self.note_group.sprites())

    def render(self, event):
        # Set background to black
        self.game.screen.fill((0, 0, 0))

        # Render Keys
        for i in range(4):
            self.game.screen.blit(self.mania_key, (510 + i * 65, 528))

        # Render Sides
        self.game.screen.blit(self.stage_left, (487, 0))
        self.game.screen.blit(self.stage_right, (770, 0))

        # Draw key and note sprites
        self.key_group.draw(self.game.screen)
        self.note_group.draw(self.game.screen)
        self.note_group.update()

        # Collision Detection
        if pygame.sprite.groupcollide(self.note_group, self.key_group, False, False):
            # Detect which key
            for key in self.key_list:
                if pygame.sprite.spritecollide(key, self.note_group, False):
                    # Key 1
                    if key.rect.topleft == (510, 563):
                        if event == "d":
                            # Kill note
                            pygame.sprite.spritecollide(key, self.note_group, True)

                    # Key 2
                    if key.rect.topleft == (575, 563):
                        if event == "f":
                            # Kill note
                            pygame.sprite.spritecollide(key, self.note_group, True)

                    # Key 3
                    if key.rect.topleft == (640, 563):
                        if event == "j":
                            # Kill note
                            pygame.sprite.spritecollide(key, self.note_group, True)

                    # Key 4
                    if key.rect.topleft == (705, 563):
                        if event == "k":
                            # Kill note
                            pygame.sprite.spritecollide(key, self.note_group, True)

        # Update Display
        pygame.display.flip()

        # When all the notes are killed
        if not self.note_group.sprites():
            # Calculate Accuracy
            accuracy = round(((self.total_notes - self.missed) / self.total_notes) * 100, 2)

            # Regenerate Notes
            self.__init__(self.game)

            # End Menu
            self.game.end_handler(accuracy)
