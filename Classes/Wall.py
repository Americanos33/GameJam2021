import Classes
from Classes.Stuff import Stuff
class Wall(Stuff) :

    def __init__(self, X, Y) :
        Stuff.__init__(self, X, Y, "wall")