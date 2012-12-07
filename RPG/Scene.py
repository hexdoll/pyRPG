import pygame

class Scene:
    IMAGE_DIR = 'data/scenes/'

    characters = []

    def __init__(self, name='test'):
        self.name = name

        self.background = pygame.image.load(self.IMAGE_DIR + self.name + '/background.png')
        self.background = self.background.convert()

        self.foreground = pygame.image.load(self.IMAGE_DIR + self.name + '/foreground.png')
        self.foreground = self.foreground.convert_alpha()

        self.collision = pygame.image.load(self.IMAGE_DIR + self.name + '/collision.png')
        self.collision_mask = pygame.mask.from_surface(self.collision)

    def render_background(self, screen):
        screen.blit(self.background, (0,0))

    def render_foreground(self, screen):
        screen.blit(self.foreground, (0,0))

    def render_mask(self, screen):
        screen.blit(self.collision, (0,0))

    def add_player(self, player):
        self.player = player

    def detect_collision(self):
        return self.collision_mask.overlap(self.player.collision_mask,
                (self.player.position['x'], self.player.position['y'])
        )
