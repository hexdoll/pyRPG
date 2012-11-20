import pygame

class Player:
    name = 'Player'
    position = {'x': 100, 'y': 100}
    direction = 'down'
    speed = 10

    def __init__(self, name='Player'):
        self.name = name

    def render(self, screen):
        screen.blit(self._get_sprite(), (self.position['x'], self.position['y']))

    '''
    Loads sprites from image file
    '''
    def _load_sprites(self, image_file, data_file):
        #hard coded for now
        self.sprites = {
                'up' : 1,
                'down' : 2,
                'left' : 3,
                'right' : 4,
        }


    '''
    returns the correct sprite to render depending on which direction the player is facing
    '''
    def _get_sprite(self):
        sprites = {
                'up' : 'data/sprites/player/up.png',
                'down' : 'data/sprites/player/down.png',
                'left' : 'data/sprites/player/left.png',
                'right' : 'data/sprites/player/right.png'
        }
        image = pygame.image.load(sprites[self.direction])
        return image.convert_alpha()

    def go_up(self):
        self.direction = 'up'
        self.position['y'] -= self.speed

    def go_down(self):
        self.direction = 'down'
        self.position['y'] += self.speed

    def go_left(self):
        self.direction = 'left'
        self.position['x'] -= self.speed

    def go_right(self):
        self.direction = 'right'
        self.position['x'] += self.speed
