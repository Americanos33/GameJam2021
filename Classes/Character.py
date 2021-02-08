class Character :

    def __init__(self, x, y):
        self.dx = 0 # X directionn
        self.dy = 0 # Y direction

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.win = True

    #def draw(self):