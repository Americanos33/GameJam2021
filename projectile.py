import pygame
import random

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player, typen):
        super().__init__()
        self.player = player
        self.typen = typen
        self.velocity = 5
        self.image = pygame.image.load("images/fourchettL.png")
        self.image = pygame.transform.scale(self.image, (58,58))
        self.rect=self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 5

        if self.typen == "boss":
            self.rect.y = player.rect.y + random.randint(0,200)
        

    def suppr(self):
        self.player.tt_projectiles1.remove(self)
        self.player.tt_projectiles2.remove(self)
        

    def move_d(self):
        
        self.rect.x += self.velocity
        self.image = pygame.image.load("images/fourchettR.png")
        
        if self.rect.x > 1022 :
            self.suppr()

        if self.typen == "player" :
            for monster in self.player.game.check_collisionMonstre(self, self.player.game.tt_monsters):
                self.suppr()  
                #infliger des dégats
                monster.damage(self.player.attack)

            for boss in self.player.game.check_collisionMonstre(self, self.player.game.tt_boss):
                self.suppr()
                boss.damage(self.player.attack)

        if self.typen == "boss" :
            for player in self.player.game.check_collisionMonstre(self, self.player.game.tt_players):
                self.suppr()
                player.damage(self.player.game.boss.attack)

    def move_g(self):

        self.rect.x -= self.velocity

        if self.rect.x < 0 :
            self.suppr()

        if self.typen == "player" :
            for monster in self.player.game.check_collisionMonstre(self, self.player.game.tt_monsters):
                self.suppr()  
                #infliger des dégats
                monster.damage(self.player.attack)

            for boss in self.player.game.check_collisionMonstre(self, self.player.game.tt_boss):
                self.suppr()
                boss.damage(self.player.attack)

        if self.typen == "boss" :
            for player in self.player.game.check_collisionMonstre(self, self.player.game.tt_players):
                self.suppr()
                player.damage(self.player.game.boss.attack)