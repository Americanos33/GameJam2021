import pygame

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.image = pygame.image.load("images/fourchettL.png")
        self.image = pygame.transform.scale(self.image, (58,58))
        self.rect=self.image.get_rect()
        self.rect.x = player.rect.x 
        self.rect.y = player.rect.y + 5
        

    def suppr(self):
        self.player.tt_projectiles1.remove(self)
        self.player.tt_projectiles2.remove(self)
        

    def move_d(self):
        
        self.rect.x += self.velocity
        self.image = pygame.image.load("images/fourchettR.png")
        
        if self.rect.x > 1022 :
            self.suppr()
            

    def move_g(self):

        self.rect.x -= self.velocity

        if self.rect.x < 0 :
            self.suppr()
            