import pygame
pygame.init()
import time

W = 600
H = 400
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("merry christmas")    
xmascard = pygame.image.load("xmascard.jpg")
xmascard1 = pygame.transform.scale(xmascard,(W,H))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    screen.blit(xmascard1,(0,0))
    font = pygame.font.SysFont("calibri",25)
    text = font.render("merry christmas", True,"dark blue")
    screen.blit(text,(200,200))
    pygame.display.update()
    time.sleep(2)

    tree = pygame.image.load("xmastree.jpg") 
    tree1 = pygame.transform.scale(tree,(W,H))
    screen.blit(tree1,(0,0))
    text1 = font.render("merry christmas and a happy new year",True,"red")
    screen.blit(text1,(200,10))
    pygame.display.update()
    time.sleep(2)


