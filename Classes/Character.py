import pygame
from pygame.locals import *

S = 5

class Character :

    def __init__(self, x, y):
        self.dx = 0 # X directionn
        self.dy = 0 # Y direction

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.image.set_colorkey((240,240,240))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.win = True

    def stop(self):

        #stops the character from moving sideways
        self.dx = 0


    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        self.dx = S

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        self.dx = -S

    def move(self) :        
        if (self.rect.x + self.dx) > 0 and (self.rect.x + self.dx) < 960 :
            self.rect.x += self.dx
        else :
            self.dx = 0


    def draw(self, surface) :
        surface.blit(self.image, self.rect)