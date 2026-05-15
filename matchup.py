import pygame

pygame.init()
w = 600 
h = 700  
screen = pygame.display.set_mode((w,h))
screen.fill("white")
subway = pygame.image.load("subway.png")
templerun = pygame.image.load("templerun.png")
ludo = pygame.image.load("ludo.png")
candycrush = pygame.image.load("candycrush.jpg")
screen.blit(subway,(50,40))
screen.blit(templerun,(50,140))
screen.blit(ludo,(50,240))
screen.blit(candycrush,(50,340))
font = pygame.font.SysFont("Arial",30)
text1 = font.render("Subway Surfers",True,"black")
text2 = font.render("Temple Run",True,"black")
text3 = font.render("Ludo",True,"black")
text4 = font.render("Candycrush",True,"black")
screen.blit(text3,(250,50))
screen.blit(text1,(250,150))
screen.blit(text4,(250,250))
screen.blit(text2,(250,350))

pygame.display.update()

while True:
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"black",(pos),30)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,"black",(pos),(pos2),10)
        pygame.draw.circle(screen,"black",(pos2),30) 
        pygame.display.update()

        

        


 
