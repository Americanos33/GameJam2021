import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 2
        monst = self.image = pygame.image.load("images/oliveMs.png")
        self.rect = monst.get_rect()
        self.rect.x = 980
        #bordure de deplacement des monstres
        self.xg = (self.rect.x)-100
        self.xd = self.rect.x
        self.count = 1
        self.rect.y = 608
        self.velocity = 2

    def deplaM(self):
        if self.rect.x == self.xd:
            self.count *= -1
        if self.rect.x == self.xg:
            self.count *= -1

        if self.count > 0 :
            if self.rect.x < self.xd:
                if not self.game.check_collision(self,self.game.tt_players):
                    self.rect.x += self.velocity
        if self.count < 0 :
            if self.rect.x > self.xg:
                if not self.game.check_collision(self,self.game.tt_players):
                    self.rect.x -= self.velocity

    
        
        
