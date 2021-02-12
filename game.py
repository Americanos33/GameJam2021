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
        
        self.banane_list = pygame.sprite.Group()
        self.orange_list = pygame.sprite.Group()
        self.fraise_list = pygame.sprite.Group()
        self.date_list = pygame.sprite.Group()
        self.pasteque_list = pygame.sprite.Group()

        self.all_walls = pygame.sprite.Group()
        self.score = 0
        self.all_decors = pygame.sprite.Group()
        self.pressed = {}

        self.fruits_graille = []
        self.nb_fruits_graille = 0

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

    def check_collisionFruit(self, sprite):
        if self.check_collisionBanane(sprite, self.banane_list) :
            self.fruits_graille.append("banane")
            self.nb_fruits_graille += 1
            return True
        elif self.check_collisionOrange(sprite, self.orange_list) :
            self.fruits_graille.append("orange")
            self.nb_fruits_graille += 1
            return True
        elif self.check_collisionFraise(sprite, self.fraise_list) :
            self.fruits_graille.append("fraise")
            self.nb_fruits_graille += 1
            return True
        elif self.check_collisionDate(sprite, self.date_list) :
            self.fruits_graille.append("date")
            self.nb_fruits_graille += 1
            return True
        elif self.check_collisionPasteque(sprite, self.pasteque_list) :
            self.fruits_graille.append("pasteque")
            self.nb_fruits_graille += 1
            return True
        else :
            return False

    def check_collisionOrange(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def check_collisionBanane(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def check_collisionFraise(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def check_collisionDate(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def check_collisionPasteque(self, sprite, group):
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
        for f in self.level.orange_list :
            self.orange_list.add(f)

        for f in self.level.pasteque_list :
            self.pasteque_list.add(f)

        for f in self.level.fraise_list :
            self.fraise_list.add(f)

        for f in self.level.banane_list :
            self.banane_list.add(f)

        for f in self.level.date_list :
            self.date_list.add(f)
    
    def add_score(self, point):    
        self.score +=point

    def spawn_decors(self):
        for x in self.level.decor_collision_list:
            self.all_decors.add(x)

    def drawScore(self, surface):
        self.font = pygame.font.SysFont("monospace", 16)
        self.score_text = self.font.render(f"Score :  {self.score}",1,(255,255,255))
        surface.blit(self.score_text, (20,20))

    def drawLives(self, surface, nb):
        self.font = pygame.font.SysFont("monospace", 16)
        self.score_text = self.font.render(f"Morts :  {nb}",1,(255,255,255))
        surface.blit(self.score_text, (20,40))
        
    def updatePerso(self, a, h, s):
        self.player.attack = a
        self.player.health = h
        self.player.max_health = h
        self.player.velocity = s