"""
Created on Thu Feb  7 13:26:58 2019

@author: claudiogarcia

CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 1 
Claudio Garcia 80628314
The purpose of this program is to draw a square and then grab that square vertices 
and use them as origin to keep drawing squares depending on users number input 
which will translate to number of repetitions.
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_squares(ax,n,ver,w):
    
   ##########           bottom left              ###########      
    
    if n>0:
        axChange = [w*.25,w*.75] #what portion the x and y coordinates are changing
        bot_left = np.copy(ver)
        bot_left[0][0] = bot_left[0][0] + axChange[1] 
        bot_left[0][1] = bot_left[0][1] - axChange[0] 
        bot_left[1][0] = bot_left[1][0] + axChange[1]
        bot_left[1][1] = bot_left[1][1] - axChange[1]
        bot_left[2][0] = bot_left[2][0] + axChange[0]
        bot_left[2][1] = bot_left[2][1] - axChange[1]
        bot_left[3][0] = bot_left[3][0] + axChange[0]
        bot_left[3][1] = bot_left[3][1] - axChange[0]
        bot_left[4][0] = bot_left[4][0] + axChange[1]
        bot_left[4][1] = bot_left[4][1] - axChange[0]       
        ax.plot(bot_left[:,0],bot_left[:,1],color='k')
        draw_squares(ax,n-1,bot_left,w/2)
        
  ##########           bottom right              ###########      
            
        axChange = [w*.25,w*.75]
        bot_right = np.copy(ver) 
        bot_right[0] = bot_right[0] - axChange[0]
        bot_right[1][0] = bot_right[1][0] - axChange[0]
        bot_right[1][1] = bot_right[1][1] - axChange[1]
        bot_right[2] = bot_right[2] - axChange[1]
        bot_right[3][0] = bot_right[3][0] - axChange[1]
        bot_right[3][1] = bot_right[3][1] - axChange[0]
        bot_right[4] = bot_right[4] - axChange[0]
        ax.plot(bot_right[:,0],bot_right[:,1],color='k')
        draw_squares(ax,n-1,bot_right,w/2)
        
    
  ##########           upper right              ###########      

        axChange = [w*.25,w*.75]
        up_right = np.copy(ver)
        up_right[0][0] = up_right[0][0] - axChange[0]
        up_right[0][1] = up_right[0][1] + axChange[1]
        up_right[1][0] = up_right[1][0] - axChange[0]
        up_right[1][1] = up_right[1][1] + axChange[0]
        up_right[2][0] = up_right[2][0] - axChange[1]
        up_right[2][1] = up_right[2][1] + axChange[0]
        up_right[3][0] = up_right[3][0] - axChange[1]
        up_right[3][1] = up_right[3][1] + axChange[1]
        up_right[4][0] = up_right[4][0] - axChange[0]
        up_right[4][1] = up_right[4][1] + axChange[1]
        ax.plot(up_right[:,0],up_right[:,1],color='k')
        draw_squares(ax,n-1,up_right,w/2)
        
        
  ##########           upper left              ###########      

        axChange = [w*.25,w*.75]
        up_left = np.copy(ver) 
        up_left[0] = up_left[0] + axChange[1]
        up_left[1][0] = up_left[1][0] + axChange[1]
        up_left[1][1] = up_left[1][1] + axChange[0]
        up_left[2] = up_left[2] + axChange[0]
        up_left[3][0] = up_left[3][0] + axChange[0]
        up_left[3][1] = up_left[3][1] + axChange[1]
        up_left[4] = up_left[4] + axChange[1]
        ax.plot(up_left[:,0],up_left[:,1],color='k')
        draw_squares(ax,n-1,up_left,w/2)
        
        


        
plt.close("all") 
orig_size = 500
ver = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.plot(ver[:,0],ver[:,1],color='k')

rep = int(input('How many repetitions you want?:  '))

draw_squares(ax,rep,ver,orig_size) #we take the original size since in this case it means the length of the square

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
