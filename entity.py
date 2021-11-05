import pygame
import random 
import math
import os

class mob:
    
    def __init__(self,win,id,pos_x,pos_y,speed):
        self.id=len(id)
        self.type="mob"
        self.width=5
        self.height=5
        self.win=win
        self.x=pos_x
        self.y=pos_y
        if(speed>0):
            self.w=speed
        else:
            self.w=1
        self.r=0
        self.g=255-255/self.w
        self.b=255/math.sqrt(self.w)
        self.target=False
        self.find=None
        self.view=1300
        self.distance_t=self.view
        self.hunger=True
        self.life_start=0
        self.life_span=random.randrange(150,200)

    def life(self,win,world_entity,time):

        #Find the new target
        for j in world_entity:
            try:
                if j.type=="food" and self.hunger==True:
                    self.distance=math.sqrt((j.x-self.x)*(j.x-self.x)+(j.y-self.y)*(j.y-self.y))

                    if self.distance_t>=self.distance:                       
                        self.distance_t=self.distance
                        self.find=j #find target


                elif j.type=="mob" and j.hunger==False and self.hunger==False and self!=j:                  
                    self.distance=math.sqrt((j.x-self.x)*(j.x-self.x)+(j.y-self.y)*(j.y-self.y))
                    if self.distance_t>=self.distance:                       
                        self.distance_t=self.distance
                        self.find=j #find target

                    
            except:
                pass

        
        try:
            #Inactive behavior
            if self.target==False:
                self.h=random.randrange(-1,1)
                self.v=random.randrange(-1,1)
                if self.h:
                    self.x-=1
                else:
                    self.x+=1
                if self.v:
                    self.y-=1
                else:
                    self.y+=1
            if self.find and self.find.id:
                self.target=True

            #Go to target
            if self.target==True and self.find.type!="death":
                self.m=random.randrange(-1,1)
                if self.x>self.find.x:
                    if self.m:
                        self.x-=self.w*2
                    else:
                        self.x-=self.w
                else:
                    if self.m:
                        self.x+=self.w*2
                    else:
                        self.x+=self.w

                if self.y>self.find.y:
                    if self.m:
                        self.y-=self.w*2
                    else:
                        self.y-=self.w
                else:
                    if self.m:
                        self.y+=self.w*2
                    else:
                        self.y+=self.w

            #Find new target
            elif self.find.type=="death": 
                self.find=None
                self.target=False
                self.distance_t=self.view

            #Eating
            if abs(self.find.x-self.x)<5 and abs(self.find.y-self.y)<5 and self.find.type=="food":
                self.find.type="death"
                self.find.x=-5
                self.find.y=-5
                self.target=False
                world_entity.remove(self.find)
                self.find=None
                self.distance_t=self.view
                self.hunger=False
                self.life_span+=(self.life_span-self.life_start)/2
            
            #Event
            if abs(self.find.x-self.x)<5 and abs(self.find.y-self.y)<5 and self.find.type=="mob":
                self.target=False
                self.find=None
                self.distance_t=self.view
                self.hunger=True
                self.test=random.randint(0,1)
                if self.test:
                    world_entity.append(mob(win,world_entity,self.x,self.y,(self.w+random.randint(-1,2))))


        except:
            pass
        self.life_start+=1
        if self.life_start>=self.life_span:
            self.type="death"
            world_entity.remove(self)

            
        pygame.draw.rect(self.win, (self.r,self.g,self.b), (self.x, self.y, self.width, self.height))

        


class food:
    def __init__(self,win,id):
        self.id=len(id)
        self.type="food"
        self.target=False
        self.width=2
        self.height=2
        self.win=win
        self.x=random.randrange(0,1366)
        self.y=random.randrange(0,768)
        self.w=5
        self.r=22.4
        self.g=255
        self.b=7.8

    def life(self,win,target,time):


        pygame.draw.rect(self.win, (self.r,self.g,self.b), (self.x, self.y, self.width, self.height))

