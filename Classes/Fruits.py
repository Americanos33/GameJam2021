import Stuff

class Fruits(Stuff, surface, name) :

    def __init__(self, X, Y, surface) :
        Stuff.__init__(self, X, Y, name, surface)

class Banane(Fruits, surface) :

    def __init__(self, X, Y, surface) :
        Fruits.__init__(self, surface, "banane")

class Orange() :

    def __init__(self, X, Y, surface) :
        Fruits.__init__(self, surface, "orange")

class Fraise() :

    def __init__(self, X, Y, surface) :
        Fruits.__init__(self, surface, "fraise")

class Date() :

    def __init__(self, X, Y, surface) :
        Fruits.__init__(self, surface, "date")

class Pasteque() :

    def __init__(self, X, Y, surface) :
        Fruits.__init__(self, surface, "pasteque")
