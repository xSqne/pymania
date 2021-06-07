import os
import random
import pygame


class Note(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.random_x = [510, 575, 640, 705]
        self.random_y = []
        for i in range(20):
            self.random_y.append(int(i * -150))

        self.note_spawn = (random.choice(self.random_x), random.choice(self.random_y))

        self.image = pygame.transform.scale(pygame.image.load(os.path.join('./', 'resources', 'img', 'mania-note.png')),
                                            (65, 30))
        self.rect = self.image.get_rect()

        self.rect.topleft = self.note_spawn


    def update(self):
        self.rect.topleft = (self.rect.x, self.rect.y + 2)

        if self.rect.y > 720:
            self.kill()
