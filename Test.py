import pygame
import time
import random
# initiating the window
pygame.init()
gray=(119,118,110)
red = (255,0,0)
black = (0,0,0)
# specifying what will be the width and the height of the window
display_width = 800
display_height = 600
# Passing the above to the variables
gamedisplays = pygame.display.set_mode((display_width,display_height))
# setting the name of the window
pygame.display.set_caption("Dodge Game")
#
clock = pygame.time.Clock()
# Inorder to Load image store it in the variables
caring = pygame.image.load('car1.jpg')
backgroundpic= pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
#defning car width from image parameters to provide restriction
car_width = 56


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic = pygame.image.load("carpolice.jpg")
    elif obs==1:
        obs_pic = pygame.image.load("carpolice.jpg")
    elif obs==2:
        obs_pic = pygame.image.load("carpolice.jpg")
    elif obs==3:
        obs_pic = pygame.image.load("carpolice.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font = pygame.font.SysFont(None,25)
    text = font.render("Escaped "+str(passed),True,black)
    score = font.render("Bounty "+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))


#Text details of message box
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("BUSTED!!!")
#function for background image
def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))


#define a function for car
def car(x,y):
    gamedisplays.blit(caring,(x,y))
    #blit enters the image into the window on x y coordinate
#starting with the game loop

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)
    #In order to move car we need to assign some variables
    #And we need to move only on x axis
    x_change = 0
    obstacle_speed=9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(display_width-200))
    obs_starty = -750
    obs_width = 52
    obs_height = 124
    passed = 0
    level = 0
    score = 0
    y2=7
    fps = 72



    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
        #If we press key the left and right will work
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-10
            if event.key==pygame.K_RIGHT:
                x_change=10
            if event.key==pygame.K_a:
                y_change+=2
            if event.key==pygame.K_b:
               obstacle_speed-=2
        if event.type==pygame.KEYUP:
            #If key not pressed then no change it shown by Keyup
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
        #change value of x
        x+= x_change
        pygame.display.set_mode().fill(gray)
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed

        background()
        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
# If a object is comming with certain pixel speed so speed of y axis shou;d also increase
        #providing restriction boundary
        if x>690- car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty = 0-obs_height
            obs_startx = random.randrange(170,(display_width-170))
            obs = random.randrange(0,3)
            passed = passed+1 #After each car passed
            score = passed*10
            if int(passed/10==0):
               level = level+1
               obstacle_speed+2
               largetext = pygame.font.Font("freesansbold.ttf",80)
               textsurf,textrect=text_objects("LEVEL "+str(level),largetext)
               textrect.center=((display_width/2),(display_height/2))
               gamedisplays.blit(textsurf,textrect)
               pygame.display.update()
               time.sleep(3)

        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx+obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()

        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
