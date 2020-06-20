# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:36:03 2020

@author: Rajesh
"""

x = ""
bill = 0
Items = ["item1","item2","item3","item4","item5","item6"]
money = [100,250,30,1250,80,550]
buy = []

print("""List of things you can buy over here:-
Item1 : 100
Item2 : 250 
Item3 : 30
Item4 : 1250
Item5 : 80
Item6 : 550
""")

while x != "no" or x != "No":
    c = input("What do you want to buy:- ")
    a = Items.index(c)
    bill = bill + money[a]
    buy.append(c)
    y = input("Do you wish to buy anything else:- ") 
    if y == "Yes" or y == "yes":
        continue
    else:
        if Items[0] in buy and Items[1] in buy:
            bill = bill -350
            z = 350*75/100
            print("You have got 25% Discount on item1 and item2")
            print("So now your bill is "+str(bill+z))
        elif Items[1] in buy and Items[3] in buy:
            bill = bill -130
            z = 130*90/100
            print("You have got 10% Discount on item1 and item3")
            print("So now your bill is "+str(bill+z))
        elif Items[2] in buy and Items[4] in buy:
            bill = bill -1500
            z = 1500*5/100
            print("You have got 5% Discount on item2 and item4")
            print("So now your bill is "+str(bill+z))
        else:
            print("No discount")
            print("Your bill is "+str(bill))
        break 
