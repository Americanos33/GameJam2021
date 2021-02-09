class Level :

        def __init__(self,levelNumber):
                
                self.levelName = 'Platformer-master/levels/level' + str(levelNumber) + '.txt'
                self.levelList = []
                self.collisionList = []
                self.numberOfCoins = 0

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
                                if self.levelList[j][i] == 't' :
                                        self.collisionList.append((Platform(i,j), 't'))
                                elif self.levelList[j][i] == 'd' :
                                        self.collisionList.append((Door(i,j), 'd'))
                                elif self.levelList[j][i] == 'm' :
                                        self.collisionList.append((Jumper(i,j), 'm'))
                                elif self.levelList[j][i] == 'c' :
                                        self.collisionList.append((Coin(i,j), 'c'))
                                        self.numberOfCoins += 1
                                elif self.levelList[j][i] == 's' :
                                        self.collisionList.append((Spikes(i,j), 's'))
            
        def set_LevelPlatformList(self):
                self.createLevelPlatformList()