import Classes
from Classes.Wall import Wall
from Classes.Fruits import Banane
from Classes.Fruits import Date
from Classes.Fruits import Fraise
from Classes.Fruits import Orange
from Classes.Fruits import Pasteque
import pygame, sys
from pygame.locals import *

surface = pygame.display.get_surface

class Level :

        def __init__(self,levelNumber):
                
                self.levelName = 'Levels/level' + str(levelNumber) + '.txt'
                self.levelList = []
                self.collisionList = []

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
                            self.collisionList.append((Wall(i,j), '1'))
                        if self.levelList[j][i] == '2' :
                            self.collisionList.append((Banane(i,j), '2'))
                        if self.levelList[j][i] == '3' :
                            self.collisionList.append((Orange(i,j), '3'))
                        if self.levelList[j][i] == '4' :
                            self.collisionList.append((Fraise(i,j), '4'))
                        if self.levelList[j][i] == '5' :
                            self.collisionList.append((Date(i,j), '5'))
                        if self.levelList[j][i] == '6' :
                            self.collisionList.append((Pasteque(i,j), '6'))
            
        def set_LevelPlatformList(self):
                self.createLevelPlatformList()