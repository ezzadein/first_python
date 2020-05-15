import math
from pygame import mixer
import random
import pygame
import time
pygame.init()

win = pygame.display.set_mode((800,600))

pygame.display.set_caption('EzzU')

#badalle A variables
x_2=30
y_2=280
vel_2=0
#badalle B variables
x=780
y=270
vel=0
#ball variables
ball_x=400
ball_y=300
start_x=400
start_y=300
ball_vel=5
ball_vel_x=5
score_x=300
score_y=20

# Score

score_value = 0
score_2_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10
# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over():
    game_over1 = over_font.render(" GAME  OVER ", True, (255, 255, 255))
    win.blit(game_over1, (220,270))
    
    #time.sleep(5)
def show_score(x, y):
    score = font.render("Score A-B : " + str(score_value )+"-" + str(score_2_value), True, (255, 255, 255))
    win.blit (score, (x, y))
    

# padalle A 
def paddel_a(x,y):
    pygame.draw.rect(win,(255,255,255),(x,y,15,80))

# padalle B
def paddel_b(x,y):
    pygame.draw.rect(win,(255,255,255),(x,y,15,80))

#ball

def ball(x,y):
    pygame.draw.circle(win,(255,255,255),(x,y),15)

#collision conditions
def isCollision(x_2,y_2,ball_x,ball_y):
    distance=math.sqrt((math.pow(x_2-ball_x,2))+(math.pow(y_2-ball_y,2)))
    if distance < 27:
        return True
    else:
        return False

#collision b\n ball and baddle B
def isCollision_2(x,y,ball_x,ball_y):
    distance=math.sqrt((math.pow(x-ball_x,2))+(math.pow(y-ball_y,2)))
    if distance < 50:
        return True
    else:
        return False


run = True

while run:
    pygame.time.delay(50)

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if keystroke is pressed check whether its right or left

        if event.type == pygame.KEYDOWN:
            # padalle B keys
            if event.key == pygame.K_DOWN:
                vel = 20
            if event.key == pygame.K_UP:
                vel = -20
            # padalle A keys
            if event.key == pygame.K_w:
                vel_2= -20
            if event.key == pygame.K_s:
                vel_2 = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                vel = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                vel_2 = 0
    #badalle B boundries & incerementation
    if y <= 0:
        y=0
    if y >= 520:
        y=520 
    y+=vel
    #badalle A boundries & incrementation
    if y_2 <= 0:
        y_2=0
    if y_2 >= 520:
        y_2=520 
    y_2+=vel_2
    #ball boundries and incerementation
    def goal(x,y,a,b):
        x += a
        y += b
    #ball movement
    ball_x+=ball_vel_x
    ball_y+=ball_vel
    if ball_x >= 400 and (ball_y <=10):
        ball_vel=5
    elif ball_x >= 400 and (ball_y >=590):
        ball_vel=-5
    elif ball_x <= 400 and (ball_y <=10):
        ball_vel=5
    elif ball_x <= 400 and (ball_y >=590):
        ball_vel=-5



    # goal scoring
    if ball_x>=820:
        score_value+=1
        ball(start_x,start_y)
        ball_x=start_x
        ball_y=start_y
        goal(ball_x,ball_y,ball_vel,ball_vel_x)
    elif ball_x <= 0:
        score_2_value+=1
        ball(start_x,start_y)
        ball_x=start_x
        ball_y=start_y
    #game winning
    if score_2_value >=3:
        game_over()
        print("player A won!!")
        restart()
        #run=False
    elif score_value >=3:
        game_over()
        print("player B won!!")
        #run=False
    # collision

    collision= isCollision(x_2,y_2,ball_x,ball_y)
    collision_2=isCollision_2(x,y,ball_x,ball_y)
    if collision:
        ball_vel_x=5
        ball_x+=ball_vel_x
    if collision_2:
        ball_vel_x=-5
        ball_x+=ball_vel_x

    show_score(score_x,score_y)
    paddel_a(x_2,y_2)
    paddel_b(x,y)
    ball(ball_x,ball_y)
    pygame.display.update()
pygame.quit()