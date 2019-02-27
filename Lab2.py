#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:58:58 2019

@author: claudiogarcia

CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 2
Claudio Garcia 80628314
The purpose of this program is to sort a list with random values and
then sort them using 3 different methods for sorting, bubble sort, merge sort, 
and quick sort.
"""

## UNCOMMENT OR COMMENT METHODS TO TRY DIFFERENT SORTS IN MEDIAN METHOD

import random
import copy
import time
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        

def getTail(L):
    cur = L
    while (cur != None and cur.next != None):
        cur = cur.next
    return cur

def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    

def Prepend(L, x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    
    else:
        L.head = Node(x, L.head)
       
    


def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
                        
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()
    
    ###############################  Lab 2   #################################  
    
def GetLength(L):
    
    temp = L.head
    counter = 0
    while temp is not None:
        counter +=1
        temp = temp.next

    return counter

def getMiddle(h):
    
        ##Base case 
        if h == None:
            return h 
        fast = h.next
        slow = h
          
        ## Move fast by two and slow by one 
        ## Finally slow will point to middle node 
        while fast is not None:
         
            fast = fast.next
            if(fast!=None):
             
                slow = slow.next
                fast=fast.next
            
        return slow


        

def sortedM(a, b, c):
        
        result = None; 
        
        if a == None:
            return b
        if b == None:
            return a
  
        
        if a.item <= b.item: 

            result = a
            result.next = sortedM(a.next, b, c)
            
        else:
        
            result = b
            result.next = sortedM(a, b.next, c)
            
            
        
        return result
    
  ##################### MEDIAN METHOD ##################
def Median(L):
    C = copy.deepcopy(L)
    
    #C.head = mergeSort(C.head) ##Sorting
    
    bubble(C)
    
    #quickSort(C)
    
    Print(C)
    return ElementAt(C, GetLength(C)//2)

 ##################### MEDIAN METHOD ##################

def ElementAt(L, n):
    if GetLength(L)%2 == 1:
        for i in range(n):
            L.head = L.head.next
        return L.head.item
    else:
        for i in range(n-1):
            L.head = L.head.next
            
        mid = L.head.item
        L.head = L.head.next
         
        return mid
    
  ###############################  Lab 2   #################################  
  
  
def printMiddle(h):
    
    
    slow_ptr = h
    fast_ptr = h
    if h!= None:
        
        while fast_ptr != None and fast_ptr.next != None:
            
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
        return slow_ptr

def bubble(L):
    c = 0
    unsorted = True
    
    while unsorted:
        temp = L.head
        unsorted = False
        
        while temp.next is not None:
            
            if temp.item > temp.next.item:
                
                t = temp.item
                temp.item = temp.next.item
                temp.next.item = t
                unsorted = True
            temp = temp.next
            c +=1
    print('Comparisons for bubble: ', c)
                
            
def mergeSort(h):
        c = 0
        ## Base case : if head is null 
        if h == None or h.next == None:
            return h
         
  
        middle = getMiddle(h)
        nextofmiddle = middle.next
  
       
        middle.next = None
  
        #Apply mergeSort on left list 
        left = mergeSort(h)
        
        #Apply mergeSort on right list 
        right = mergeSort(nextofmiddle)
  
        #Merge the left and right list
        sortedlist = sortedM(left, right, c)
        
        
        
        return sortedlist
        
        
def quickSort(L):
    counter = 0
    if GetLength(L) >1:
        pivot=L.head.item
        L1 = List()
        L2 = List()
        t = L.head.next
        
        #populates two different lists depending on .item value
        while t != None:
            if t.item<pivot:
                Append(L1, t.item)
                
            else:
                Append(L2, t.item)
                
            t = t.next
            counter +=1
            
        quickSort(L1)
        quickSort(L2)
        
        #appending if empty to sort
        if IsEmpty(L1):
            Append(L1, pivot)
            
        else:
            Prepend(L2, pivot)
        
        if IsEmpty(L1):
            L.head = L2.head
            L.tail = L2.tail
            
        else:
            L1.tail.next = L2.head
            L.head = L1.head
            L.tail = L2.tail
            
        print('Comparisons for quick: ', counter)
            

def createList(L, num):
    for i in range(num):
        Append(L,random.randrange(100))
        
        
L = List()

createList(L, 10)
print('Original list')
Print(L)
print(' ')

start_time = time.time()
print('Sorting and returning the median of the list')
print('Median value: ', Median(L))
print("--- %s seconds ---" % (time.time() - start_time))







