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
        self.est_vivant = True
        self.dx = 0
        self.dy = 0

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.image.set_colorkey((240,241,241))

        #self.rect = self.image.get_rect()
        self.rect = Rect(0,0,40,64)
        self.rect.x = 0
        self.rect.y = 0
        self.win = True

        self.rect2 = Rect(0,0,40,63)

        self.saut = 0
        self.saut_monte = 0
        self.nb_saut = 2
        self.a_sauter = False

        self.tt_projectiles1 = pygame.sprite.Group()
        self.tt_projectiles2 = pygame.sprite.Group()
        self.nb_projectiles = 30

    def damage(self,amount): 
        if self.health - amount > amount:
            self.health -=amount
        if self.health <= 10:
            self.est_vivant= False
            

    def gravite(self):
        if  not pygame.sprite.spritecollideany(self, self.game.all_walls) :
                self.rect.y += 5
        else : 
            self.nb_saut = 2
        if self.rect.y >= 668:
            self.est_vivant = False

    def moveRight(self):

        #moves the character to the Right and changes the character image accordingly
        self.rect.x += self.velocity
        self.printImage(1)
        self.game.check_collisionFruit(self, self.game.all_fruits)
        if self.game.check_collisionWallX(self, self.game.all_walls):
            self.rect.x -= self.velocity

    def moveLeft(self):
        
        #moves the character to the Left and changes the character image accordingly
        self.rect.x -= self.velocity
        self.printImage(2)
        self.game.check_collisionFruit(self, self.game.all_fruits)
        if self.game.check_collisionWallX(self, self.game.all_walls):
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

        if self.a_sauter and self.nb_saut >= 0:
            
            if self.saut_monte >= 10:
                self.saut_monte = 0
                self.saut = 0
                self.a_sauter = False
            else: 
                self.saut_monte += 2
                self.saut = self.saut_monte
        
        self.rect.y -= (10 * (self.saut/2))

        if self.game.check_allCollisions(self, self.game.all_walls):
            self.rect.y += (10 * (self.saut/2))

        self.game.check_collisionFruit(self, self.game.all_fruits)

        


    def draw(self, surface) :
        surface.blit(self.image, self.rect)
        #r = pygame.Surface((self.rect.width, self.rect.height))
        #surface.blit(r, self.rect)

    def lancer_projectile1(self):
        self.tt_projectiles1.add(Projectile(self))

    def lancer_projectile2(self):
        self.tt_projectiles2.add(Projectile(self))

    def update_health_bar(self, surface):
        #couleur de la jauge (vert)
        bar_color = (111, 210, 46)
        #couleur de l'arriere plan de la jauge
        back_bar_color = (60,63,60)
        
        #definir la position de note jauge de vie
        #ainsi que sa largeur et son epaisseur 
        bar_position = [self.rect.x - 25, self.rect.y, self.health ,7]
        
        #definir la position de l'arriere plan 
        #de la jauge de vie
        back_bar_position = [self.rect.x - 25, self.rect.y, self.max_health ,7]

        #dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)