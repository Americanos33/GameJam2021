import pygame
from player import Player
from monster import Monster
from pygame.locals import *


class Game :

    def __init__(self):
        self.player = Player()
        self.tt_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster=Monster()
        self.tt_monsters.add(monster)
        