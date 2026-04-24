import pygame
import time
from pygame.locals import *
pygame.init()

W = 400
H = 400

screen = pygame.display.set_mode((W,H))
fish   = pygame.image.load("fish2.png")
ocean  = pygame.image.load("ocean.jpg")
fishx = 200
fishy = 200

keys = [False,False,False,False]
while fishy < 400:
    screen.blit(ocean,(0,0))
    screen.blit(fish,(fishx,fishy))
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
        if fishy > 0:
            fishy-=9
    elif keys[1]:
        if fishy < 540:
                 
            fishy+=9
    elif keys[2]:
        if fishx > 0:
            fishx-=9
    elif keys[3]:
        if fishx < 540:
            fishx+=9
    fishy+=4
    time.sleep(0.05)


