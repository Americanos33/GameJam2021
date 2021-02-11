import pygame
from player import Player
from monster import Monster
from pygame.locals import *
import Classes.Level
from Classes.Level import Level


class Game :

    def __init__(self, level):
        self.is_playing = False
        self.menu = True
        self.game_over = False 
        self.tt_players = pygame.sprite.Group()
        self.level = level
        self.player = Player(self)
        self.tt_players.add(self.player)

        self.tt_monsters = pygame.sprite.Group()
        self.all_fruits = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.pressed = {}

        if self.level.nblvl == 1:
            self.spawn_monster()
            self.spawn_monster()
        elif self.level.nblvl == 2:
            self.spawn_monster()

        #self.levelnumber = level.getNbLvl()
        self.spawn_wall()
        self.spawn_fruits()

    def check_collisionDpl(self, sprite1, sprite2):
        if not pygame.sprite.collide_rect(sprite1, sprite2):
            return True
        
    

    def check_collisionWallX(self, sprite, group):
        #r = pygame.Rect(sprite.rect.width, sprite.rect.height)
        for i in group:
            if (i.rect.top == sprite.rect.bottom):                
               return True
            else :
                return self.check_allCollisions(sprite, group)
        return False

    def check_collisionWallYGround(self, sprite, group):
        for i in group:
            if i.rect.top == sprite.rect.bottom:
                return True
        return False

    def check_collisionWallYCiel(self, sprite, group):
        for i in group:
            if i.rect.bottom == sprite.rect.top:
                return True
        return True

    def check_allCollisions(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def check_collisionFruit(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def check_collisionMonstre(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster=Monster(self)
        self.tt_monsters.add(monster)

    def spawn_wall(self):
        for w in self.level.wall_list :
            self.all_walls.add(w)
    
    def spawn_fruits(self):
        for f in self.level.fruits_list :
            self.all_fruits.add(f)
        