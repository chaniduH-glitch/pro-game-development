import pygame 
pygame.init()
pygame.font.init()
pygame.mixer.init()
W,H = 900,500
screen = pygame.display.set_mode((W,H))
White = "white" 
Black = "black"
Yellow = "yellow"
Red = "red"
hit = pygame.mixer.Sound("Grenade+1.mp3")
fire = pygame.mixer.Sound("Gun+Silencer.mp3")
border = pygame.Rect(W//2-5,0,10,H)
font = pygame.font.SysFont("Arial",15)
fps = 60
velocity = 5
bullet_velocity = 7
max_bullets = 3
ssw,ssh = 55,40
yellowhit = pygame.USEREVENT+1
redhit = pygame.USEREVENT+2
yellow_image = pygame.image.load("yellow.png")
yellow_ss = pygame.transform.rotate(pygame.transform.scale(yellow_image,(ssw,ssh)),90)
red_image = pygame.image.load("red.png")
red_ss = pygame.transform.rotate(pygame.transform.scale(red_image,(ssw,ssh)),270)
space = pygame.transform.scale(pygame.image.load("space1.png"),(W,H))
def draw(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(space,(0,0))
    screen.blit(yellow_ss,(yellow.x,yellow.y))
    screen.blit(red_ss,(red.x,red.y))
    pygame.draw.rect(screen,Black,border)
    red_healthtext = font.render("health:"+str(red_health),1,White)
    yellow_healthtext = font.render("health:"+str(yellow_health),1,White)
    screen.blit(red_healthtext,(W-red_healthtext.get_width()-10,10)) 
    screen.blit(yellow_healthtext,(10,10))
    for i in red_bullets:
        pygame.draw.rect(screen,Red,i)
    for i in yellow_bullets:
        pygame.draw.rect(screen,Yellow,i)


    pygame.display.update()
def yellow_move(keyspressed,yellow):
    if keyspressed[pygame.K_a]and yellow.x - velocity > 0: 
        yellow.x -= velocity
    elif keyspressed[pygame.K_d]and yellow.x + velocity+yellow.width < border.x:
        yellow.x+=velocity
    elif keyspressed[pygame.K_w] and yellow.y - velocity > 0: 
        yellow.y -= velocity
    elif keyspressed[pygame.K_s] and yellow.y + velocity+yellow.height < H - 15:
        yellow.y+= velocity

def red_move(keyspressed,red):
    if keyspressed[pygame.K_LEFT]and red.x - velocity > border.x + border.width: 
        red.x -= velocity 
    elif keyspressed[pygame.K_RIGHT]and red.x + velocity + red.width < W:
        red.x += velocity
    elif keyspressed[pygame.K_UP]and red.y - velocity > 0: 
        red.y -= velocity
    elif keyspressed[pygame.K_DOWN]and red.y + velocity + red.height < H-15:
        red.y += velocity
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += bullet_velocity 
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            yellow_bullets.remove(bullet)
        elif bullet.x > W:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= bullet_velocity 
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellowhit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
def win(T):
    text = font.render(T,1,White)
    screen.blit(text,(W/2-text.get_width()/2,H/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

             
run = True
red = pygame.Rect(700,300,ssw,ssh)
yellow = pygame.Rect(100,300,ssw,ssh)
red_bullets = []
yellow_bullets = []
red_health = 10
yellow_health = 10
clock = pygame.time.Clock()
while run:
    clock.tick(fps)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and len(yellow_bullets)<max_bullets:
                bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                yellow_bullets.append(bullet)
                fire.play()
            if event.key == pygame.K_l and len(red_bullets)<max_bullets:
                bullet = pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                red_bullets.append(bullet)
                fire.play()
        if event.type == redhit:
            red_health-=1
            hit.play()
        if event.type == yellowhit:
            yellow_health-=1
            hit.play()
    winner = ""
    if red_health <= 0:
        winner = "yellow wins"
    if yellow_health <= 0:
        winner = "red wins"
    if winner != "":
        win(winner)
        break 
    
    
 
                 
    draw(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    keyspressed = pygame.key.get_pressed()
    yellow_move(keyspressed,yellow)
    red_move(keyspressed,red)
    handle_bullets(yellow_bullets,red_bullets,yellow,red)







    

                               
                               
