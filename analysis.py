import numpy as np
import matplotlib.pyplot as plt
A2 = np.loadtxt("game2.txt") #Use np to load texts. 
A1 = np.loadtxt("game1.txt")
length1 = np.linspace(0,len(A2),len(A2)+1) #X axis is from 0 to length of list A2. 
A2b0=[] #An initial empty list
for i in range(0,len(A2)):
    A2b0+=[0] #Add zeros to create list of length A2. 
#Repeat steps for different colors. 
A2b1=[] 
for i in range(0,len(A2)):
    A2b1+=[0]
A2b2=[]
for i in range(0,len(A2)):
    A2b2+=[0]
A2b3=[]
for i in range(0,len(A2)):
    A2b3+=[0]
#Set each index of new lists to the index of each tuple in list A2. 
for i in range(0,len(A2)):
    A2b0[i]=A2[i][0]
    A2b1[i]=A2[i][1]
    A2b2[i]=A2[i][2]
    A2b3[i]=A2[i][3]
    plt.title("game2.txt Statistics on Alien Killings") #Create a unique title. 
#Legend is based on pdf. Each list has distinct pattern and color. 
plt.plot(A2b0,"^-r") 
plt.plot(A2b1,"^-g")
plt.plot(A2b2,"*-b")
plt.plot(A2b3,"^-m") 
plt.show() #Show results. 
#I repeat the same for Game 1. Major difference includes new title. Also, I put x label, legned, and y label since they are the same for both games.
length2 = np.linspace(0,len(A1),10*(len(A1)+1))

A1z0=[]
for i in range(0,len(A1)):
    A1z0+=[0]
A1z1=[]
for i in range(0,len(A1)):
    A1z1+=[0]
A1z2=[]
for i in range(0,len(A1)):
    A1z2+=[0]
A1z3=[]
for i in range(0,len(A1)):
    A1z3+=[0] 
for i in range(0,len(A1)):
    A1z0[i]=A1[i][0]
    A1z1[i]=A1[i][1]
    A1z2[i]=A1[i][2]
    A1z3[i]=A1[i][3]
    plt.title("game1.txt Statistics on Alien Killings")
plt.plot(A1z0,"^-r")
plt.plot(A1z1,"^-g")
plt.plot(A1z2,"*-b")
plt.plot(A1z3,"^-m") 
plt.xlabel("Time Steps")
plt.ylabel("#Aliens Shot")
plt.legend(["red","blue","green","purple"])
plt.show()


