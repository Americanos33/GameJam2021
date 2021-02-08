import pygame
from pygame.locals import *

# Pygame initialization
pygame.init()

def drawWindow(surface):
    pygame.draw.rect(surface, (255,255,255), (100,100,100,100))

def redrawWindow(surface):
    drawWindow(surface)
    pygame.display.update()

def main():
    width = 1024
    height = 768
    win = pygame.display.set_mode((width, height))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        redrawWindow(win)

        for event in pygame.event.get():
            if event.type == QUIT:
                flag = False
                pygame.display.quit()
                pygame.quit()

    pass


main()