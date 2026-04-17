import pygame
from pygame.locals import * 
import time
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
rocket = pygame.image.load("rocket.png")
space = pygame.image.load("space.png")
rocketx = 200
rockety = 200

keys = [False,False,False,False]
while rockety < 600:
    screen.blit(space,(0,0))
    screen.blit(rocket,(rocketx,rockety))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0]= True 
            elif i.key == K_DOWN:
                keys[1] = True
            elif i.key == K_LEFT:
                keys[2] = True
            elif i.key == K_RIGHT:
                keys[3] = True
        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0]= False
            elif i.key == K_DOWN:
                keys[1] = False
            elif i.key == K_LEFT:
                keys[2] = False
            elif i.key == K_RIGHT:
                keys[3] = False

    if keys[0]:
        if rockety > 0:
            rockety-=7
    elif keys[1]:
        if rockety < 540:
            rockety+=7
    elif keys[2]:
        if rocketx > 0:
            rocketx-=7
    elif keys[3]:
        if rocketx < 540:
            rocketx+=7
    rockety+=4
    time.sleep(0.05)





        
            
