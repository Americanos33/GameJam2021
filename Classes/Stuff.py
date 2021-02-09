class Stuff :

    def __init__(self, X, Y, stuffName, surface) :

        if self.stuffName != "void" :
            self.X = X
            self.Y = Y 
            self.stuffName = stuffName
            self.image = pygame.image.load('../images/' + self.stuffName + ".png")
            self.image.set_colorkey(GREY)  #set the transparent color = grey
            self.rect = self.image.get_rect() #create the rectangle associated with the platform
            self.rect.left = SIZE*(self.X) 
            self.rect.bottom = SIZE*(self.Y+1)

    def draw(self) :
        
        surface.blit(self.image, self.rect)