

class Decor:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.transform.smoothscale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.left = 32*(self.X) 
        self.rect.bottom = 32*(self.Y)

    def draw(self):
        