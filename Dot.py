########################
## Team Members
## Name1:          
## Name2:
#########################
from tkinter import *
import random
class Dot:
    ##### TO COMPLETE
    """I intitialized a number of arguments. I set boolean b to default False. Items had a variety of choices.
    When b becomes true by clicking, the x, y, and color features should appear. self.d represents creation of oval
    based on x and y selected coordinates and random color."""
    def __init__(self,c,x,y,co,b=False):
        self.x=x 
        self.y=y 
        self.co=co
        self.c=c
        self.b=b
        if self.co=="red":#I included these three options in case co(color) was already defined. This was helpful for getting color of dots to be one color. 
            self.co=="red"
        if self.co=="blue":
            self.co=="blue"
        if self.co=="green":
            self.co=="green"
        items=["red","orange","yellow","green","blue","white","purple"]
        if (self.co=="rainbow"):
            self.co=random.choice(items) 
        self.d=self.c.create_oval(x-1,y-1,x+1,y+1,fill=self.co, outline = self.co,tags="oval")
        if (b is True):
            print(x,y,self.co) #I printed out coordinates and colors here.

#################################################################
#################################################################  
def main(): 
    ##### create a window, canvas
    root = Tk() # instantiate a tkinter window
    canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
    canvas.pack()
    root.update()   # update the graphic
    #canvas.create_rectangle(100,400,400,100,outline="white")
    # Tkinter binding action (mouse click)
    root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
    
    root.mainloop() # wait until the window is closed
if __name__=="__main__":
    main()

