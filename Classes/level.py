import position as posi

class Level:

    def __init__(self, nbLvl):
        self.nbLvl = 1
        fichier = open("~/Documents/stockPython/data", "r")
        ligne = fichier.readline()
        while ligne !=("numero lvl " + nbLvl):
            ligne = fichier.readline()
        self.longueur = int(ligne = fichier.readline())
        self.largeur = int(ligne = fichier.readline())
        self.departJx = int(ligne = fichier.readline())
        self.departJy = int(ligne = fichier.readline())
        posi.Position.__init__(self, self.departJx, self.departJy)
        self.nbTypeFruit = int(ligne = fichier.readline())
        j = 0
        for j in range(0, self.nbTypeFruit):
            self.nomFruit = fichier.readline()
            self.posFruitx = int(ligne = fichier.readline())
            self.posFruity = int(ligne = fichier.readline())
            posi.Position.__init__(self, self.posFruitx, self.posFruity)
            self.tableFruits = {}
            self.tableFruits[str(j)] = posi.Position

        while (fichier.readline() != ""):
            self.grille = self.grille + "\n" + fichier.readline()

            

    def nextLevel(self):
        self.nbLvl = self.nbLvl+1
    

    def initialiseGrille(self):
        self.grille.initialiseJoueur(self)
        self.grille.initialiseFruit(self)
        print(self.grille)


    def initialiseFruits(self): 
        for k in self.tableFruits.items():
            posi.posFruit = self.tableFruits[k]
            c = self.longueur * (posi.posFruit.self.posFruitx - 1) + posi.posFruit.self.posFruity
            caracteres = list(self.grille)
            caracteres[c] = "O"
            self.grille = "".join(caracteres)

    def initialiseJoueur(self):
        c = self.longueur * (self.departJx - 1) + self.departJy
        caracteres = list(self.grille)
        caracteres[c] = "X"
        self.grille = "".join(caracteres)
        return self.grille

