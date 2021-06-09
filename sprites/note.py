import os
import random
import pygame


class Note(pygame.sprite.Sprite):
    def __init__(self, ps):
        super().__init__()
        self.ps = ps
        self.random_x = [510, 575, 640, 705]
        self.random_y = []
        for i in range(60):
            self.random_y.append(int(i * random.randint(-150, -75)))

        # Generate a random coordinate
        self.note_spawn = (random.choice(self.random_x), random.choice(self.random_y))

        # Image for note sprite
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('./', 'resources', 'img', 'mania-note.png')),
                                            (65, 30))
        self.rect = self.image.get_rect()

        # Set coordinate to rectangle of sprite
        self.rect.topleft = self.note_spawn

    def update(self):
        # Move the note down
        self.rect.topleft = (self.rect.x, self.rect.y + 1)

        # When notes reach the end of the screen
        if self.rect.y > 720:
            self.ps.missed += 1
            self.kill()
