
def calcArea():
    HexagonArea = 1.5*1.732*Length
def calcPeri():
    PermiMeterHexagon = 6*Length
def CalcAngleSum():
    SumAngles = 6*120
def display():
    print('Area of Hexagon is: ',HexagonArea)
    print('Perimeter of Hexagon is: ',PeriMeterHexagon)
    print('Sum of Angles is: ',SumAngles)
# Here we have the functions of Hexagon. CalcArea just takes the length and outputs the area. Same as perimeter. In the document, the value of a 
# was 120 so using that I calculated SumAngles. We Will put these functions in Hexagon class.


def CalcAreaSquare():
    SquareArea = Length*Length
def CalcPeriSquare():
    SquarePeriMeter = 4*Length
def display():
    print('Area of the square is: ',SquareArea)
    print('Perimeter of the square is: ',SquarePeriMeter)


# In[7]:

class Hexagon:
    def __init__(self, length):
        self.Length = length
        self.HexagonArea = 0
        self.PeriMeterHexagon = 0
        self.SumAngles = 1

    def calcArea(self):
        self.HexagonArea = 1.5 * 1.732 * self.Length

    def calcPeri(self):
        self.PeriMeterHexagon = 6 * self.Length

    def calcAngleSum(self):
        self.SumAngles = 6 * 120

    def display(self):
        print('Area of Hexagon is: ', self.HexagonArea)
        print('Perimeter of Hexagon is: ', self.PeriMeterHexagon)
        print('Sum of Angles is: ', self.SumAngles)

hexagon = Hexagon(7)   # This is the last digit of my CNIC. Using it, we create an instance.


# In[4]:

class Square:
    def __init__(self, length):
        self.Length = length
        self.SquareArea = 0
        self.SquarePeriMeter = 0

    def calcAreaSquare(self):
        self.SquareArea = self.Length * self.Length

    def calcPeriSquare(self):
        self.SquarePeriMeter = 4 * self.Length

    def display(self):
        print('Area of the square is: ', self.SquareArea)
        print('Perimeter of the square is: ', self.SquarePeriMeter)
square = Square(8) # Same logic as Hexagon's class except formulae are different.


# In[8]:

while(1):
    print('Press 1 to calculate Area,Perimeter and Sum Of Angles of Hexagon \n Press 2 to calculate Area and Perimeter of Square \n Press any other key to exit')
    choice = input()
    if choice=='1':
        hexagon.calcArea()
        hexagon.calcPeri()
        hexagon.calcAngleSum()
        hexagon.display()
    elif choice=='2':
        square.calcAreaSquare()
        square.calcPeriSquare()
        square.display()
    else:
        print('Exiting \n')
        break

