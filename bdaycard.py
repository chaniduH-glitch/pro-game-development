import pygame
pygame.init()
import time

W = 600
H = 400
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Happy Birthday")    
bday = pygame.image.load("bday card.jpg")
bday1 = pygame.transform.scale(bday,(W,H))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bday1,(0,0))
    font = pygame.font.SysFont("calibri",25)
    text = font.render("happy birthday", True,"dark blue")
    screen.blit(text,(200,200))
    pygame.display.update()
    time.sleep(2)

    cake = pygame.image.load("cake.jpg") 
    cake1 = pygame.transform.scale(cake,(W,H))
    screen.blit(cake1,(0,0))
    text1 = font.render("have a good birthday",True,"red")
    screen.blit(text1,(200,10))
    pygame.display.update()
    time.sleep(2)



    



