from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile
def main(): 
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height
        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        ############################################
        ####### start simulation
        ############################################ 
        t=0
        i=0
        while True:
                bo=random.randint(100,300) #Random radius
                x=random.randint(0,w) #Random width for new canvas
                y=h #Height adjusted to new canvas. 
                hei=random.randint(h/4,3*h/4) #Height value now declared for add_explosion.
                speed=random.randint(2,7) #Speed again random. 
                items=["rainbow"] #I decided to only choose rainbow explosions for co. 
                co=random.choice(items)         
                for success in missiles: #For all successful missiles
                        if success.is_active()==True: #If status remains true
                                success.next() #Move
                                if success.is_active()==False: #When status becomes false(after going pass declared height)
                                        Explosion.add_explosion(canvas,booms,success.x,success.y,bo,co) 
                                        """Add explosion. To get coordinates right, do it at the x and y coordinates 
                                        where the missile gets deactivated"""      
                for ignite in booms:
                        ignite.next() #Continue explosion until declared radius is reached.
                while (t%50==0): #0.01*50=0.5 seconds, so every 0.5 seconds, a new missile strikes
                        Missile.add_missile(canvas,missiles,x,y,hei,speed,co)
                        y=y+speed
                        t=t+1 #prevent continuous loop. 
                t=t+1 #increment by 1. 
                y=y+speed
                root.update()
                time.sleep(0.01)
        root.mainloop()




        ### To complete







        

if __name__=="__main__":
    main()


