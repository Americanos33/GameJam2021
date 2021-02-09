import Classes
from game import Game
import pygame
from pygame.locals import *

# Variables
width = 1024
height = 768
rows = 32

# Pygame initialization
pygame.init()
pygame.display.set_caption("Le lit perdu")
win = pygame.display.set_mode((width, height))

# Character initialization
game = Game()

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
    game.player.draw(win)
    win.blit(banane, (128, 576))
    win.blit(orange, (288, 576))
    win.blit(date, (448, 576))
    win.blit(fraise, (578, 576))
    win.blit(pasteque, (736, 576))
    drawGrid(width, rows, win)
    pygame.draw.rect(win, (160,82,45), (0,668,1028,100))
    pygame.display.update()


def main():
    # Game runing variables
    inGame = True
    clock = pygame.time.Clock()

    while inGame:

        redrawWindow()

        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < win.get_width():
            game.player.moveRight()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.moveLeft()

        for event in pygame.event.get():
            if event.type == QUIT:
                inGame = False
                pygame.display.quit()
                pygame.quit()
            
            if event.type == KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_UP:
                    game.player.moveSaut()
            elif event.type == KEYUP:
                game.pressed[event.key] = False

        pygame.time.delay(1)
        clock.tick(60)


main()