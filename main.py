import Classes
from Classes import Character
import pygame
from pygame.locals import *

# Variables
width = 1024
height = 768
rows = 32

# Pygame initialization
pygame.init()
win = pygame.display.set_mode((width, height))

# Character initialization
carac = Character.Character(0,576)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127,127,127)

# Images
levelBackground = pygame.image.load('images/ciel_jour.jpg')
levelBackground = pygame.transform.scale(levelBackground, (width, height))

banane = pygame.image.load('images/banane.png')
banane = pygame.transform.smoothscale(banane, (32,32))

orange = pygame.image.load('images/oranepd.png')
orange = pygame.transform.smoothscale(orange, (32,32))

date = pygame.image.load('images/dategre.png')
date = pygame.transform.smoothscale(date, (32,32))

fraise = pygame.image.load('images/fraise.png')
fraise = pygame.transform.smoothscale(fraise, (32,32))

pasteque = pygame.image.load('images/pasteqq.png')
pasteque = pygame.transform.smoothscale(pasteque, (32,32))


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
    

def redrawWindow():
    win.blit(levelBackground, (0,0))
    carac.draw(win)
    win.blit(banane, (150, 576))
    win.blit(orange, (300, 576))
    win.blit(date, (450, 576))
    win.blit(fraise, (600, 576))
    win.blit(pasteque, (750, 576))
    drawGrid(width, rows, win)
    pygame.display.update()

def main():
    # Game runing variables
    inGame = True
    clock = pygame.time.Clock()

    while inGame:

        print(carac.dx)

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_LEFT and carac.dx < 0: # PROBLEME ICI : carac.dx  ne fonctionne pas comme prévu
                    carac.stop()
                if event.key == K_RIGHT and carac.dx > 0: # PROBLEME ICI : carac.dx  ne fonctionne pas comme prévu
                    carac.stop()
            if event.type == KEYDOWN:
                if event.key == K_LEFT :
                    carac.moveLeft()
                if event.key == K_RIGHT :
                    carac.moveRight()
                if event.key == K_DOWN :
                    carac.stop()

        carac.move()

        redrawWindow()

        for event in pygame.event.get():
            if event.type == QUIT:
                inGame = False
                pygame.display.quit()
                pygame.quit()

    pygame.time.delay(1)
    clock.tick(120)


main()