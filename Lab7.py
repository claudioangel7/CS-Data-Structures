
"""
CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 7
Claudio Garcia 80628314
The purpose of this program is to modify lab 6 and various other methods
that can make the program more interesting by actually finding a solution 
to the maze created.
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
            
def setAmount(s): #sets in the disjoint set forests
    c=0
    for i in range(len(s)):
        if s[i]<0:
            c+=1
    return c



def removeComp(s, walls, numSets): #remove random parts of the wall
    while numSets>1:
        w = random.choice(walls) #random wall selection
        i = walls.index(w) #position of wall
        if find(s, w[0]) != find(s, w[1]): ##if root of w[0] is not the same as w[1]
            walls.pop(i) #wall removal
            union_by_size(s, w[0], w[1])  #wall union after the removal
            numSets -=1
    return w

def draw_maze_path(walls,path,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for p in path:
        if p[1]-p[0] != 1: 
            # Vertical Path
            px0 = (p[1]%maze_cols)+.5
            px1 = px0
            py0 = (p[1]//maze_cols)-.5
            py1 = py0+1
        else: 
            # Horizontal Path
            px0 = (p[0]%maze_cols)+.5
            px1 = px0+1
            py0 = (p[1]//maze_cols)+.5
            py1 = py0
        ax.plot([px0,px1],[py0,py1],linewidth=1,color='r')
    for w in walls:
        if w[1]-w[0] == 1: # Vertical Wall position
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else: # Horizontal Wall postion
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
    ax.axis('on') 
    ax.set_aspect(1.0)
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


def Maze_User(m,S,W):
    edge_list = []
    counter = 0
    path = False
    while counter < m:
        d = random.randint(0,len(W)-1)
        # if roots are different
        if find(S,W[d][0]) != find(S,W[d][1]):
            # Join sets
            union(S,W[d][0],W[d][1])
            # Delete wall
            edge_list.append(W.pop(d)) 
            counter += 1
            if counter >= len(S)-1:
                path = True
        elif path: # if there a path start removing any walls
            union(S,W[d][0],W[d][1]) 
            edge_list.append(W.pop(d)) # Wall removal
            counter += 1
    return edge_list

def edge_list_to_adj_list(G,size):
    adj_list = [[] for i in range(size)]
    for i in range(len(G)):
        adj_list[G[i][0]].append(G[i][1])
        adj_list[G[i][1]].append(G[i][0])
    return adj_list 

############################  LAB 7   #####################################
    

    
def BreadthFirstSearch(adj):
    prev = np.zeros(len(adj), dtype=np.int)-1 # Initialize prev array
    visited = [False]*len(adj) # No vertex has been visited
    Q = []
    
    Q.append(adj[0][0]) # Insert the first element to the queue 
    visited[adj[0][0]] = True #Vertex has been visited
    
    while Q:
        if prev[len(adj)-1] >= 0: #if wanted vertex has been reached end
            break
        n = Q.pop(0)
        for j in adj[n]:
            if visited[j] == False: # append to queue if vertex has not been visited
                visited[j] = True
                prev[j] = n
                Q.append(j)
    #starting vertex = -1 since bc no vertex points to this one
    prev[0] = -1 
    return prev

def DepthFirstSearch(adj):
    prev = np.zeros(len(adj), dtype=np.int)-1
    visited = [False]*len(adj)
    S = []
    
    S.append(adj[0][0])
    visited[adj[0][0]] = True
    visited[0] = True 
    prev[adj[0][0]] = 0
    
    while True:
        # continue if the vertex has been reached end
        if prev[len(adj)-1] >= 0:
            break
        n = S.pop()
        for j in adj[n]:
            if visited[j] == False:
                visited[j] = True
                prev[j] = n
                S.append(j)
        if S == []:
            S.append(adj[0][1])
    return prev

def DepthFirst_recursive(adj,origin,visited,prev):
    visited[origin] = True
    for i in adj[origin]:
        if visited[i] == False:
            prev[i] = origin
            DepthFirst_recursive(adj, i, visited, prev)
    return prev
        


def prevEdge(prev):
    E = []
    i = len(prev)-1 # i equal to the end
    while True: 
        if prev[i] == 0 or prev[i] < 0: # Base case when prev is equal to 0 or less
            E.append([0,i])
            break
        elif i < prev[i]: # Edges in the order of small,big
            E.append([i,prev[i]])
        else:    
            E.append([prev[i],i])
        i = prev[i]
    return E # Return the edge list



plt.close("all") 
maze_rows = 30
maze_cols = 30

m = int(input("Choose number of walls to remove: "))
W = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_cols*maze_rows)



if (maze_cols*maze_rows)-1 == m:
    print("\nThere is a unique path from source to destination.")
elif (maze_cols*maze_rows) > m:
    print("\nA path from source to destination is not guaranteed to exist.")
else:
    print("\nThere is at least one path from source to destination.")

edge_list = Maze_User(m,S,W) #Edge list from randomly created maze

adj_list = edge_list_to_adj_list(edge_list,maze_cols*maze_rows) # convert edge list to adj list


prev = BreadthFirstSearch(adj_list) # Function ends when goal has been reached to shorten time
path = (prevEdge(prev))
print("edje list of path: ",path)
draw_maze_path(W,path,maze_rows,maze_cols)


#prev = DepthFirstSearch(adj_list) 
#path = (prevEdge(prev))
#print("edje list of path: ",path)
#draw_maze_path(W,path,maze_rows,maze_cols)
#
#
#visited = [False]*len(adj_list)
#p = np.zeros(len(adj_list),dtype=int)-1
#prev = DepthFirst_recursive(adj_list,0,visited,p)
#path = (prevEdge(prev))
#print("edje list of path: ",path)
#draw_maze_path(W,path,maze_rows,maze_cols)
