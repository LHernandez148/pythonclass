class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    Bev1=Beverage("Diet Coke", 1.50)
    Bev2=Beverage("water", 1.00)
    Bev3=Beverage("oranje juice", 2.00)
    Bev4=Beverage("Coke", 1.50)
    Bev5=Beverage("Fanta", 1.50)
    Bev6=Beverage("Coke Zero", 1.50)
    BevList = [Bev1, Bev2, Bev3, Bev4, Bev5, Bev6]
    def menu(self):
        print("\nHello, welcome to the vending machine \nHere are our options")
        i = 0
        for beverage in self.BevList:
            print("{}. {}: {}".format((i+1),self.BevList[i].name,self.BevList[i].price))
            i = i+1
        print("Make your selection")

    def Vending(self):
        if Drink == 1 or 2 or 3 or 4 or 5 or 6:
            Item = Drink - 1
            if self.BevList[Item].price <= Money:
                print("Vending {} right now, enjoy your drink".format(self.BevList[Item].name))
                if self.BevList[Item].price != Money:
                    Change = Money - self.BevList[Item].price
                    print("Here is your change, dispensing ${}".format(Change))
            else:
                print("Not enough money, try again")
        else:
            print("Invalid Drink please try again")
P = 1
while P == 1:
    VenMach = VendingMachine()
    VenMach.menu()
    Drink = int(input("Make a selection (1-6)\n"))
    Money = float(input("Insert the money required\n"))
    VenMach.Vending()
