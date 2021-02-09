import pygame
import time
from pygame.locals import *


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        
        self.dx = 0
        self.dy = 0

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.printImage(1)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 608
        self.win = True

        self.saut = 0
        self.saut_monte = 0
        self.saut_descend = 5
        self.nb_saut = 0
        self.a_sauter = False

    def move(self) :

        # UPDATE the position of the character if the collisions allow it
        #self.grav()
        
        self.rect.x += self.dx
        #self.collisionX(collisionList)
        
        
        self.rect.y += self.dy
        #self.collisionY(collisionList)



    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        self.dx = self.velocity
        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.printImage(1)

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        self.dx = -self.velocity
        self.image = pygame.image.load("images/personnage2.png").convert_alpha()
        self.printImage(2)

    def printImage(self, nb):
        self.image = pygame.transform.scale(self.image, (64,64))

        if nb == 1:
            self.image.set_colorkey((240,241,241))
        elif nb == 2:
            self.image.set_colorkey((240,240,240))


    def moveSaut(self):
        if self.a_sauter :
            if self.saut_monte >=5:
                self.saut_descend -= 1
                self.saut = self.saut_descend
            else: 
                self.saut_monte += 1
                self.saut = self.saut_monte
            
            if self.saut_descend < 0:
                self.saut_monte = 0
                self.saut_descend = 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10 * (self.saut/2))  


    def draw(self, surface) :
        surface.blit(self.image, self.rect)