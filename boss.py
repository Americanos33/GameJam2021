import pygame


class Boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 400
        self.max_health = 400
        self.attack = 1

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
                