from telnetlib import XASCII
from tkinter import *
import math,time,random
from Dot import Dot
import numpy as np 
class Explosion:
    #### to complete
    def __init__(self,c,co,max_rad=80):
        self.c=c
        self.max_rad=max_rad#Set max radius
        self.co=co#Set color
        self.layer=15#Each radius should have 15 dots. 
        self.booms=[]#Setting default valumes for r, booms, and active
        self.dotlist=[]#Set empty list of explosions.
        self._active=False #Set active to default false. #Made this protected for Explosion_gravity to work.
    def activate(self,x,y):
        self.x=x #Set x-coordinates
        self.y=y #Set y-coordinates
        self.starting_radius=0 #Set default radius at 0. 
        self._active=True #Change to true. #Made this protected for Explosion_gravity to work. 
    def deactivate(self): 
        self._active=False ##Set to false
        for dot in self.dotlist: #For indexes in dotlist
            self.c.delete(dot.d) #Delete the index with d.
    #I return self.__active in is_active 
    def is_active(self):
            return self._active #Return boolean
    def next(self):
        i=0
        if (self._active==True) and (self.starting_radius<=self.max_rad): #If radius is not over 80 pixels and active is true, I create a 
            #new x and y coordinate with a new oval starting at x and y. I append this to my list.
            while (i<=self.layer): #Radius 0 to 15 
                theta=random.randint(1,360) #Random radius
                newx=self.x+self.starting_radius*math.cos(theta/360*(2*math.pi)) #New x-coordinate
                newy=self.y+self.starting_radius*math.sin(theta/360*(2*math.pi)) #New y-coordinate
                self.d=Dot(self.c,newx,newy,self.co,"True") #Use Dot class to create dot. 
                self.dotlist.append(self.d) #Append to list in self.dotlist.
                i=i+1 #Increment i from 0 to 15. 
            self.starting_radius+=1 #Increment from 0 to 80
        else:
            self.deactivate() #If conditions are not met, deactivate occurs. 
    @staticmethod
    def add_explosion(c,booms,x,y,max_rad=80,co="rainbow"):
        #boom=Explosion(c,co,"True",max_rad) ##Instantiates boom
        #boom=Explosion_gravity(c,co)
        choices=[Explosion(c,co,max_rad),Explosion_gravity(c,co)]
        boom=choices[random.randint(0,1)]
        boom.activate(x,y) #Activates x and y with new self variables and setting active to True.
        boom.next()
        i=0 
        while True:
            l=len(booms) 
            if i>=l: #If explosion is greater than length of list, then there should be no deletion
                break
            if booms[i].is_active()==False: #If explosion is false, then I'll get rid of explosion. 
                booms.pop(i) #Removes False statements after a new click.
            else:
                i=i+1 #Increment by 1 to keep up with l. 
        booms.append(boom) #Add boom to list of booms. 
class Explosion_gravity(Explosion):
    def __init__(self,c,co,max_time=40):
        super().__init__(c,co)
        self.starting_radius=0
        np.speed = np.random.randint(1,5,15) #Use random numpy method. Creates fifteen random values from 1 to 5. 
        self.max_time=max_time
        np.theta = np.random.randint(0,359,15) #Use random numpy method. Creates fifteen random values from 0 to 359. 
    def next(self):
        i=0 #Start from 0
        if (self._active==True) and (self.starting_radius<=self.max_time): #If explosion is active and radius is less than time.
            while i<self.layer: #From 0 to 14 for array.
                new_gx=self.x+np.speed[i]*math.cos(np.theta[i]/360*(2*math.pi))*self.starting_radius
                new_gy=self.y-np.speed[i]*math.sin(np.theta[i]/360*(2*math.pi))*self.starting_radius+0.06*(self.starting_radius**2)
                self.d=Dot(self.c,new_gx,new_gy,self.co)
                i=i+1 #Increment till 14
                self.dotlist.append(self.d) #Add Dot creation to list
            self.starting_radius+=1 #Increment radius till max time. 
        else:
            self.deactivate() #If conditions are not met, deactivate occurs.
#################################################################
#################################################################
    
def main(): 
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y) )
        ############################################
        ####### start simulation
        ############################################
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
                #b.is_active()
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

