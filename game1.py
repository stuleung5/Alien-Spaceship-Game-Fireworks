from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *
########## global variable
game_over=False
######### Functions
record={"blue":0,"red":0,"green":0,"purple":0}
def stop_game(canvas):
    global game_over
    game_over=True
    if game_over==True:
        #This creates GAME OVER sign. If game over happens.
        canvas.create_text(635/2,960/2.5,text="GAME OVER",fill="orange",font=("Courier",100))
        print(record)
def shoot(canvas,aliens,booms,ammunition,x,y,list_for_tuple):
    #I set default values to prevent any mixing of colors or mixing of point values.  
    default_color="white"
    default_reduction=-3
    for boom in booms:
        boom.next()
    for createalien in aliens:
            if createalien.is_active()==True and createalien.is_shot(x,y)==True: #If alien is active and shot
                default_color=createalien.co #Default color changes before add_explosion.
                default_reduction=0 #Default_reduction goes to zero, so if default_reduction and createalien.point mix(combine). +0 does nothing. 
                Explosion.add_explosion(canvas,booms,x,y,30,default_color)            
                createalien.deactivate() #Deactivate alien.
                ammunition.increment(createalien.point)
                #Increment by 1 if alien is of a certain color. 
                if createalien.co=="red":
                    record[createalien.co]+=1
                if createalien.co=="blue":
                    record[createalien.co]+=1
                if createalien.co=="green":
                    record[createalien.co]+=1
                if createalien.co=="purple":
                    record[createalien.co]+=1
                list_for_tuple.append(record["red"]) #Create list of tuples.
                f1=open("game1.txt","a")
                f1.write( str(record["red"])+" "+str(record["blue"])+" "+str(record["green"])+" "+str(record["purple"])+"\n" )
                f1.close()
            if createalien.is_active()==True and createalien.is_shot(x,y)==False and ammunition.counter>=0: #If alien has missed. 
                ammunition.increment(default_reduction) #Reduce by -3
                Explosion.add_explosion(canvas,booms,x,y,30,default_color) #White explosion
                if ammunition.counter<=0:
                    stop_game(canvas) #Stop game if counter is 0 or below
                    print(record)
                    break #Break to stop any more point reductions. 
                break #Break to stop any more point reductions if game continues.
        
        
    
    ####### to complete


################
    
def main():    
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        #my_image=PhotoImage(file="space1.png")
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        ammunition=Counter(canvas,10)
        
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,ammunition,e.x,e.y,list_for_tuple))
        root.bind("<Escape>",lambda e:stop_game(canvas))
        ############################################
        ####### start simulation
        ############################################
        #To complete (time sleep is 0.01s)
        t=0
        list_for_tuple=[]
        while True:
            while t%50==0:  
                aliens+=[Alien.add_alien(canvas,aliens)] #Add alien to list. 
                #list_for_tuple.append(tuple([record["red"],record["blue"],record["green"],record["purple"]]))
                t=t+1 #Avoid infinite loop.
            for createalien in aliens:
                createalien.next() #Next to unleash more aliens. 
                
            for boom in booms:
                boom.next() #Next unleash more explosions. 
              #update the graphic (redraw)
            root.update()
            time.sleep(0.01)
            t=t+1 #Increment to 50.  
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

