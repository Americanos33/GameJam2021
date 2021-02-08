import pygame

class Character :

    def __init__(self, x, y):
        self.dx = 0 # X directionn
        self.dy = 0 # Y direction

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75,75))
        self.image.set_colorkey((240,240,240))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.win = True

    def move(self) :
        self

    def draw(self, surface) :
        surface.blit(self.image, (0,593))