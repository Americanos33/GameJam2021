import Classes
from Classes.Wall import Wall
from Classes.Fruits import Banane
from Classes.Fruits import Date
from Classes.Fruits import Fraise
from Classes.Fruits import Orange
from Classes.Fruits import Pasteque
from Classes.Decor import Decor
import pygame, sys
from pygame.locals import *

surface = pygame.display.get_surface

class Level :

        def __init__(self,levelNumber):
                
                self.nblvl = levelNumber
                self.levelName = 'Levels/level' + str(levelNumber) + '.txt'
                self.levelList = []
                
                self.wall_list = pygame.sprite.Group()
                self.decor_collision_list = pygame.sprite.Group()
                self.decor_simple_list = pygame.sprite.Group()

                self.banane_list = pygame.sprite.Group()
                self.orange_list = pygame.sprite.Group()
                self.fraise_list = pygame.sprite.Group()
                self.date_list = pygame.sprite.Group()
                self.pasteque_list = pygame.sprite.Group()

        def readMap(self):

                f = open(self.levelName, 'r')

                g = list(f)

                l = []
                for s in g :
                    l +=[list(s)]

                for i in range(len(l)-1) :
                    l[i].pop()
                return l

        def createLevelPlatformList(self):
                self.levelList = self.readMap()
                
                for j in range(len(self.levelList)):
                    for i in range(len(self.levelList[j])):
                        if self.levelList[j][i] == '1' :
                            self.wall_list.add(Wall(i,j))
                        if self.levelList[j][i] == '2' :
                            self.banane_list.add((Banane(i,j)))
                        if self.levelList[j][i] == '3' :
                            self.orange_list.add((Orange(i,j)))
                        if self.levelList[j][i] == '4' :
                            self.fraise_list.add((Fraise(i,j)))
                        if self.levelList[j][i] == '5' :
                            self.date_list.add((Date(i,j)))
                        if self.levelList[j][i] == '6' :
                            self.pasteque_list.add((Pasteque(i,j)))
                        if self.levelList[j][i] == '7' :
                            self.decor_simple_list.add((Decor(i,j, "tree")))
                        if self.levelList[j][i] == '8' :
                            self.decor_collision_list.add((Decor(i,j, "bed")))                        
                        if self.levelList[j][i] == '9' :
                            self.decor_collision_list.add((Decor(i,j, "porte")))

        def set_LevelPlatformList(self):
                self.createLevelPlatformList()

        def getNbLvl(self):
            return self.nblvl