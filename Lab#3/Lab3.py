#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:09:14 2019

@author: claudiogarcia

CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 3
Claudio Garcia 80628314
The purpose of this program is to recieve an binary search tree and draw it as if it was tree.
Then, to search for a given key and return true or false depending on if the key is in the tree.
Another function is to recieve a sorted list and append the values into a tree and return the root
The fourth function is the opposite, we recieve a tree and we extract the values to append them in to a list
The number five prints the values of the tree and the depth in which they are.
"""

import numpy as np
import matplotlib.pyplot as plt

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T


def InOrder(T):
  if T is None:
      return                     

  InOrder(T.left)   
  
  print(T.item)      
               
  InOrder(T.right)  

def Smallest(T):

  if T.left is None:
      return T
  else:
      return Smallest(T.left)
  
  
def Largest(T):

  if T.right is None:
      return T
  else:
      return Largest(T.right)


def SearchK(T, k):
    
  if k > T.item:

      if T.right is not None:
          if T.item == k:
              return T
          else:
              SearchK(T.right,k)
  
  if k < T.item:
      
      if T.left is not None:
          if T.item == k:
              return T
          else:
              SearchK(T.left,k)


def sum(T):
    tempR = T.right
    tempL = T.left
    s = T.item
    s2 = 0
    
    while tempR is not None:
        s += tempR.item
        tempR = tempR.right
        
    while tempL is not None:
        s2 += tempL.item
        tempL = tempL.left

    return s+s2

def SumTree(T):

    if T is None:        
        return 0
    else:
        return SumTree(T.left) + T.item +  SumTree(T.right)
    
    
def FindDepth(T,k):
  
     if T is None:
        return 0
     else:
        if k != T.item:
             return -1
             
             
        elif k == T.item:
             return 1
         
        FindDepth(T.right,k), FindDepth(T.left,k)
            
    
T = None
A = [20, 7, 21, 5, 1, 13, 41, 6, 9, 12, 32, 7]
for a in A:
    T = Insert(T,a)
    
######################### LAB 3 ################################


def draw_line(ax, n, p, w): #code to make a line
    if n>0:
        i1 = [1,0]
        q=p*w + p[i1]*(1-w)
        ax.plot(p[:,0], p[:,1],color='k')
        draw_line(ax,n-1,q,w)
        
plt.close("all")
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('on')
fig.savefig('triangle.png')



def draw_tree(T, x, y, xChange, yChange):
    if T is not None:
        #Circulating T.item usign bbox function in plt
        plt.text(x, y+yChange, T.item, bbox={"boxstyle":"Round","facecolor":"white"})
        
        #Using same method of Lab 1 to draw trees 
        if T.left is not None: #Tree to the left
            q=np.array([[x-xChange, y], [x, y+yChange]])
            
            draw_line(ax, 1, q,.9)
            
            draw_tree(T.left, x-xChange, y-yChange, xChange/2, yChange)
        
        if T.right is not None: #Tree to the right
            q = np.array([[x, y+yChange], [x+xChange, y]])
            
            draw_line(ax,1,q,.9)
            
            draw_tree(T.right, x+xChange, y-yChange, xChange/2, yChange)
            

def iterativeSearch(T, k):
    if T is None:
        return -1 #The key is not in the tree
    
    if T.item == k:#Key at the root return true
        
        return True
    
    if T is not None:
        while T is not None: #iterating through the binary tree with a while loop until it finds the key
            if T.item < k:
                T = T.right 
            elif T.item > k:
                T = T.left
            else: #else returning true when found
            
                return True
    return -1



def sortedListToBST(L):
    if len(L) == 0:
        return None
    
    mid = len(L)//2
    
    root = BST(L[mid]) #root is the mid of the sorted list
    
    #because is sorted we just save the call in root.left and root.right 
    root.left = sortedListToBST(L[:mid]) 
    root.right = sortedListToBST(L[mid+1:])
    
    return root #return the reference


def extract(T):
    if T is None:
        return [] #return an empty list if T has no items
    else:
        return extract(T.left)+[T.item]+extract(T.right) #inserting the items in a list
    

def printDepth(T, h):
    for i in range(h+1): #for loop to print the depth and the keys on that depth
                         #depending on the height of T
        print('Keys at depth', i)
        ElementAtDepth(T, i)
        print()

def height(T):#function to get the height of a given tree
    if T is None:
        return -1
    else:
        a = 1+height(T.left)
        b = 1+height(T.right)
    if a>=b:
        return a
    if b>=a:
        return b
    
def ElementAtDepth(T, n): #function to print T.item to be used in printDepth method
    if T is None:
        return
    if n==0:
        print(T.item, end=' ')
    else:
        ElementAtDepth(T.left, n-1) #going to the left of the tree and printing when n=0
        ElementAtDepth(T.right, n-1)
    


draw_tree(T, 100, 100, 100, 100)
key = 18
print('\nNumber #2', 'Searching for: ', key, 'in tree ')
print(iterativeSearch(T, key))

print('\nNumber #3', 'Root:')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BSTList = sortedListToBST(L)
print(BSTList.item)

print('\nNumber #4')
s = extract(T)
print(s)

print('\nNumber #5')
printDepth(T, height(T))
        
    