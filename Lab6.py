

"""
CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 6
Claudio Garcia 80628314
The purpose of this program is to practice disjoint sets forests 
"""

# Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019
import matplotlib.pyplot as plt
import numpy as np

import random
import time

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root
        
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
            
def setAmount(s): #sets in teh disjoint set forests
    c=0
    for i in range(len(s)):
        if s[i]<0:
            c+=1
    return c


def remove(s, walls, numSets): #remove random parts of the wall
    while numSets>1:
        w = random.choice(walls)  #random wall selection
        i = walls.index(w) #position of wall
        if find(s, w[0]) != find(s, w[1]):  #if root
            walls.pop(i) #wall removal
            union(s, w[0], w[1]) #wall union after the removal
            numSets -=1
    return w

def removeComp(s, walls, numSets): #remove random parts of the wall
    while numSets>1:
        w = random.choice(walls) #random wall selection
        i = walls.index(w) #position of wall
        if find(s, w[0]) != find(s, w[1]): #if root
            walls.pop(i) #wall removal
            union_by_size(s, w[0], w[1])  #wall union after the removal
            numSets -=1
    return w

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 



maze_rows = 20
maze_cols = 20

walls = wall_list(maze_rows,maze_cols) #list of walls in the maze

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

S = DisjointSetForest(maze_rows*maze_cols)  #new disjoint sets forests 
                                            #combining rows and columns

numSets = setAmount(S) #sets in the dsf

#start_time = time.time()
#remove(S, walls, numSets)
#print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
removeComp(S, walls, numSets)
print("--- %s seconds ---" % (time.time() - start_time))

draw_maze(walls,maze_rows,maze_cols) 



            