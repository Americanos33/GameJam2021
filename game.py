import pygame
from player import Player
from monster import Monster
from pygame.locals import *
import Classes.Level
from Classes.Level import Level
import random

class Game :

    def __init__(self, level):
        self.is_playing = False
        self.menu = True
        self.game_over = False 
        self.game_wined = False
        self.tt_players = pygame.sprite.Group()
        self.level = level
        self.player = Player(self)
        self.tt_players.add(self.player)

        self.tt_monsters = pygame.sprite.Group()
        self.all_fruits = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.score = 0
        self.all_decors = pygame.sprite.Group()
        self.pressed = {}

        self.level = level

        self.nb_monstres = 0

        if self.level.nblvl == 1:
            self.nb_monstres = 1
            self.spawn_monster()
            self.nb_monstres = 2
            self.spawn_monster()
            self.nb_monstres = 3
            self.spawn_monster()
        elif self.level.nblvl == 2:
            self.nb_monstres = 1
            self.spawn_monster()
            self.nb_monstres = 2
            self.spawn_monster()
            self.nb_monstres = 3
            self.spawn_monster()
            self.nb_monstres = 4
            self.spawn_monster()
        elif self.level.nblvl == 3 :
            self.nb_monstres = 1
            self.spawn_monster()
            self.nb_monstres = 2
            self.spawn_monster()
            self.nb_monstres = 3
            self.spawn_monster()
            self.nb_monstres = 4
            self.spawn_monster()
            self.nb_monstres = 5
            self.spawn_monster()

        #self.levelnumber = level.getNbLvl()
        self.spawn_wall()
        self.spawn_fruits()
        self.spawn_decors()

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
    
    def add_score(self, point):    
        self.score +=point

    def spawn_decors(self):
        for x in self.level.decor_collision_list:
            self.all_decors.add(x)

    def drawScore(self, surface):
        self.font = pygame.font.SysFont("monospace", 16)
        self.score_text = self.font.render(f"Score :  {self.score}",1,(255,255,255))
        surface.blit(self.score_text, (20,20))

        
