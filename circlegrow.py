import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
class Circle():
    def __init__(self,colour,position,size):
        self.screen = screen
        self.c = colour
        self.size = size
        self.p = position
    def draw(self):
        pygame.draw.circle(self.screen,self.c,self.p,self.size)
    def grow(self):
        self.size +=10
        pygame.draw.circle(self.screen,self.c,self.p,self.size)

object1 = Circle("red",(50,60),10) 
run = True
while run:
     for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            object1.draw()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            object1.grow()
            
            pygame.display.update() 


        
