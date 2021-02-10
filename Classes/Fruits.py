import Classes
from Classes.Stuff import Stuff
import pygame

class Fruits(pygame.sprite.Sprite) :

    def __init__(self, X, Y, name) :
        pygame.sprite.Sprite.__init__(self)
        self.X = X
        self.Y = Y
        self.name = name
        self.image = pygame.image.load("images/" + self.name + ".png")
        self.image = pygame.transform.smoothscale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.left = 32*(self.X) 
        self.rect.bottom = 32*(self.Y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Banane(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "banane")

class Orange(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "orange")

class Fraise(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "fraise")

class Date(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "date")

class Pasteque(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "pasteque")
