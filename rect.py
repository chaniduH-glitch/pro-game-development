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
object3 = Circle("orange",(50,60),10)


        
class Rectangle():
    def __init__(self,color,size):
        self.screen = screen
        self.c = color
        self.size = size
    def draw(self):
        pygame.draw.rect(self.screen,self.c,self.size)
object1 = Rectangle("red",(0,0,300,400))
object2 = Rectangle("green",(30,40,150,200))
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            object3.draw()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            object1.draw()
            object2.draw()
            pygame.display.update()
        
    screen.fill("blue")
  




    




        


        
        
