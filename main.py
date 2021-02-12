import Classes
from Classes import Level
from game import Game
import time
import pygame, sys
from pygame.locals import *
import random

# Variables
width = 1024
height = 768
rows = 32
currentLevel = 2

# Pygame initialization
pygame.init()
pygame.display.set_caption("Le lit perdu")
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Game initialization



def chgmtNiv(lvl):
    level = Level.Level(lvl)
    level.set_LevelPlatformList()
    game = Game(level)
    return (level, game)


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

menuBackground = pygame.image.load('images/menu1.png')
menuBackground = pygame.transform.scale(menuBackground, (width, height))

gameOver = pygame.image.load('images/Game_Over.png')
gameOver= pygame.transform.scale(gameOver, (width,height))

gameWin = pygame.image.load('images/fin_bed.png')
gameWin = pygame.transform.scale(gameWin, (width,height))


def drawGrid(w, r, surface):
    sizeBtwn = w // r
 
    x = 0
    y = 0
    for l in range(r):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

    

def redrawWindow(lvl,level,game):
    
    
    if lvl > 0 :
        win.blit(levelBackground2, (0,0))
    else :
        win.blit(levelBackground, (0,0))
        
    game.player.tt_projectiles1.draw(win)
    game.player.tt_projectiles2.draw(win)
    game.tt_monsters.draw(win)
    
    #drawGrid(width, rows, win)
    #pygame.draw.rect(win, (160,82,45), (0,668,1028,100))
    

    for decor in level.decor_simple_list :
        decor.draw(win)

    for decor in level.decor_collision_list :
        decor.draw(win)

    for projectile in game.player.tt_projectiles1:
        projectile.move_g()

    for projectile in game.player.tt_projectiles2:
        projectile.move_d()

    for monster in game.tt_monsters:
        monster.deplaM()
        monster.update_health_bar(win)

    for f in level.pasteque_list :
        f.draw(win)

    for f in level.banane_list :
        f.draw(win)

    for f in level.orange_list :
        f.draw(win)

    for f in level.fraise_list :
        f.draw(win)

    for f in level.date_list :
        f.draw(win)

    for plat in level.wall_list :
        plat.draw(win)

    game.drawScore(win)

    game.player.draw(win)
    game.player.update_health_bar(win)

def main():
    # Game runing variables
    running = True
    lvle=0
    level,game=chgmtNiv(lvle)

    inGame = game.is_playing
    inMenu = game.menu
    
    game_Over = game.game_over 
    game_Win = game.game_wined
    
    score = 0
    a = 0
    h = 0
    s = 0
    
    
    while running:
        
        if inGame:
            
            redrawWindow(lvle,level,game)  
            game.player.gravite()
            game.player.nb_projectiles += 1

            if not game.player.est_vivant:
                game_Over = True

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

            if game.check_collisionMonstre(game.player, game.all_decors):
                if lvle >= 3:
                    game_Win = True
                    inGame = False
                elif lvle == 0:
                    game.player.checkfruitsGraille()
                    a = game.player.attack
                    h = game.player.health
                    s = game.player.velocity
                    score += game.score
                    lvle += 1
                    level,game=chgmtNiv(lvle)
                    game.updatePerso(a, h, s)
                else :
                    score += game.score
                    lvle += 1
                    level,game=chgmtNiv(lvle)
                    game.updatePerso(a, h, s)

            if lvle == 0 and game.nb_fruits_graille == 5 :
                game.player.checkfruitsGraille()
                a = game.player.attack
                h = game.player.health
                s = game.player.velocity
                score += game.score
                lvle += 1
                level,game=chgmtNiv(lvle)
                game.updatePerso(a, h, s)
                       
            
              
        else:      
            inGame = False
            

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
                        
            win.fill((0,0,0))
            win.blit(menuBackground, (0,0))
        
        elif game_Over:
            game_Over = False
            inGame = True
            level,game=chgmtNiv(lvle)
            game.updatePerso(a, h, s)
            game.player.est_vivant= True
                    
            

        elif game_Win:
            for event in pygame.event.get():
                if event.type == QUIT:
                    inGame = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        pygame.quit()
                        sys.exit()
            win.fill((0,0,0))
            win.blit(gameWin, (0,0))
            win.blit(game.score_text, (600,500))
            

        pygame.display.update()
        pygame.time.delay(2)
        clock.tick(60)

main()