#!/usr/bin/python

# Utility program to check the animations and functionality of the
# animatedSprite class

import pygame
from RPG.AnimatedSprite import AnimatedSprite

# code from http://www.gamedev.net/topic/444490-pygame-easy-as-py/
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("AnimatedSprite preview")

        self.clock = pygame.time.Clock()

        self.sprite = AnimatedSprite(self.clock, 'data/sprites/player/player_debug.png')

        self.background = pygame.image.load('data/scenes/debug.png').convert()

    def MainLoop(self):
        keepGoing = True
        direction = ''
        while keepGoing:
            self.clock.tick(30) #limit fps

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                # may want to look at pygame.key.set_repeat
                if event.type == pygame.KEYDOWN:
                    keyName = pygame.key.name(event.key)
                    self.sprite.speed = 10
                    if keyName == 'up':
                        self.sprite.direction = self.sprite.set_animation('up')
                    elif keyName == 'down':
                        self.sprite.direction = self.sprite.set_animation('down')
                    elif keyName == 'left':
                        self.sprite.direction = self.sprite.set_animation('left')
                    elif keyName == 'right':
                        self.sprite.direction = self.sprite.set_animation('right')
                    elif keyName == 'q':
                        self.sprite.direction = self.sprite.set_animation('spin')

                elif event.type == pygame.KEYUP:
                    if pygame.key.name(event.key) in ('up','down','left','right','q'):
                        self.sprite.speed = 0

            font = pygame.font.Font(None, 36)
            info = "Animation: %s Frame: %s" % (self.sprite.animation, self.sprite.frame)
            text = font.render(info, 1, (255, 255, 255))

            self.screen.blit(self.background, (0,0))
            self.screen.blit(text, (0,0))
            self.screen.blit(self.sprite.get_frame(), (320,240))
            pygame.display.flip()

g = Game()
g.MainLoop()
