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
        pygame.display.set_caption("Gems Pygame RPG")

        self.clock = pygame.time.Clock()

        self.sprite = AnimatedSprite(self.clock, 'data/sprites/player/player.png')

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((100,60,25))

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
                    if keyName == 'up':
                        self.sprite.direction = AnimatedSprite.DIRECTION_UP
                    elif keyName == 'down':
                        self.sprite.direction = AnimatedSprite.DIRECTION_DOWN
                    elif keyName == 'left':
                        self.sprite.direction = AnimatedSprite.DIRECTION_LEFT
                    elif keyName == 'right':
                        self.sprite.direction = AnimatedSprite.DIRECTION_RIGHT

                elif event.type == pygame.KEYUP:
                    if pygame.key.name(event.key) in ('up','down','left','right'):
                        self.sprite.direction = AnimatedSprite.DIRECTION_DOWN

            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.sprite.get_frame(), (0,0))
            pygame.display.flip()

g = Game()
g.MainLoop()
