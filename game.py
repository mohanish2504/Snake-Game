# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame 
import time
import random

pygame.init()

screensize = (800,600)
display = pygame.display.set_mode(screensize)
pygame.display.update()



blue=(0,0,255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

blocksize = 20

snake_x = 100
snake_y = 100

food_x = 0
food_y = 0

snake_x_change = 0
snake_y_change = 0

pos = [snake_x,snake_y]
snake_size = 1;

clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [screensize[0]/2, screensize[1]/2])
 
def checkBorderhit(pos):
    if pos[0] == 0 or pos[0] == screensize[0] or pos[1] == screensize[1] or pos[1]==0 : return True
    return False

def changefood():
    global food_x,food_y 
    food_x = round(random.randrange(0, screensize[0] - blocksize) / 20) * 20
    food_y = round(random.randrange(0, screensize[1] - blocksize) / 20) * 20
    
def selfHit(snakebody,currentposition):
    for x in snakebody[:-1]:
        if x== currentposition: return True
    return False

def placeSnake(snakebody):
    for pos in snakebody[:-1]:
        pygame.draw.rect(display, black, [pos[0], pos[1], blocksize, blocksize],border_radius=20)
    pygame.draw.rect(display, black, [snakebody[-1][0], snakebody[-1][1], blocksize, blocksize],width=1,border_radius=20)

def gotfood(pos):
    if pos[0] == food_x and pos[1]==food_y:return True
    return False
    
gamerunning = True
changefood()

snakebody = []


while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and (snake_x_change != -blocksize or snake_size==1):
                snake_x_change = blocksize
                snake_y_change = 0
            if event.key == pygame.K_a and (snake_x_change != blocksize or snake_size==1):
                snake_x_change = -blocksize
                snake_y_change = 0
            if event.key == pygame.K_w and (snake_y_change != blocksize or snake_size==1):
                snake_x_change = 0
                snake_y_change = -blocksize
            if event.key == pygame.K_s and (snake_y_change != -blocksize or snake_size==1):
                snake_x_change = 0
                snake_y_change = blocksize             
    snake_x += snake_x_change
    snake_y += snake_y_change
    pos = [snake_x,snake_y]  
    
    snakebody.append(pos)
    
    if len(snakebody) > snake_size :
       del snakebody[0]
    
    if selfHit(snakebody,pos):
        gamerunning = False
    
    if checkBorderhit(pos): gamerunning = False
    
    if gotfood(pos): 
        snake_size+=1
        changefood()
        
    
    
    display.fill(white)
    placeSnake(snakebody)
    #pygame.draw.rect(display, black, [pos[0], pos[1], blocksize, blocksize])
    pygame.draw.rect(display, blue, [food_x, food_y, blocksize*0.9, blocksize*0.9],border_radius=20)
    
    pygame.display.update()
    
    clock.tick(15)
    
message("You lost",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
