import pygame
from projectile import Projectile

class Boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 400
        self.max_health = 400
        self.attack = 10
        self.velocity = 5

        self.tt_projectiles1 = pygame.sprite.Group()
        self.tt_projectiles2 = pygame.sprite.Group()
        self.nb_projectiles = 20
    
        if self.game.level.nblvl == 4:
            self.image = pygame.image.load("images/Boss1.png").convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (256,256))
            self.rect = self.image.get_rect()
                
            self.rect.x = 350
            self.rect.y = 400
            self.xg = (self.rect.x)-100
            self.xd = self.rect.x

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si ses pv <= 0
        if self.health <= 0: 
            self.game.add_score(100)
            
            #Supprimer le monstre
            self.game.tt_boss.remove(self) #fais gaffe ça supprime tous les monstres 
            #ajout du score
            
    def update_health_bar(self, surface):
    
        bar_color = (111, 210, 46)

        back_bar_color = (60,63,60)
        

        bar_position = [self.rect.x - 15, self.rect.y, self.health ,5]
        
        back_bar_position = [self.rect.x - 15, self.rect.y, self.max_health ,5]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)
        
   
    def deplaM(self):
        if self.rect.y == self.yd:
            self.count *= -1
        if self.rect.y == self.yg:
            self.count *= -1

        if self.count > 0 :
            if self.rect.y < self.xy:
                if not self.game.check_collisionMonstre(self,self.game.tt_players):
                    self.rect.y += self.velocity
                #si le monstre est en collision avec le joueur il inflige des degats
                else:   
                    self.game.player.damage(self.attack)
        if self.count < 0 :
            if self.rect.y > self.yg:
                if not self.game.check_collisionMonstre(self,self.game.tt_players):
                    self.rect.y -= self.velocity
                else: 
                    self.game.player.damage(self.attack)


    def lancer_projectile1(self):
        self.tt_projectiles1.add(Projectile(self))
                