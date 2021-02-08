import Classes
from Classes import *
import pygame
from pygame.locals import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127,127,127)

# Pygame initialization
pygame.init()


def drawWindow(surface):
    pygame.draw.line(surface, (160,82,45), (0,668), (1024,668), 5)
    

def redrawWindow(surface):
    drawWindow(surface)
    pygame.display.update()

def main():
    # Size elements
    width = 1024
    height = 768
    win = pygame.display.set_mode((width, height))

    # Images
    levelBackground = pygame.image.load('images/ciel_jour.jpg')
    levelBackground = pygame.transform.scale(levelBackground, (width, height))

    carac = pygame.image.load('images/personnage1.png').convert_alpha()
    carac = pygame.transform.scale(carac, (75,75))
    carac.set_colorkey((240,240,240))

    banane = pygame.image.load('images/banane.png')
    banane = pygame.transform.smoothscale(banane, (40,40))

    orange = pygame.image.load('images/oranepd.png')
    orange = pygame.transform.smoothscale(orange, (40,40))

    date = pygame.image.load('images/dategre.png')
    date = pygame.transform.smoothscale(date, (80,80))

    # Game runing variables
    inGame = True
    clock = pygame.time.Clock()

    while inGame:

        win.blit(levelBackground, (0,0))
        win.blit(carac, (0,593))
        win.blit(banane, (200, 593))
        win.blit(orange, (500, 593))
        win.blit(date, (700, 593))

        redrawWindow(win)

        for event in pygame.event.get():
            if event.type == QUIT:
                inGame = False
                pygame.display.quit()
                pygame.quit()

    pass


main()