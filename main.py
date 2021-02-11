import Classes
from Classes import Level
from game import Game
import pygame, sys
from pygame.locals import *

# Variables
width = 1024
height = 768
rows = 32
currentLevel = 1

# Pygame initialization
pygame.init()
pygame.display.set_caption("Le lit perdu")
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Game initialization
level = Level.Level(currentLevel)
game = Game(level)
level.set_LevelPlatformList(game)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127,127,127)

# Images
levelBackground = pygame.image.load('images/ciel_jour.jpg')
levelBackground = pygame.transform.scale(levelBackground, (width, height))

levelBackground2 = pygame.image.load('images/ciel_nuit-2.jpg')
levelBackground2 = pygame.transform.scale(levelBackground2, (width, height))

banane = pygame.image.load('images/banane.png')
banane = pygame.transform.smoothscale(banane, (32,32))

orange = pygame.image.load('images/orange.png')
orange = pygame.transform.smoothscale(orange, (32,32))

date = pygame.image.load('images/date.png')
date = pygame.transform.smoothscale(date, (32,32))

fraise = pygame.image.load('images/fraise.png')
fraise = pygame.transform.smoothscale(fraise, (32,32))

pasteque = pygame.image.load('images/pasteque.png')
pasteque = pygame.transform.smoothscale(pasteque, (32,32))

wall = pygame.image.load('images/wall.png')
wall = pygame.transform.smoothscale(wall, (32,32))

menuBackground = pygame.image.load('images/menu1.jpg')
menuBackground = pygame.transform.scale(menuBackground, (width, height))

gameOver = pygame.image.load('images/Game_Over.png')
gameOver= pygame.transform.scale(gameOver, (width,height))

def drawGrid(w, r, surface):
    sizeBtwn = w // r
 
    x = 0
    y = 0
    for l in range(r):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

    #pygame.draw.line(surface, (160,82,45), (0,668), (1024,668), 5)
    
#def clear(self):
    self.win.fill(self.color)

def redrawWindow():
    win.blit(levelBackground, (0,0))
    game.player.draw(win)
    game.player.tt_projectiles1.draw(win)
    game.player.tt_projectiles2.draw(win)
    game.tt_monsters.draw(win)
    game.player.update_health_bar(win)
    for projectile in game.player.tt_projectiles1:
        projectile.move_g()

    for projectile in game.player.tt_projectiles2:
        projectile.move_d()

    for monster in game.tt_monsters:
        monster.deplaM()
        monster.update_health_bar(win)

    for plat in level.fruits_list :
        plat.draw(win)

    for plat in level.wall_list :
        plat.draw(win)

    for decor in level.decor_list :
        decor.draw(win)

def main():
    # Game runing variables
    running = True
    
    inGame = game.is_playing
    inMenu = game.menu
    finMenu = False
    game_Over = game.game_over 
    est_vivant = game.player.health >= 1
    while running:
        
        if inGame:
            
            redrawWindow()

            game.player.gravite()
            game.player.nb_projectiles += 1

            if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < win.get_width():
                    game.player.moveRight()

            elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
                    game.player.moveLeft()  

                

            for event in pygame.event.get():
                if event.type == QUIT:
                    inGame = False
                    pygame.display.quit()
                    pygame.quit()
                    runnig = False
                if event.type == KEYDOWN:
                    game.pressed[event.key] = True
                    if event.key == pygame.K_UP:
                        game.player.a_sauter=True
                        game.player.nb_saut -= 1
                    if event.key == pygame.K_w:
                        if game.player.nb_projectiles >= 30:
                            game.player.lancer_projectile1()
                            game.player.nb_projectiles = 0
                    if event.key == pygame.K_x:
                        if game.player.nb_projectiles >= 30:
                            game.player.lancer_projectile2()
                            game.player.nb_projectiles = 0
                        
                        
                        
                elif event.type == KEYUP:
                    game.pressed[event.key] = False

            game.player.moveSaut()             
            
              
        else:      
            inGame = False
            game.player.est_vivant= False

        if inMenu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    inMenu = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == KEYDOWN:      
                    if event.key == pygame.K_SPACE:
                        inMenu = False
                        inGame = True
                        game.player.est_vivant= True
                        print(inGame)
            win.fill((0,0,0))
            win.blit(menuBackground, (0,0))
        
        elif not game.player.est_vivant:
            for event in pygame.event.get():
                if event.type == QUIT:
                    inMenu = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE :
                        inMenu = True
                        inGame = False
            win.fill((0,0,0))
            win.blit(gameOver, (0,0))
            

        

        
            
        pygame.display.update()
        pygame.time.delay(2)
        clock.tick(60)

main()