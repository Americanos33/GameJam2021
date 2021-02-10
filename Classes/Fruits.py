import Classes
from Classes.Stuff import Stuff

class Fruits(Stuff) :

    def __init__(self, X, Y, name) :
        Stuff.__init__(self, X, Y, name)

class Banane(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "banane")

class Orange(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "orange")

class Fraise(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "fraise")

class Date(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "date")

class Pasteque(Fruits) :

    def __init__(self, X, Y) :
        Fruits.__init__(self, X, Y, "pasteque")
