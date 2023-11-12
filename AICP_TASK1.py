
import numpy as np
import pandas as pd
import re
BasicComponenetsCost =200
Components = ['Category','Item Code','Description','Price']
Category = ['Case','Case','RAM','RAM','RAM','HDD','HDD','HDD','SDD','SDD','HDD2','HDD2','Optical Drive','Optical Drive','Optical Drive','Operating System','Operating System']
ItemCodes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
Description = ['Compact','Tower','8GB','16GB','32GB','1 TB HDD','2 TB HDD','4 TB HDD','240 GB SSD','480 GB SSD','1 TB HDD','2 TB HDD','4 TB HDD','DVD/Blu-Ray Player','DVD/Blu-Ray Re-writer','Standard Version','Professional Version']
Price = [75.00,150.00,79.99,149.99,299.99,49.99,89.99,129.99,59.99,119.99,49.99,89.99,129.99,50.00,100.00,100.00,175.00]
ExtraItemsList = []
df = pd.DataFrame(columns=Components)
df['Category'] = np.array(Category)
df['Item Code'] = np.array(ItemCodes)
df['Description'] = np.array(Description)
df['Price'] = np.array(Price)
print(df)
# One Case, One RAM and One HDD important.
print('Cost of basic components is: ', BasicComponenetsCost)
print('You may choose any of the following components from the list above.')
print('Buying one case, one RAM and one HDD is a must ')


#Till Now, I have put all of the data in a single dataframe using pandas library.
# I did this so accessing and working with data becomes easier.


# In[2]:

BasicComponenetsCost =200
ItemsList = []
def CalculateCost(Category):
    global BasicComponenetsCost
    global ItemsList
    print('Choose  one case from the following using item code: \n',df[df['Category']==Category])
    Choice = str(input("Enter choice:"))
    while(1): #Loops breaks only if correct component item code is input
        if Choice not in list(df[df['Category']==Category]['Item Code']): #Checks if the item code of the category we are adding to our list exists or not.
            print(list(df[df['Category']==Category]['Item Code']))
            print("Invalid Choice")
            Choice = input("Enter choice again:")
        else:
            Name = Choice
            Choice = df[df.eq(Choice).any(axis=1)] # This Function finds where is the chosen item in the above dataframe.
            Price = float(Choice['Price']) #Once it finds the item, it stores its price.
            Price = str(Price)
            ItemsList.append(Category + ' ' + str(Name) + ' Price: ' + Price)
            BasicComponenetsCost += float(Choice['Price'])
            break
#This function calculate the price of an item and appends it in items list. 


# In[3]:

#This is the same function as above except for extra items. I had two use two different functions due to global variables.
ExtraItemsList = []
def CalculateCostTwo(Category):
    global BasicComponenetsCost
    global ExtraItemsList
    print('Choose  one case from the following using item code: \n',df[df['Category']==Category])
    Choice = str(input("Enter choice:"))
    while(1):
        if Choice not in list(df[df['Category']==Category]['Item Code']):
            print(list(df[df['Category']==Category]['Item Code']))
            print("Invalid Choice")
            Choice = input("Enter choice again:")
        else:
            Name = Choice
            Choice = df[df.eq(Choice).any(axis=1)] # here we are accessing the category, price and description of the item we are currently adding to our list
            Price = float(Choice['Price'])
            Price = str(Price)
            ExtraItemsList.append(Category + ' ' + str(Name) + ' Price: ' + Price) # Category name and Price added to a python list
            BasicComponenetsCost += float(Choice['Price']) # The price of the component is added to total price variable
            break


# In[4]:

# In TASK 1, Price of only HDD, Case and RAM is calculated. For calculation, I have used the function mentioned above.
def Task1():
    global BasicComponenetsCost
    global ItemsList
    CalculateCost('HDD')
    print('\n')
    print('Your Bill till now: ', BasicComponenetsCost)
    CalculateCost('Case')
    print('Your Bill till now: ', BasicComponenetsCost)
    print('\n')
    CalculateCost('RAM')
    print('Your Bill till now: ', BasicComponenetsCost)
    print('\n')
    print('Total Cost of your PC is: ',BasicComponenetsCost)
    print('Items Names and their prices:')
    print(ItemsList)
    Question = input(print('Do want to remove any component and add a different one? \n Press 1 for Yes or any other key for no'))# User can decide to remove or add any component they want to.
    if(Question=='1'):
      while(Question=='1'):
        # In this loop, Item is being removed from the ItemsList list.
        ComponentChoice = input(print('Which Component do you want to remove'))
        if ComponentChoice in list(df['Category']):

          for i in ItemsList:
                if ComponentChoice in i:
                  PriceToBeRemoved = (re.findall("\d+\.\d+", i))[0] # re.findall() function is used to find if the string (ItemsList element) contains a number or not.
                  PriceToBeRemoved = float(PriceToBeRemoved)        # Doing this to extract price of the component that is about to be removed
                  BasicComponenetsCost -= PriceToBeRemoved #Item Price subtracted from the total
                  ItemsList.remove(i) #Item Removed
          CalculateCost(ComponentChoice)
          print('Item Removed Successfully \n Items List now: ', ItemsList,'\n Bill now: ', BasicComponenetsCost)
        else:
          print('There isnt any component with this name. Try again')
        Question = input(print('Dou want to remove any component and add a different one? \n Press 1 for Yes or any other key for no'))
    print('Your Bill is: ', BasicComponenetsCost)

# This is task 1 where we have to calculate price of HDD,RAM and Case. Lets run this code
Task1()


# In[5]:

def Task2():
    global BasicComponenetsCost
    global ExtraItemsList
    while(1):
        print('Choose Any Of the componenets from the following list!')
        print(df[2:]) #I have used df[2:] to exclude cases in this list. A customer would only buy one case for their PC.
        Component = str(input("What Component are you looking for? \n Enter it's Category"))
        while(Component not in df['Category'][2:].values): # If item is not found, It is entered again
            print('No such component found! \n Try Again')
            Component = str(input("Enter Correct Name of Component!!"))
        print(Component + ' has the following range of items \n You may choose any of the following using their item codes: \n') #All the items of that specific component are displayed
        CalculateCostTwo(Component) #Function to calculate cost is called
        print('Total Cost of your PC is: ',BasicComponenetsCost)
        print('Items Names and their prices:')
        print(ExtraItemsList)
        Question = input(print('Do want to remove any component and add a different one? \n Press 1 for Yes or any other key for no'))
        while(Question=='1'):
          # This loop is same as above loop in task 1
          ComponentChoice = input(print('Which Component do you want to remove, Enter its item code \n'))
          if ComponentChoice in list(df['Item Code']):
            for i in ExtraItemsList:
              if ComponentChoice in i:
                    PriceToBeRemoved = (re.findall("\d+\.\d+", i))[0] # We use re.findall function to find the price of
                    # the component from the items list. As price is in float, the function extracts the float value 
                    # and subtracts it from total bill.
                    PriceToBeRemoved = float(PriceToBeRemoved)
                    BasicComponenetsCost -= PriceToBeRemoved
                    ExtraItemsList.remove(i)
                    print('Item Removed Successfully \n Items List now: ', ExtraItemsList,'\n Bill now: ', BasicComponenetsCost)
          else:
            print('There isnt any component with this name. Try again')
          #Before exiting user is asked to confirm if they want to exit or not
          Question = input(print('Do want to remove any component and add a different one? \n Press 1 for Yes or any other key for no'))
        print('Items List: \n',ExtraItemsList)
        ExitChoice = input(print('Are you done shopping? \n Press 0 to exit or any other key to continue \n'))
        if(ExitChoice=='0'):
          break

#This task is for extra components. Lets execute this code.
# Lets input wrong thing.
Task2()
# In the last task, We calculate the final bill by applying discount
def task3():
  global ExtraItemsList
  if(len(ExtraItemsList)==1): # If only one extra item
    OldCost = BasicComponenetsCost
    NewCost = BasicComponenetsCost - (BasicComponenetsCost * 0.05) #5% Discount is applied
    print('You Saved ',OldCost - NewCost, ' Dollars by buying one extra component')
    return NewCost
  if(len(ExtraItemsList)>=2):
    OldCost = BasicComponenetsCost
    NewCost = BasicComponenetsCost - (BasicComponenetsCost * 0.1) # If 2 or more extra items bought, 10% discount is applied
    print('You Saved ',OldCost - NewCost, ' Dollars by buying one extra component')
    return NewCost
Cost = task3()
print('Final Cost: ', Cost)
