import Classes
from Classes import Level
from game import Game
import pygame, sys
from pygame.locals import *

# Variables
width = 1024
height = 768
rows = 32
currentLevel = 0

# Pygame initialization
pygame.init()
pygame.display.set_caption("Le lit perdu")
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

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

orange = pygame.image.load('images/orange.png')
orange = pygame.transform.smoothscale(orange, (32,32))

date = pygame.image.load('images/date.png')
date = pygame.transform.smoothscale(date, (32,32))

fraise = pygame.image.load('images/fraise.png')
fraise = pygame.transform.smoothscale(fraise, (32,32))

pasteque = pygame.image.load('images/pasteque.png')
pasteque = pygame.transform.smoothscale(pasteque, (32,32))

wall = pygame.image.load('images/Wall.png')
wall = pygame.transform.smoothscale(wall, (32,32))

menuBackground = pygame.image.load('images/menu1.jpg')
menuBackground = pygame.transform.scale(menuBackground, (width, height))

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
    game.player.tt_projectiles.draw(win)
    game.tt_monsters.draw(win)
    win.blit(banane, (128, 576))
    win.blit(orange, (288, 576))
    win.blit(date, (448, 576))
    win.blit(fraise, (578, 576))
    win.blit(pasteque, (736, 576))
    win.blit(wall, (800, 576))
    drawGrid(width, rows, win)
    pygame.draw.rect(win, (160,82,45), (0,668,1028,100))


def main():
    # Game runing variables
    inGame = False
    inMenu = True
    level = Level.Level(currentLevel)
    level.set_LevelPlatformList()

    while True:

        if inGame:

            redrawWindow()

            if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < win.get_width():
                game.player.moveRight()
                game.player.collisionX(level)
                game.player.collisionY(level)
            elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
                game.player.moveLeft()
                game.player.collisionX(level)
                game.player.collisionY(level)

            if game.player.rect.y >= 609:
                game.player.rect.y=604

            for event in pygame.event.get():
                if event.type == QUIT:
                    inGame = False
                    pygame.display.quit()
                    pygame.quit()
                    break
                if event.type == KEYDOWN:
                    game.pressed[event.key] = True
                    if event.key == pygame.K_UP:
                        game.player.a_sauter=True
                elif event.type == KEYUP:
                    game.pressed[event.key] = False

            game.player.moveSaut()
            game.player.collisionX(level)
            game.player.collisionY(level)


        elif inMenu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    inMenu = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    break
                if event.type == KEYDOWN:      
                    if event.key == K_SPACE:
                        inMenu = False
                        inGame = True
            win.blit(menuBackground, (0,0))

        for plat in level.collisionList :
            plat[0].draw()
            
        pygame.display.update()
        pygame.time.delay(2)
        clock.tick(60)

main()