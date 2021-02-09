import pygame
from player import Player
from pygame.locals import *


class Game :

    def __init__(self):
        self.player = Player()
        self.pressed = {}
        