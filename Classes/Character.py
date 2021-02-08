import pygame

class Character :

    def __init__(self, pos):
        self.dx = 0 # X directionn
        self.dy = 0 # Y direction
        self.pos = (pos[0], pos[1])

        self.image = pygame.image.load("images/personnage1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.image.set_colorkey((240,240,240))

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.bottom = pos[1]
        self.win = True

    def move(self) :

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1


    def draw(self, surface) :
        surface.blit(self.image, self.pos)