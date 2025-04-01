Rain=0
Wind = 0
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
    Input = list(map(Decimal, input("Input your rain and wind number separated by a space: ").split()))
    Rain = Input[o]

    if len(Input) == 1:
        1
    else:
        wind = Input[1]
        WindL.append(Wind)
    RainL.append(Rain)
    o = o + 1
    print(Wind)
    print(len(Input))
    if Rain == -1.0:
        e = 0
        TotalRL = 0
        TotalWL = 0
        i = 0
        while i == len(RainL):
            RainL[i] = Num1
            WindL[i] = Num2
            TotalRL = TotalRL + Num1
            TotalWL = Num2 + TotalWL
            i = i + 1
        AveR = TotalRL / len(RainL)
        AveW = TotalWL / len(RainL)
        NumRead = len(RainL)
        WeaSev = ((AveR * 10) + AveW)
        print("The average rain is {} inches \nThe average wind is {} mph \n The weather severity for these {} readings is: {}".format(AveR, AveW, NumRead, WeaSev))
