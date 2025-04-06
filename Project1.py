Rain=0
Wind=0
RainL = []
WindL = []
AveR = 0
AveW = 0
Num1=0
Num2=0
TotalRL = 0
TotalWL = 0
i = 0
e = 1
o = 0
from decimal import Decimal
while e == 1:
    Input = list(input("Input your rain and wind number separated by a space: ").split())
    Check = Decimal(Input[0])
    if Check == (-1.0):
        e = 0
        TotalRL = 0
        TotalWL = 0
        i = 0
        while i <= len(RainL) - 1:
            Num1 = RainL[i]
            Num2 = WindL[i]
            TotalRL = TotalRL + Num1
            TotalWL = Num2 + TotalWL
            i = i + 1
        AveR = TotalRL / len(RainL)
        AveW = TotalWL / len(RainL)
        NumRead = len(RainL)
        WeaSev = ((AveR * 10) + AveW)
        print("The average rain is {} inches \nThe average wind is {} mph \n The weather severity for these {} readings is: {}".format(AveR, AveW, NumRead, WeaSev))
    elif Check != -1.0:
        Wind = Decimal(Input[1])
        Rain = Decimal(Input[0])
        WindL.append(Wind)
        RainL.append(Rain)
