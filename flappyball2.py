import pgzrun 

WIDTH = 600 
HEIGHT= 400

gravity = 2000.0

class Ball():

    def __init__(self,x,y,c):
        self.x = x
        self.y = y 
        self.vx = 200 
        self.vy = 0
        self.radius = 60
        self.c = c 
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.c)
ball = Ball(70,80,"red")
ball2 = Ball(300,280,"blue")
def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
def update(dt):
    uy = ball.vy
    ball.vy+=gravity*dt
    ball.y +=(uy+ball.vy)*0.5*dt
    if ball.y > HEIGHT-ball.radius:
        ball.y = HEIGHT-ball.radius
        ball.vy = -ball.vy*0.9
    ball.x += ball.vx*dt
    if ball.x>WIDTH-ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx
    uy = ball2.vy
    ball2.vy+=gravity*dt
    ball2.y +=(uy+ball2.vy)*0.5*dt
    if ball2.y > HEIGHT-ball2.radius:
        ball2.y = HEIGHT-ball2.radius
        ball2.vy = -ball2.vy*0.9
    ball2.x += ball2.vx*dt
    if ball2.x>WIDTH-ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx
def on_key_down(key):
    if key == keys.DOWN:
        ball.vy = -400
    if key == keys.S:
        ball2.vy = -400
pgzrun.go()