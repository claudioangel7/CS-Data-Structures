#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:56:22 2019

@author: claudiogarcia

CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 1 
Claudio Garcia 80628314
The purpose of this program is to draw a circles that keeps on moving to the left, 
and the second method draws circles to left, right, up, and right depending on users 
number input which will translate to number of repetitions.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 
import time

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        
        ax.plot(x,y,color='k')
        

        draw_circles(ax,n-1,[radius*w, 0],radius*w,w) # center x = 90...
        
        
def draw_circles2(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        draw_circles2(ax,n-1,center,radius/3,w) #Center circle
        
        draw_circles2(ax,n-1,[center[0]+radius/1.5, center[1]],radius/3,w) # x to the right
        
        draw_circles2(ax,n-1,[center[0]-radius/1.5,center[1]],radius/3,w)  # x to the left
       
        draw_circles2(ax,n-1,[center[0],center[1]+radius/1.5],radius/3,w)  # y to up
        
        draw_circles2(ax,n-1,[center[0],center[1]-radius/1.5],radius/3,w)  # y to down
        
        
start_time = time.time()
rep = int(input('How many repetitions you want?:  '))

    
plt.close("all") 
fig, ax = plt.subplots() 

c = [100, 0]
c2 = [330, 0]

draw_circles(ax, rep*8, c, 100,.88)
draw_circles2(ax, rep, c2, 100,.9)

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
print("--- %s seconds ---" % (time.time() - start_time))

    
    
    