import pygame


class Boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 400
        self.max_health = 400
        self.attack = 1

        
        boss = self.image = pygame.image.load("images/patate.png")
        self.rect = boss.get_rect()
            
        self.rect.x = 0
        self.rect.y = 0
        self.xg = (self.rect.x)-100
        self.xd = self.rect.x
                