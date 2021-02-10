import pygame
import time
from projectile import Projectile
from pygame.locals import *
import Classes
from Classes.Level import Level


class Player(pygame.sprite.Sprite) :

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 3
        
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


    def moveRight(self, level):

        #moves the character to the Right and changes the character image accordingly
        self.rect.x += self.velocity
        self.printImage(1)
        self.game.check_collisionFruit(self, self.game.all_fruits)
        if (self.game.check_collision(self, self.game.tt_monsters)) or (self.game.check_collision(self, self.game.all_walls)) :
            self.rect.x += -self.velocity

    def moveLeft(self, level):
        
        #moves the character to the Left and changes the character image accordingly
        self.rect.x += -self.velocity
        self.printImage(1)
        self.game.check_collisionFruit(self, self.game.all_fruits)
        if (self.game.check_collision(self, self.game.tt_monsters)) or (self.game.check_collision(self, self.game.all_walls)):
            self.rect.x += self.velocity

    def printImage(self, nb):
        if nb == 1:
            self.image = pygame.image.load("images/personnage1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64,64))
            self.image.set_colorkey((240,241,241))
        elif nb == 2:
            self.image = pygame.image.load("images/personnage2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64,64))
            self.image.set_colorkey((240,240,240))


    def moveSaut(self):
        if not self.game.check_collision(self, self.game.all_walls) :
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
            self.game.check_collisionFruit(self, self.game.all_fruits)

    def draw(self, surface) :
        surface.blit(self.image, self.rect)

    def lancer_projectile1(self):
        self.tt_projectiles1.add(Projectile(self))

    def lancer_projectile2(self):
        self.tt_projectiles2.add(Projectile(self))
