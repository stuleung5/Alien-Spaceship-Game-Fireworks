from tkinter import *

class SpaceShip:
    def __init__(self,c):
        self.c=c
        self.__active=False
        self.ship_image=PhotoImage(file="ship.png")
        self.space_image=PhotoImage(file="space2.png")
        self.w2=self.space_image.width()
        self.h2=self.space_image.height()
        ws=self.ship_image.width()
        self.hs=self.ship_image.height()
        self.d=self.c.create_image(self.w2/2,self.h2-ws*3.1,anchor=NW,image=self.ship_image,tags="ship")
        self.other=self.ship_image.subsample(3, 3)
        self.bonus=self.c.create_image(0,0,anchor=NW,image=self.other,tags="bonus_ship1")
        self.bonus=self.c.create_image(30,0,anchor=NW,image=self.other,tags="bonus_ship2")
        self.bonus=self.c.create_image(60,0,anchor=NW,image=self.other,tags="bonus_ship3")
        self.x=self.w2/2
        self.y=self.h2-ws*3.1
    def activate(self):
        self.__active=True
    def deactivate(self,a):
        if a=="destruction":
            self.c.delete("ship")
            self.__active=False
        if a==3:
            self.c.delete("bonus_ship3")
        if a==2:
            self.c.delete("bonus_ship2")
        if a==1:
            self.c.delete("bonus_ship1")
    def is_active(self):
        return self.__active
    def shift_left(self):
        if self.x>5:
            self.c.move(self.d,-15,0)
            self.x-=15
        else:
            self.c.move(self.d,0,0)
    def shift_right(self):
        if self.x<7*self.w2/8:
            self.c.move(self.d,15,0)
            self.x+=15
        else:
            self.c.move(self.d,0,0)
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
    
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)

    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

