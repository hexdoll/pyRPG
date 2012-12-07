import pygame
'''
Animated sprite class
Reads in sprite sheets uses that to animate
'''

class AnimatedSprite:
    images = [] #array of all sprites
    animations = {}
    animation = [] #which animation?
    counter = 0 #number of times we've displayed the current frame
    speed = 10 # frames per second
    frame = 0 #frame of animation cycle we're on

    #configurable animations
    #Hard coded for now
    animations = {
        'default': [(0,0)],
        'down': [(0,0),(1,0),(2,0),(3,0)],
        'up': [(0,3),(1,3),(2,3),(3,3)],
        'left': [(0,1),(1,1),(2,1),(3,1)],
        'right': [(0,2),(1,2),(2,2),(3,2)],
        'spin': [(0,0),(0,1),(0,3),(0,2)]
    }
    #Hard coded for now
    size = (27,47)

    def __init__(self, clock, filename):
        self.clock = clock
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit,message
        self._split()
        self.set_animation('default')

    # from http://pygame.org/wiki/Spritesheet
    def _image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill((0,0,0,0)) #transparent background
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def _split(self):
        (width, height) = self.size

        for x in range(self.sheet.get_width() / width):
            self.images.append([])
            for y in range(self.sheet.get_height() / height):
                self.images[x].append(self._image_at((x*width, y*height, width, height)))
    
    #reset starts the animation from the beginning
    def set_animation(self, animation, reset=False):
        if animation in self.animations:
            self.animation = animation
        if reset:
            self.frame = 0

    def get_frame(self):
        animation = self.animations[self.animation]
        self.frame = self.frame % len(animation) # loop to beginning of animation

        (x,y) = animation[self.frame]

        if self.speed == 0: #prevents div by 0 in frame counter
            return self.images[x][y]
        
        #how many times to display each frame
        if self.counter > self.clock.get_fps() / self.speed:
            self.counter = 0
            self.frame += 1
    
        self.counter += 1

        # print self.counter
        # print self.frame
        return self.images[x][y]
