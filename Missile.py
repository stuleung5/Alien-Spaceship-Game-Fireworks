from tkinter import *
import time,random
class Missile:
    #### to complete
    """I initialized variables using self"""
    def __init__(self,c,hei=0,speed=5,co="orange",wofm=8,heofm=25):
        self.c=c##canvas
        self.hei=hei##ceiling height
        self.speed=random.randint(2,7)##pixel increment
        self.co=co##color
        self.wofm=wofm##width
        self.heofm=heofm##height
        self.speed=speed
        self.__active=False
        self.missiles=[]
    """For activate, I made sure x-coordinate is center by subtracting by half the width and adding half the
    width. Since, y is suppose to represent bottom of missile, I did y and then y minus the height"""
    def activate(self,x,y):
        self.x=x ##x coordinate
        self.y=y# y coordinate
        self.missiles=self.c.create_rectangle(x-self.wofm/2,y,x+self.wofm/2,y-self.heofm,fill=self.co,outline=self.co)
        self.__active=True
    """I delete missiles if this method is called up"""
    def deactivate(self):
        self.__active=False
        self.c.delete(self.missiles)
    """Returns status of a missile"""
    def is_active(self):
        return self.__active
    """If the status of missile is true. I increase it by a speed(determined randomly). I also adjust y-coordinate. 
    If the missile's top height is less than height of canvas, then the missile deactivates"""
    def next(self):
        if (self.__active==True):
            self.c.move(self.missiles,0,-self.speed)
            self.y=self.y-self.speed
        if (self.y<=self.hei+self.heofm):
            self.deactivate()
    """This adds a missile with a random x-coordinate and a random speed. There is also random colors and a random 
    height. There are some exceptions, so this static method works for other classes."""
    @staticmethod
    def add_missile(c,missiles,x,y,hei=0,speed=5,co="orange"): #c=canvas, l=list, x,y coordinates, height of canvas, pixel increment, color
        """For Game 2, to get the missile to shoot properly, if the missile is not 800, then the x-coordinate will 
        remain stable.""" 
        if x==800: 
            x=random.randint(25,x-25)
        """Again, for Game 2, to move the missile more quickly like in the video for Game 2, if the speed has been
        declared 8 or greater, then there is no random speed."""
        if speed<8:
            speed=random.randint(2,7)
        items=["red","orange","yellow","green","blue","purple"]
        if (co=="choose orange"): #This is for game2.py. I saw that missiles were all oranges in example. 
            co="orange"
        else:
            co=items[random.randint(0,5)]
        if hei==0: #For fireworks, if height had already been declared as a value other than 0, then there is no random.
            hei=random.randint(0,y)
        #I instantiate the missile and then activate it. 
        Gr=Missile(c,hei,speed,co)
        Gr.activate(x,y)
        i=0
        while True:
            j=len(missiles)
            if i==0 or i>=j:
                break #If missiles is 0, then there should be no deletion. 
            else:
                missiles.pop(i) #Remove missiles from list.
                i=i+1
        missiles.append(Gr) #Add Gr to missiles
        return Gr
    
###################################################
###################################################        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock       
        while True:
           ##### To complete
            for Gr in missiles:
                Gr.next()
            for b in missiles:
                print(b.is_active(),end=" ")
            print()
            while (t%50==0):
                Missile.add_missile(canvas,missiles,w,h)
                t+=1
            # check active status of list of booms (for debugging)
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
if __name__=="__main__":
    main()

