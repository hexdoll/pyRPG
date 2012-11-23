import pygame

class Scene:
    IMAGE_DIR = 'data/scenes/'
    #background
    #foreground
    #collision

    def __init__(self, name='test'):
        self.name = name

        self.background = pygame.image.load(self.IMAGE_DIR + self.name + '/background.png')
        self.background = self.background.convert()

        self.foreground = pygame.image.load(self.IMAGE_DIR + self.name + '/foreground.png')
        self.foreground = self.foreground.convert_alpha()

        self.collision = pygame.image.load(self.IMAGE_DIR + self.name + '/collision.png')
        self.collision = pygame.mask.from_surface(self.collision)

    def renderBackground(self, screen):
        screen.blit(self.background, (0,0))

    def renderForeground(self, screen):
        screen.blit(self.foreground, (0,0))
