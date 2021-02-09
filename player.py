import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.image.set_colorkey((240,240,240))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 606
        self.win = True


    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        self.rect.x += self.velocity

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        self.rect.x -= self.velocity

    


    def draw(self, surface) :
        surface.blit(self.image, self.rect)