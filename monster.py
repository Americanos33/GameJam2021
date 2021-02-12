import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1

        if game.level.nblvl == 1:
            monst = self.image = pygame.image.load("images/oliveMs.png")
            self.rect = monst.get_rect()
            if game.nb_monstres == 1 :
                self.rect.x = 704
                self.rect.y = 200
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            elif game.nb_monstres == 2 :
                self.rect.x = 192
                self.rect.y = 290
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            elif game.nb_monstres == 3 :
                self.rect.x = 416
                self.rect.y = 606
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1

        elif game.level.nblvl == 2:
            monst = self.image = pygame.image.load("images/oignon.png")
            self.rect = monst.get_rect()
            if game.nb_monstres == 1 :
                self.rect.x = 640
                self.rect.y = 50
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 2 :
                self.rect.x = 576
                self.rect.y = 250
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 3 :
                self.rect.x = 64
                self.rect.y = 310
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 4 :
                self.rect.x = 512
                self.rect.y = 600
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
  
        elif game.level.nblvl == 3:
            monst = self.image = pygame.image.load("images/concombre.png")
            self.rect = monst.get_rect()
            if game.nb_monstres == 1 :
                self.rect.x = 960
                self.rect.y = 35
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 2 :
                self.rect.x = 160
                self.rect.y = 65
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 3 :
                self.rect.x = 180
                self.rect.y = 455
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 4 :
                self.rect.x = 480
                self.rect.y = 650
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1
            if game.nb_monstres == 5 :
                self.rect.x = 1000
                self.rect.y = 390
                self.xg = (self.rect.x)-100
                self.xd = self.rect.x
                self.count = 1

        #if game.level.nblvl == 1:
        #    monst = self.image = pygame.image.load("images/oliveMs.png")
        #elif game.level.nblvl == 2:
        #    monst = self.image = pygame.image.load("images/oignon.png")
        #elif game.level.nblvl == 3:
        #    monst = self.image = pygame.image.load("images/concombre.png")
        #elif game.level.nblvl == 0:
        #    monst = self.image = pygame.image.load("images/Boss1.png")

        #self.rect = monst.get_rect()
        #self.rect.x = 400 + random.randint(0, 300)
        #self.rect.x = 416
        #bordure de deplacement des monstres
        #self.xg = (self.rect.x)-100
        #self.xd = self.rect.x
        #self.count = 1
        #self.rect.y = 606 
        self.velocity = 2

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si ses pv <= 0
        if self.health <= 0: 
            self.game.add_score(20)
            
            #Supprimer le monstre
            self.game.tt_monsters.remove(self) #fais gaffe ça supprime tous les monstres 
            #ajout du score
            
    def update_health_bar(self, surface):
        #couleur de la jauge (vert)
        bar_color = (111, 210, 46)
        #couleur de l'arriere plan de la jauge
        back_bar_color = (60,63,60)
        
        #definir la position de note jauge de vie
        #ainsi que sa largeur et son epaisseur 
        bar_position = [self.rect.x - 15, self.rect.y, self.health ,5]
        
        #definir la position de l'arriere plan 
        #de la jauge de vie
        back_bar_position = [self.rect.x - 15, self.rect.y, self.max_health ,5]

        #dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)
        
   
    def deplaM(self):
        if self.rect.x == self.xd:
            self.count *= -1
        if self.rect.x == self.xg:
            self.count *= -1

        if self.count > 0 :
            if self.rect.x < self.xd:
                if not self.game.check_collisionMonstre(self,self.game.tt_players):
                    self.rect.x += self.velocity
                #si le monstre est en collision avec le joueur il inflige des degats
                else:   
                    self.game.player.damage(self.attack)
        if self.count < 0 :
            if self.rect.x > self.xg:
                if not self.game.check_collisionMonstre(self,self.game.tt_players):
                    self.rect.x -= self.velocity
                else: 
                    self.game.player.damage(self.attack)
    
        
        
