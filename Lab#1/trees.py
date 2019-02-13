#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:54:02 2019

@author: claudiogarcia

CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 1 
Claudio Garcia 80628314
The purpose of this program is to draw a binary-like tree depending on users 
number input which will translate to number of repetitions.
"""

import numpy as np
import matplotlib.pyplot as plt


        
def draw_trees(ax, n, x_change, y_change, x, y ):
    if n>0:
        #changing the center x to right and left. y changes always downwards
        right = np.array([[x, y], [x - x_change, y - y_change]])
        left = np.array([[x, y], [x + x_change, y - y_change]])
        
        ax.plot(right[:,0],right[:,1],color='k')
        ax.plot(left[:,0],left[:,1],color='k')

        
        draw_trees(ax, n-1, x_change / 2, y_change, x - x_change, y - y_change)
        
        draw_trees(ax, n-1, x_change / 2, y_change, x + x_change, y - y_change)



rep = int(input('How many repetitions you want?:  '))      

plt.close("all")
fig, ax = plt.subplots()
ax.axis('on')

draw_trees(ax, rep, 100, 50, 0, 0)

ax.set_aspect(1.0)
plt.show()
fig.savefig('lines.png')