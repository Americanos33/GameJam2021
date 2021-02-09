import Stuff

class Wall(Stuff, surface) :

    def __init__(self, X, Y, surface) :
        Stuff.__init__(self, X, Y, "Wall", surface)