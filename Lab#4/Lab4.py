
"""
CS 2302 Data Structures Spring 2019
MW 10:30-11:50 in CCSB 1.0202
Instructor: Olac Fuentes
TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
Peer Leader: Erick Macik

Lab 4
Claudio Garcia 80628314
The purpose of this program is to practice B-trees by
creating methods that execute dif
"""

import time

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
        
        
        
   
def Height(T): # Finds the Height of the tree     
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])  # recursively adds 1 if the tree is not leaf


def BTreeToSortedList(T): # Converts the tree into a sorted list
    if T.isLeaf:
        return T.item
    L = []
    for i in range(len(T.item)):
        L = L + (BTreeToSortedList(T.child[i])) # appends the items of the tree in ascending order
        L.append(T.item[i])               
    return L + BTreeToSortedList(T.child[-1])   # returns the list recursively and goes to the last item 


def MinAtDepth(T, d): # Finds the minimum element of the tree
    if T.isLeaf:
        return T.item[0]
    if d==0:
        return T.item[0] # returns the minimum number of the tree until depth is 0
    else:
        # recursively subtract the depth by 1 
        return MinAtDepth(T.child[0],d-1) 
    

def MaxAtDepth(T,d): # Finds the maximum element of the tree    
    if T.isLeaf:
        return T.item[-1]
    if d==0:
        return T.item[-1] # returns largest number until depth is 0
    else:
        # recursively subtracts the depth by 1 
        return MaxAtDepth(T.child[-1],d-1)
    

def ItemsAtDepth(T,d): # Prints the items at a given depth   
    if d ==0:
        for t in T.item: 
            print(t,end= ' ') # prints the items until depth = 0
    if not T.isLeaf:
        for i in range(len(T.child)):
            # recursively subtracts depth by 1
            ItemsAtDepth(T.child[i],d-1)
            

def NumsAtDepth(T, d): # Returns the number of items at a given depth
    c = 0
    if d == 0:
        return len(T.item)
    if T.isLeaf:
        return len(T.item) # returns the number of 
    for i in range(len(T.child)):
        c += NumsAtDepth(T.child[i],d-1)
    return c


def FullNodes(T): # Checks how many nodes are full 
    c = 0
    if not T.isLeaf:
        for i in range(len(T.child)): # when T is.Leaf then recursively we add 1 to each element
            c += FullNodes(T.child[i])
    if len(T.item) == T.max_items: # else we add 1 if the length of the item
        c += 1               
    return c
                
    

def FullLeaves(T): # Checks how many leaves are full
    c = 0
    if T.isLeaf:
        if len(T.item) is T.max_items:    
            return 1
    else:
        for i in range(len(T.child)):
            c += FullLeaves(T.child[i]) #this one do the same as the other
                                              #one, but here recursivley checks if 
                                              #the item is leaf
    return c
        

def KeyAtDepth(T, k): # returns the depth of a certain number
    if k in T.item:
        return 0
    if T.isLeaf:
        return -1   #should return -1 if teh key is not in the tree
    if k>T.item[-1]:
        d = KeyAtDepth(T.child[-1],k)   #recursively looks for for the key if k is in the right side
    else:
        for i in range(len(T.item)):
            if k < T.item[i]:
                d = KeyAtDepth(T.child[i],k)    # check the left side
    if d == -1:
        return -1
    return d + 1                                #returns the depth



                                          
    
depth = 2
key = 105
L = [30, 50, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6, 60, 90, 29, 20, 60, 70, 158, 40, 90, 80, 110, 120, 2, 13, 134]
#L = [60, 90, 29, 20, 60, 70, 158, 40, 90, 80, 110, 120, 2, 13, 134]


T = BTree()    
for i in L:
    Insert(T,i)

PrintD(T, ' ')


time1 = time.time()
print('1.  The height of the tree:',Height(T))
print("\n--- %s seconds ---" % (time.time() - time1))

time2 = time.time()
print('2.  B-Tree converted into a sorted list:')
print(BTreeToSortedList(T))
print("\n--- %s seconds ---" % (time.time() - time2))

time3 = time.time()
print('3.  The minimum element at a depth of',depth,'is:',MinAtDepth(T,depth))
print("\n--- %s seconds ---" % (time.time() - time3))

time4 = time.time()
print('4.  The maximum element at a depth of',depth,'is:',MaxAtDepth(T,depth))
print("\n--- %s seconds ---" % (time.time() - time4))

time5 = time.time()
print('5.  Number of nodes at a depth of', depth,':',NumsAtDepth(T,depth))
print("\n--- %s seconds ---" % (time.time() - time5))

time6 = time.time()
print('6.  All items at a depth of', depth, ':')
ItemsAtDepth(T,depth)
print()
print("\n--- %s seconds ---" % (time.time() - time6))

time7 = time.time()
print('7.  Number of nodes that are full:',FullNodes(T))
print("\n--- %s seconds ---" % (time.time() - time7))

time8 = time.time()
print('8.  Number of leaves that are full:',FullLeaves(T))
print("\n--- %s seconds ---" % (time.time() - time8))

time9 = time.time()
print('9. ',key,'can be found at a depth of:',KeyAtDepth(T,key))
print("\n--- %s seconds ---" % (time.time() - time9))
