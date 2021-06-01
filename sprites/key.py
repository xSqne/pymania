import os
import pygame


class Key(pygame.sprite.Sprite):
    def __init__(self):
        super(Key, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('./', 'resources', 'img', 'mania-note.png')),
                                            (65, 30))
        self.rect = self.image.get_rect()
        self.rect.move()


