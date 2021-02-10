import pygame, sys
from pygame.locals import *

class Stuff :

    def __init__(self, X, Y, stuffName) :

        self.X = X
        self.Y = Y 
        self.stuffName = stuffName
        self.image = pygame.image.load("images/" + self.stuffName + ".png")
        #self.image.set_colorkey((127,127,127))  #set the transparent color = grey
        self.rect = self.image.get_rect() #create the rectangle associated with the platform
        self.rect.left = 20*(self.X) 
        self.rect.bottom = 20*(self.Y+1)

    def draw(self) :
        
        pygame.display.get_surface().blit(self.image, self.rect)