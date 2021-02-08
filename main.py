import Classes
from Classes import Character
#from Character import *
import pygame
from pygame.locals import *

# Variables
width = 1024
height = 768
rows = 16

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127,127,127)

# Pygame initialization
pygame.init()


def drawGrid(w, r, surface):
    sizeBtwn = w // r
 
    x = 0
    y = 0
    for l in range(r):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

    #pygame.draw.line(surface, (160,82,45), (0,668), (1024,668), 5)
    

def redrawWindow(w, r, surface):
    drawGrid(w, r, surface)
    pygame.display.update()

def main():
    # Size elements
    win = pygame.display.set_mode((width, height))

    # Images
    levelBackground = pygame.image.load('images/ciel_jour.jpg')
    levelBackground = pygame.transform.scale(levelBackground, (width, height))

    carac = Character.Character(0,593)

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
        carac.draw(win)
        win.blit(banane, (200, 593))
        win.blit(orange, (500, 593))
        win.blit(date, (700, 593))

        redrawWindow(width, rows, win)

        for event in pygame.event.get():
            if event.type == QUIT:
                inGame = False
                pygame.display.quit()
                pygame.quit()

    pass


main()