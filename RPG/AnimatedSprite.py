import pygame
'''
Animated sprite class for working with sprites that can move in 4 directions
'''

class AnimatedSprite:
    SPRITE_WIDTH = 4
    SPRITE_HEIGHT = 4

    DIRECTIONS = 4
    DIRECTION_DOWN = 0
    DIRECTION_LEFT = 1
    DIRECTION_RIGHT = 2
    DIRECTION_UP = 3

    images = []
    direction = DIRECTION_DOWN
    counter = 0 #number of times we've displayed the current frame
    speed = 10 # frames per second
    frame = 0 #frame of walk cycle we're on

    def __init__(self, clock, filename):
        self.clock = clock
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit,message
        self.split()

    # from http://pygame.org/wiki/Spritesheet
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill((0,0,0,0)) #transparent background
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def split(self):
        height = self.sheet.get_height() / self.SPRITE_HEIGHT
        width = self.sheet.get_width() / self.SPRITE_HEIGHT

        for x in range(self.SPRITE_WIDTH):
            self.images.append([])
            for y in range(self.SPRITE_HEIGHT):
                self.images[x].append(self.image_at((x*width, y*height, width,height)))
    
    def get_frame(self):
        # print 'frame: %.0f' % self.frame
        # print 'counter: %.0f' % self.counter
        # fps = self.clock.get_fps()
        # print 'fps: %.2f' % fps
        # if self.counter > fps / self.speed:
        
        #how many times to display each frame
        if self.counter > self.clock.get_fps() / self.speed:
            self.counter = 0
            self.frame += 1

            #self.images[direction][frame] still
            #self.images[x][0] spinning
            #self.images[direction][frame] walking

        if self.frame > self.SPRITE_WIDTH-1: # loop to beginning of animation
            self.frame = 0
        
        image = self.images[self.frame][self.direction]
        self.counter += 1

        # print self.counter
        # print self.frame
        return image
