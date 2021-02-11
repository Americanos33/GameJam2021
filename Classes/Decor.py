import pygame

class Decor(pygame.sprite.Sprite):

    def __init__(self, X, Y, name):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = pygame.image.load("images/" + name + ".png")
        if name == "tree":
            self.image = pygame.transform.smoothscale(self.image, (128,128))
        else :
            self.image = pygame.transform.smoothscale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.left = 32*(self.X) 
        self.rect.bottom = 32*(self.Y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)