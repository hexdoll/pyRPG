import pygame

class Scene:
    IMAGE_DIR = 'data/scenes/'

    def __init__(self):
        self.name = 'test'

        self.background = pygame.image.load(self.IMAGE_DIR+'background.png')
        self.background = self.background.convert()

        self.foreground = pygame.image.load(self.IMAGE_DIR+"foreground.png")
        self.foreground = self.foreground.convert_alpha()

    def renderBackground(self, screen):
        screen.blit(self.background, (0,0))

    def renderForeground(self, screen):
        screen.blit(self.foreground, (0,0))
