import pygame
import time
from projectile import Projectile
from pygame.locals import *
import Classes
from Classes.Level import Level


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()

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
        self.nb_saut = 2
        self.a_sauter = False

        self.tt_projectiles1 = pygame.sprite.Group()
        self.tt_projectiles2 = pygame.sprite.Group()
        self.nb_projectiles = 30


    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        
        self.rect.x += self.velocity
        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.printImage(1)

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        
        self.rect.x += -self.velocity
        self.image = pygame.image.load("images/personnage2.png").convert_alpha()
        self.printImage(2)

    def printImage(self, nb):
        self.image = pygame.transform.scale(self.image, (64,64))

        if nb == 1:
            self.image.set_colorkey((240,241,241))
        elif nb == 2:
            self.image.set_colorkey((240,240,240))


    def moveSaut(self):
        if self.a_sauter and self.nb_saut >= 0:
            
            if self.saut_monte >= 5:
                self.saut_descend -= 1.5
                self.saut = self.saut_descend
            else: 
                self.saut_monte += 2
                self.saut = self.saut_monte
            
            if self.saut_descend < 0:
                self.saut_monte = 0
                self.saut_descend = 5
                self.a_sauter = False
                
        
        self.rect.y = self.rect.y - (10 * (self.saut/2))  


    def draw(self, surface) :
        surface.blit(self.image, self.rect)

    def lancer_projectile1(self):
        self.tt_projectiles1.add(Projectile(self))

    def lancer_projectile2(self):
        self.tt_projectiles2.add(Projectile(self))

    def collisionX(self, level) :
        
        for c in level.collisionList :
            if c[0].rect.colliderect(self.rect) :
                if c[1] == '1':
                    #Contre un mur
                    if self.dx > 0 :
                        self.rect.right = c[0].rect.left
                        return False   
                    elif self.dx < 0 :
                        self.rect.left = c[0].rect.right
                        return False
                elif c[1] == '2':
                    #Contre une banane
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '3' :
                    #Contre une orange
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '4' :
                    #Contre une fraise
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '5' :
                    #Contre une date
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '6' :
                    #Contre une pastèque
                    level.collisionList.remove(c)
                    return True
                else:
                    return True

    def collisionY(self, level) :
                
        for c in level.collisionList :
            if c[0].rect.colliderect(self.rect) :
                if c[1] == '1':
                    if self.dy > 0 :
                        self.rect.bottom = c[0].rect.top 
                        self.dy = 0
                        return False
                    elif self.dy < 0 :
                        self.rect.top = c[0].rect.bottom
                        self.dy = 0
                        return False
                elif c[1] == '2':
                    #Contre une banane
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '3' :
                    #Contre une orange
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '4' :
                    #Contre une fraise
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '5' :
                    #Contre une date
                    level.collisionList.remove(c)
                    return True
                elif c[1] == '6' :
                    #Contre une pastèque
                    level.collisionList.remove(c)
                    return True
                else :
                    return True