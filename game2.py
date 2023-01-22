from importlib.abc import ResourceReader
from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile
 
########## global variable
game_over=False
######### Function
def stop_game(): #Same in game1.py
    global game_over
    game_over=True 
def stop_game(canvas): #Same in game1.py
    global game_over
    game_over=True
    if game_over==True:
        canvas.create_text(635/2,960/2.5,text="GAME OVER",fill="orange",font=("Courier",100)) #Same in game1.py
def main():    
    ##### create a window, canvas 
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png") 
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    t=0
    blue_int=0
    red_int=0
    green_int=0
    purple_int=0
    record={"blue":0,"red":0,"green":0,"purple":0}
    canvas.create_image(0,0,anchor=NW,image=my_image)
    canvas.pack()
    root.update() 
    #The three lines below are the empty lists for explosions, aliens, and missiles
    list_explosion=[]
    list_missiles=[]
    list_aliens=[]
    list_for_tuple=[]
    #I instantiate and activate SpaceShip. 
    cr_ship=SpaceShip(canvas)
    cr_ship.activate()
    #I instantiate Counter starting with point 0. 
    startcounter=Counter(canvas,0)
    #I used cr_ship to get shift_left() and shift_right().
    root.bind("<Left>",lambda e: cr_ship.shift_left())
    root.bind("<Right>",lambda e: cr_ship.shift_right())
    #I add Missile if I press up. I adjusted coordinates to make sense. I made speed faster. 
    root.bind("<Up>",lambda e:Missile.add_missile(canvas,list_missiles,cr_ship.x+37.5,h-240,1,20,"choose orange"))
    root.bind("<Escape>",lambda e:stop_game(canvas))
    i=3
    while True:
        while (t%100==0): #For every 100 seconds
            list_aliens+=[Alien.add_alien(canvas,list_aliens)] #Add to alien list. 
            t=t+1 #Break infinite loop. 
            list_for_tuple.append(tuple([record["red"],record["blue"],record["green"],record["purple"]]))
            #print(list_for_tuple)
        for boom in list_explosion:
            boom.next() #Continue explosions. 
            if boom.is_active()==False and cr_ship.is_active()==False and startcounter.counter>0: #If explosion is gone and ship is deactivated,
                #Deactivate ship lives.
                if i==2:
                    cr_ship=SpaceShip(canvas)  #Then instantiate and activate ship.
                    cr_ship.activate()
                    cr_ship.deactivate(3)
                if i==1:
                    cr_ship=SpaceShip(canvas)  #Then instantiate and activate ship.
                    cr_ship.activate()
                    cr_ship.deactivate(3)  
                    cr_ship.deactivate(2)
        for cr_alien in list_aliens:
            cr_alien.next() #Continue alines
            if cr_alien.is_active()==True and cr_alien.x-25<cr_ship.x+37.5 and cr_alien.x+25>cr_ship.x-37.5 and cr_alien.y>cr_ship.y-37.5 and 652.5<cr_alien.y and cr_alien.y<727.5:
            #If an alien is active and it fits inside the SpaceShip's coordinates deactivate the ship and cause a rainbow explosion.
                cr_ship.deactivate("destruction")
                startcounter.increment(-10) #Also decrease by 10. 
                cr_alien.deactivate() #Deactivate alien. 
                if startcounter.counter<=0 and startcounter.counter>=-10:
                    Explosion.add_explosion(canvas,list_explosion,cr_ship.x+37.5,cr_ship.y+37.5,50,"rainbow")
                    stop_game(canvas) #Stop the game 
                    print(record) #Print out dictionary. 
                    cr_ship.deactivate("destruction") #Deactivate the ship.
                    cr_ship.deactivate(3) #Deactivate ship lives. 
                    cr_ship.deactivate(2)
                    cr_ship.deactivate(1)
                    cr_ship.x=-99999 
                    cr_ship.y=-99999
                    for cr_missile in list_missiles:
                        cr_missile.deactivate() #Deactivate missile. 
                    f2=open("game2.txt","a") #Open file and draw from append. 
                    for i in range(0,len(list_for_tuple)): #We have a list of tuples.  
                        tuple_extract=list_for_tuple[i] #Set each tuple to tuple_extract. 
                        f2.write(str(tuple_extract[0])+" "+str(tuple_extract[1])+" "+str(tuple_extract[2])+" "+str(tuple_extract[3])+"\n") 
                        #Print out index of tuple in the form of a string
                    f2.close() #Close file
                if startcounter.counter>0: #If even after decrement, startcounter is greater than 0,
                    cr_ship.deactivate("destruction") #Still need to deactivate ship
                    Explosion.add_explosion(canvas,list_explosion,cr_ship.x+37.5,cr_ship.y+37.5,50,"rainbow") #Create rainbow explosion.
                    if i>0: #If i is greater than 0 (Note: i is initally at value 3.) 
                        cr_ship.deactivate(i) #Deactivate integer value "i" life. 
                        if i==2: #If i is 2. 
                            cr_ship.deactivate(i+1) #Repeat deactivation for third life(along with second).
                        if i==1:
                            cr_ship.deactivate(i+1) #Repeate deactivation for second and third life(along with first)
                            cr_ship.deactivate(i+2)
                            cr_ship.deactivate("destruction") #Deactivate ship with no chance to activate it again.  
                            stop_game(canvas) #Stop game
                            print(record) #Print record
                            cr_ship.x=-99999 
                            cr_ship.y=-99999
                        i=i-1 #Decrement by 1 for loss of life. 

        for cr_missile in list_missiles:
            cr_missile.next() #Create new missiles
            for cr_alien in list_aliens:
                if cr_missile.is_active()==True and cr_alien.is_active()==True: #If these missile and alien are active  
                    if cr_alien.is_shot(cr_missile.x,cr_missile.y): #If shot is correct
                        startcounter.increment(cr_alien.point) #Increment by alien's point value
                        cr_alien.deactivate() #Remove alien from screen
                        Explosion.add_explosion(canvas,list_missiles,cr_alien.x,cr_alien.y+25,30,cr_alien.co) #Add explosion based
                        #on alien's color
                        if cr_alien.co=="red": #If alien color is 1, 
                            red_int+=1 #Increment red_int by 1.
                            record[cr_alien.co]=red_int
                        #Same process for blue, green, and purple.
                        if cr_alien.co=="blue":
                            blue_int+=1
                            record[cr_alien.co]=blue_int
                        if cr_alien.co=="green":
                            green_int+=1
                            record[cr_alien.co]=green_int
                        if cr_alien.co=="purple":
                            purple_int+=1
                            record[cr_alien.co]=purple_int                
            
        
        t=t+1 #Increment time by 1.
        root.update()
        time.sleep(0.01)
    root.mainloop()

    #### to complete


if __name__=="__main__":
    main()

