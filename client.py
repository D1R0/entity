import pygame
import time
from entity import *
pygame.init()

background_colour = (32,33,36)
win = pygame.display.set_mode((1366,768))
pygame.display.set_caption("ai")
win.fill(background_colour)
pygame.display.flip()
    

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

time_display_start=time.time()
time_in_game=0
total=0
run = True
top=0
x=[]
while run:
    if time_in_game==0:
        for i in range(500):
           x.append(food(win,x)) 
    print("len of entities:",len(x))
    time_in_game+=1
    win.fill(background_colour)
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]:
        x.append(mob(win,x,random.randrange(0,500),random.randrange(0,500),1))
    if keys[pygame.K_f]:
        x.append(food(win,x))
    count=0

    for i in range(len (x)):
        try:
            x[i].life(win,x,time)
            if x[i].type=="mob":
                count+=1
        
            if top<x[i].life_start and x[i].type=="mob":
                top=x[i].life_start
            
        except:
            pass
    if time_in_game%10==0: 
        x.append(food(win,x))

    time_display_stop=time.time()
    time_display=time_display_stop-time_display_start
    
    t_d = myfont.render('%.1f' %time_display, False, (255, 255, 255))
    win.blit(t_d,(0,0))
    

    pygame.display.update() # This updates the screen so we can see our rectangle
    
pygame.quit()