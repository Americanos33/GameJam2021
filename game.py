import pygame
from player import Player
from monster import Monster
from pygame.locals import *
import Classes.Level
from Classes.Level import Level


class Game :

    def __init__(self, level):
        self.tt_players = pygame.sprite.Group()
        self.player = Player(self)
        self.tt_players.add(self.player)
        self.tt_monsters = pygame.sprite.Group()
        self.all_fruits = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.level = level
        #self.levelnumber = level.getNbLvl()
        self.spawn_wall()
        self.spawn_fruits()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_collisionFruit(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster=Monster(self)
        self.tt_monsters.add(monster)

    def spawn_wall(self):
        for w in self.level.wall_list :
            self.all_walls.add(w)
    
    def spawn_fruits(self):
        for f in self.level.fruits_list :
            self.all_fruits.add(f)
        