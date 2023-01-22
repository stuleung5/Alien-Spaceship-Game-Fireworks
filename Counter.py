from tkinter import *
from turtle import up
class Counter:
    def __init__(self,c,counter=0):
        self.c=c
        self.counter=counter
        self.d=self.c.create_text(600,50,text=str(self.counter),fill="green",font=("Courier",25))
    def increment(self,a):
        self.counter+=a
        self.c.itemconfig(self.d,text=str(self.counter))
    
    # to complete
#########################
def main(): 
    root = Tk()
    w,h=800,1000
    my_image=PhotoImage(file="space2.png")
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
    x=Counter(canvas,counter=10)
    root.bind("<Left>",lambda e:x.increment(-1))
    root.bind("<Right>",lambda e:x.increment(1))
    
    canvas.pack()
    root.mainloop()
    # to complete
if __name__=="__main__":
    main()
