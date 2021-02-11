import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, X, Y, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1

        if game.level.nblvl == 1:
            monst = self.image = pygame.image.load("images/oliveMs.png")
        elif game.level.nblvl == 2:
            monst = self.image = pygame.image.load("images/oignon.png")

        self.rect = monst.get_rect()
        self.rect.x = X
        #bordure de deplacement des monstres
        self.xg = (self.rect.x)-100
        self.xd = self.rect.x
        self.count = 1
        self.rect.y = Y 
        self.velocity = 2 + random.randint(0, 2)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si ses pv <= 0
        if self.health <= 0: 
            #Supprimer le monstre
            self.game.tt_monsters.remove(self) #fais gaffe ça supprime tous les monstres 
                
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
    
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)