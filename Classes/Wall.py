import Classes
from Classes.Stuff import Stuff
import pygame
class Wall(Stuff, pygame.sprite.Sprite) :

    def __init__(self, X, Y) :
        Stuff.__init__(self, X, Y, "wall")