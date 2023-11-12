
import pandas as pd
import numpy as np


# Data is put in a dataframe just like in previous tasks:
LeavingTimes = ['09:00', '11:00', '13:00','15:00']
ReturningTimes = ['10:00', '12:00', '14:00','16:00']
UpCost = 25
DownCost  = 25
TrainUpSeats = [480,480,480,480] #Seats Available
TrainDownSeats= [480,480,480,640] #Seats Available
TotalTicketsSold = [0,0,0,0]
MoneyEarned = [0,0,0,0]
ReturnTicket = 50
DiscountedTickets = [0,0,0,0]
data = {
    'LeavingTimes': LeavingTimes,
    'ReturningTime': ReturningTimes,
    'TrainUpSeats': TrainUpSeats,
    'TrainDownSeats': TrainDownSeats,
    'MoneyEarned' : MoneyEarned,
    'TotalTicketsSold' : TotalTicketsSold,
    'DiscountedTickets' : DiscountedTickets
}
df = pd.DataFrame(data)
# Four Trains and every trains will have it's own ticket calculations.
df 
#This is the dataframe I would be making changes in.



# Data of every train is printed seperately using a FOR loop. Outer FOR loop iterates over rows and inner FOR loop iterates over columns
def Task1():
    count = 1
    BreakCount = 0
    print('         TRAIN SCHEDULE         ')
    for j in range(len(df)):
        print('Details Of Train: ',count)
        for i in (df.columns):
            if BreakCount == 4:
                break
            if(i=='TrainUpSeats ' and df[i][j]==0):
                print('No more ticket available for this train \n CLOSED! \n')
                break
            BreakCount+=1    
            print(i, ':', df[i][j])
        print('Total Money Earned from Train: ',count,' is: ',df['MoneyEarned'][j])    
        count+=1
        BreakCount = 0
        print('\n')    
        
        
 #This is task 1. YOu can see I have used two loops to do this task.       



def Task2():
    DiscountForPeople = 0
    while(1):
            Tickets  = input('How many tickets do you want to buy? \n')
            while(int(Tickets)==0):
                print('Enter Correct Number of tickets \n')
                Tickets  = input('How many tickets do you want to buy? \n')
            print('Possible choices: \n 1: ',LeavingTimes[0], ' 2: ',LeavingTimes[1],' 3: ',LeavingTimes[2],' 4: ',LeavingTimes[3])
            TrainupTime = input('Choose a train number to travel to your destination, Press 1,2,3 or 4:  ')
            while(1):
                if TrainupTime not in ['1','2','3','4']:
                    print('Incorrect Choice')
                    print('Possible choices: \n 1: ',LeavingTimes[0], ' 2: ',LeavingTimes[1],' 3: ',LeavingTimes[2],' 4: ',LeavingTimes[3])
                    TrainupTime = input('Choose a train number to travel to your destination: ')

                else:
                    # Below Line is comparing number of tickets with number of tickets available for the chosen train journey.
                    # 
                    if int(Tickets) > int(df[df['LeavingTimes'] == df['LeavingTimes'][int(TrainupTime)-1]]['TrainUpSeats']):
                        print('These many tickets for departure time are not available! \n Available tickets for time: ', LeavingTime,  int(df[df['LeavingTimes'] == LeavingTime]['TrainUpSeats']))
                        choice = input('Enter Yes to Change Departure Time')
                        if(choice=='Yes' or choice=='yes'):
                            print('Possible choices: \n 1: ',LeavingTimes[0], ' 2: ',LeavingTimes[1],' 3: ',LeavingTimes[2],' 4: ',LeavingTimes[3])
                            TrainupTime = input('Choose a train number to travel to your destination, Press 1,2,3 or 4:  ')
                        Tickets  = input('How many tickets do you want to buy? \n')

                    else:
                        TrainupTime = int(TrainupTime) 
                        # For the line below, TrainUpTime-1 is used because indexing of a python data frame starts from 0.
                        # but are choices of times are numbered 1,2,3,4.
                        LeavingTime = df['LeavingTimes'][TrainupTime-1]
                        break
            print('Possible choices: \n 1: ',ReturningTimes[0], ' 2: ',ReturningTimes[1],' 3: ',ReturningTimes[2],' 4: ',ReturningTimes[3])        
            TrainDownTime = input('Choose a train number to get back from your destination, Press 1,2,3 or 4: ')
            # Same Code as above except for Returning Journey
            while(1):
                if TrainDownTime not in ['1','2','3','4'] or int(TrainupTime)>int(TrainDownTime):
                    print('Incorrect Choice')
                    print('Possible choices: \n 1: ',ReturningTimes[0], ' 2: ',ReturningTimes[1],' 3: ',ReturningTimes[2],' 4: ',ReturningTimes[3])
                    TrainDownTime = input('Choose a train number to travel back from your destination: ')
                else:
                    if int(Tickets) > int(df[df['ReturningTime'] == df['ReturningTime'][int(TrainDownTime)-1]]['TrainDownSeats']):
                        print('These many tickets for departure time are not available! \n Available tickets for time: ', ReturningTime,  int(df[df['ReturningTime'] == ReturningTime]['TrainDownSeats']))
                        choice = input('Enter Yes to change arrival time: ')
                        if(choice=='Yes' or choice=='yes'):
                            print('Possible choices: \n 1: ',ReturningTimes[0], ' 2: ',ReturningTimes[1],' 3: ',ReturningTimes[2],' 4: ',ReturningTimes[3])        
                            TrainDownTime = input('Choose a train number to get back from your destination, Press 1,2,3 or 4: ')
                        Tickets  = input('How many tickets do you want to buy? \n')
                    else:    
                        TrainDownTime = int(TrainDownTime)
                        ReturningTime = df['ReturningTime'][TrainDownTime-1]

                        index =  df[df['ReturningTime'] == ReturningTime].index
                        value =  df['TrainDownSeats'][index] - int(Tickets) 
                        df.loc[index, 'TrainDownSeats'] = value

                        index =  df[df['LeavingTimes'] == LeavingTime].index
                        value =  df['TrainUpSeats'][index] - int(Tickets) 
                        df.loc[index, 'TrainUpSeats'] = value
                        print('Your ',Tickets,'have been booked \n Your journey would start at, ', LeavingTime,' and end at ',ReturningTime)
                        break
            if int(Tickets) >=10 or int(Tickets) <=80: #Checks if discount is applicable or not
                DiscountForPeople = int(Tickets) // 10
                index =  df[df['ReturningTime'] == ReturningTime].index #Find index of returning journey
                df.loc[index, 'DiscountedTickets'] += DiscountForPeople #Add number of discounted tickets
                index = df[df['LeavingTimes'] == LeavingTime].index #Same as above except for departure time
                df.loc[index, 'DiscountedTickets'] += DiscountForPeople
                Total = (int(Tickets)- DiscountForPeople) * ReturnTicket #Number of tickets x 50$(PRice of one ticket)
            else:
                Total = int(Tickets) * ReturnTicket
            print('Your Total Bill is: ', Total)
            choose = input(print('Do you want to exit? Enter yes to exit or any other key to continue purchasing \n '))
            if(choose=='Yes' or choose=='yes'):
                break

def Task3():
    TrainUpSeats = [480,480,480,480] #Seats Available Initially
    TrainDownSeats= [480,480,480,640] #Seats Available Initially
    Highest = 0 
    IndexHighest = 0
    for i in range(len(df)):
        # Total tickets sold calculated by adding leaving and arriving tickets of their respective train journeys
        df.loc[i, 'TotalTicketsSold'] = (TrainUpSeats[i] - df.loc[i, 'TrainUpSeats']) + (TrainDownSeats[i] - df.loc[i, 'TrainDownSeats'])
        df.loc[i, 'MoneyEarned'] = (df.loc[i, 'TotalTicketsSold'] - df.loc[i, 'DiscountedTickets']) * 50
        if df['MoneyEarned'][i] > Highest:
            Highest = df['MoneyEarned'][i]
            IndexHighest = i
    for i in range(len(df)):
        print(df['TotalTicketsSold'][i],' were the total number of tickets sold for train: ', i+1)
        print('Train Number ',i+1,'earned ', df['MoneyEarned'][i] )
    print('The train which sold most amount of tickets was: ', IndexHighest+1)    


Task1()

Task2()

Task3()
