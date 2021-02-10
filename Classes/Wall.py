import Classes
from Classes.Stuff import Stuff
import pygame
class Wall(pygame.sprite.Sprite) :

    def __init__(self, X, Y) :
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.transform.smoothscale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.left = 20*(self.X) 
        self.rect.bottom = 20*(self.Y+1)

    def draw(self, surface):
        surface.blit(self.image, self.rect)