import pygame
import time
from pygame.locals import *


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.printImage(1)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 606
        self.win = True


    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        self.rect.x += self.velocity
        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.printImage(1)

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        self.rect.x -= self.velocity
        self.image = pygame.image.load("images/personnage2.png").convert_alpha()
        self.printImage(2)

    def printImage(self, nb):
        self.image = pygame.transform.scale(self.image, (64,64))

        if nb == 1:
            self.image.set_colorkey((240,241,241))
        elif nb == 2:
            self.image.set_colorkey((240,240,240))


    def moveSaut(self):
        self.rect.y += -1   


    def draw(self, surface) :
        surface.blit(self.image, self.rect)