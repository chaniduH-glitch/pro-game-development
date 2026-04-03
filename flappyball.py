import pgzrun 

WIDTH = 600
HEIGHT = 400

gravity = 2000.0

class Ball():

    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.vx = 200 
        self.vy = 0
        self.radius = 60
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"red")
ball = Ball(50,100)
def draw():
    screen.clear()
    ball.draw()
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
def on_key_down(key):
    if key == keys.DOWN:
        ball.vy = -500
pgzrun.go()



    



        