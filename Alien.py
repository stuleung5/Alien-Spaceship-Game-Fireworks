from tkinter import *
import math
import time, random
class Alien:
    ### to complete
    """I initialized variables with self. like in the previous classes. I also added images for each of the aliens. I used canvas
    to create a yellow rectangle. I also have a random self.x. Finally, I used .width() and .height() to get the width and height
    of image. """
    def __init__(self,c,increment=4,co="yellow",w=50,h=50,point=1):
        self.c=c
        self.increment=increment
        self.co=co
        self.w=w
        self.h=h
        self.point=point
        self.my_image=PhotoImage(file="space2.png")
        self.width=self.my_image.width()
        self.height=self.my_image.height()
        self.x=random.randint(0+self.w/2,self.width-self.w/2)
        self.redimage=PhotoImage(file="alien_red.png")
        self.greenimage=PhotoImage(file="alien_green.png")
        self.blueimage=PhotoImage(file="alien_blue.png")
        self.image=PhotoImage(file="alien-g7e6b14b81_640.png",)
        self.y=0
        self.adjust=0
        self.alienlist=[]
    def activate(self):
        self._active=True#Set to true
        if (self.co=="yellow"):
            self.d=self.c.create_rectangle(self.x-self.w/2,self.y,self.x+self.w/2,self.y+self.h,fill=self.co,outline=self.co,tags="yellow")
            self.alienlist.append(self.d)
    def is_active(self):
        return self._active#Return boolean
    def deactivate(self):
        self._active=False#Set to false
        self.c.delete(self.d)
        #for remove in self.alienlist:
            #self.c.delete(remove)#Delete aliens using self.d
    def next(self):
        if (self._active==True):
            try:
                self.new=self.c.move(self.d,0,self.increment)#If true, move down by self.increment.
            except:
                pass
            self.x+=0#Adjust x-coordinate
            self.y+=self.increment#Adjust y-coordinate
            if self.y>self.height*3/4+20: #If height is too much for this
                self.deactivate()
                self.y=0
                self.x=random.randint(self.w/2,self.width-self.w/2)
                self.activate()
            #return self.new
    """Uses the fact that x-coordinate of images is at the center, so I have -width/2 and +width/2. y-coordinate of images
    is at the top, so y on its own and y+height representing bottom. """
    def is_shot(self,x,y):
        if (self.x-self.w/2<=x<=self.x+self.w/2 and self.y<=y<=self.y+self.h): 
            return True
        else:
            return False
    @staticmethod
    def add_alien(c,aliens):
        aliens=[Alien_red(c),Alien_green(c),Alien_blue(c),Alien_mine(c)] #Randomly choosing an alien
        choice=aliens[random.randint(0,3)] 
        choice.activate() #Activate random instantiation.
        i=0 
        while True:
            j=len(aliens) 
            if i==0 or i>=j: #If i is 0, then no deletion should happen. Meanwhile, if i is greater than 80, deletion should not happen.
                break
            if not aliens[i].is_active():
                aliens.pop(i) #Otherwise, remove and return value
            else:
                i=i+1 #Increments from 0 to 80
        aliens.append(choice) ##Add boom from instantiation."""
         #Returns value of list.
        return choice
        
################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,c):
        self.c=c
          # keep a reference (avoid garbage collector)
        super().__init__(self.c,increment=4,co="red",w=50,h=50,point=2)
        self.c.delete("yellow")
        self.d=[] #I created this list, so that lists of different aliens can be used for game1 and game2. 
        # contstructor to complete
    # to complete
    def activate(self):
        self._active=True
        """Here I created the new images for each alien. After all, the next Alien classes all have the parent class
        of Alien_red, not Alien.""" 
        if self.co=="red":
            self.d=self.c.create_image(self.x,self.y+self.h/2,anchor=CENTER,image=self.redimage)
        if (self.co=="green"):
            self.d=self.c.create_image(self.x,self.y+self.h/2,anchor=CENTER,image=self.greenimage)
        if (self.co=="blue"):
            self.d=self.c.create_image(self.x,self.y+self.h/2,anchor=CENTER,image=self.blueimage)
        if (self.co=="purple"):
            self.d=self.c.create_image(self.x,self.y+self.h/2,anchor=CENTER,image=self.image)
        
###############################################################
###############################################################

class Alien_green(Alien_red):
    def __init__(self,c):
        self.c=c
        Alien.__init__(self,c,increment=4,co="green",w=50,h=50,point=4) #I create a new Alien __init__.
    # to complete
    def next(self):
        self.move=random.randint(-5,5) #I used a random move value. 
        if (self._active==True):
            self.c.move(self.d,self.move,self.increment) #This should move randomly. 
            self.y+=self.increment #Increment x and y-coordinates to make sure hit is accurate
            self.x+=self.move 
            if (self.y>self.height*3/4+20): #If alien reaches bottom of canvas, deactivate alien. Also, activate a new alien with a different self.x value.
                self.deactivate()
                self.y=0
                self.x=random.randint(self.w/2,self.width-self.w/2)
                self.activate()
###############################################################
###############################################################
class Alien_blue(Alien_red):
    def __init__(self,c):
        self.c=c
        Alien.__init__(self,c,increment=4,co="blue",w=50,h=50,point=3) #I create a new Alien __init__.
        self.theta=random.randrange(-160,-20) #I use create a random angle.
        self.theta=self.theta/360*(2*math.pi) #I change from degrees to radians.
    # to complete
    def next(self):
        if (self._active==True):
            theta=self.theta #If alien is active, theta becomes self.theta(default)
            increment=self.increment #If alien is active, increment becomes self.increment(default)
            while (self.x-self.w/2<0):
                self.theta=math.pi-theta #If hitting to the left, self.theta changes to 180-theta.
                break
            while (self.x+self.w/2>self.width):
                self.theta=-1*math.pi-theta #-180-theta if hit to the right. 
                increment=-1*increment #Change increment to -1 to ensure alien moves left. 
                break
            #This is where movement takes place. I make sure the y value is always increasing. self.increment is postive or negative
            #based on whether it hits the right side of image. 
            self.c.move(self.d,self.increment*math.cos(self.theta),abs(self.increment*math.sin(self.theta))) 
            self.x+=self.increment*math.cos(self.theta)
            self.y+=abs(self.increment*math.sin(self.theta))
            while (self.x-self.w/2<0):
                self.theta=math.pi-theta
                self.increment*=-1
                break
            while (self.x+self.w/2>self.width):
                self.theta=-1*math.pi-theta
                self.increment=-1*increment
                break
            if (self.y>=self.height*3/4+20): #If alien reaches bottom of canvas
                self.deactivate() #Deactivate 
                self.y=0
                self.x=random.randint(self.w/2,self.width-self.w/2) 
                self.activate() #Start a new alien at the top with a random x coordiante.

class Alien_mine(Alien_red):
    """M For this, I have an image created initally at specific x-coordinates. The image randomness
    has also increased. This creates more evasive moment. """
    def __init__(self,c):
        self.c=c
        Alien.__init__(self,c,increment=8,co="purple",w=50,h=50,point=5)
    def next(self):
        self.move=random.randint(-15,15) #I used a random move value. 
        if (self._active==True):
            self.c.move(self.d,self.move,self.increment)
            self.y+=self.increment
            self.x+=self.move 
            if (self.y>self.height*3/4+20):
                self.deactivate()
          
###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
    print(x,y,result)
    
def main(): 
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        #Initialize alien
        #alien=Alien(canvas)
        alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)
        #alien=Alien_mine(canvas)
        alien.activate()
        
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        t=0               # time clock
        
        while True:
            if (not alien.is_active()):
                alien.activate()
            alien.next() # next time step
            root.update()  # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

