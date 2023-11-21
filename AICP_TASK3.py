
# coding: utf-8

# In[36]:

import pandas as pd
import numpy as np


# In[37]:

Matrix = [[55,65,75],[120,150,170],[210,320,240]] # 2D MAtrix with source data
StudentID = 123453 # Student ID


# In[38]:

def CostSlab1():
    List1 = []
    for i in Matrix[0]: # Matrix with index 0 indicates that its the first row
        List1.append(i*10)  # Every element of that row is multiplied by its cost
    print('Bill for Slab 1: \n', List1)    


# In[39]:

def CostSlab2():
    List1 = []
    for i in Matrix[1]:  # Matrix with index 1 indicates that its the second row
        List1.append(i*15)
    print('Bill for Slab 2: \n', List1)    


# In[40]:

def CostSlab3():
    List1 = []
    for i in Matrix[2]: # Matrix with index 2 indicates that its the third row
        List1.append(i*20)
    print('Bill for Slab 3: \n', List1)    


# In[41]:

def TASK():
    print('Student ID: ',StudentID)
    while(1):
        print('Enter 1 to print Cost of Slab 1 and 2 \n Enter 2 to print cost of Slab 3 \n Enter any other key to exit')
        Choice = input()
        if Choice == '1':
            CostSlab1()
            CostSlab2()
        elif Choice == '2':
            CostSlab3()
        else:
            print('Exit')
            break


# In[42]:

TASK()


# In[ ]:



