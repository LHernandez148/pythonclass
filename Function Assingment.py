import math
def Area(R):
    return math.pi * (R ** 2)
radius = int(input("What is the radius of your circle?"))
print(Area(radius))

def TotalM(Cash, Rate):
    return Cash + (Cash * (Rate/100))
Money = int(input("How much money?"))
Taxrate = int(input("What is the tax rate?"))
print(TotalM(Money, Taxrate))

def Temp(D):
    return (D - 32)*(5/9)
Degrees = int(input("What is the temperature in Fahrenheit?"))
print(Temp(Degrees))
#Code made by Luis Hernandez