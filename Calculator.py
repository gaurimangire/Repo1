# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:16:56 2020

@author: Admin
"""

option = ""
x = ""

while option != 7:
    print("""This is a calculator. Here you can calculate the following
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Remainder Calculation
6. To the Power Values(In this the 1st number is base value and the 2nd is index value)
7. Quit
""")
    option = int(input("Enter the option from the above operation:-"))
    if option == 7:
        break
    while x != "No" or x != "no":
        num1 = int(input("Enter a number:-"))
        num2 = int(input("Enter another number:-"))
        if option == 1:
            print("The addition of "+str(num1) + " and " +str(num2) + " is:-" +str(num1+num2))
        elif option == 2:
            if num1 >= num2:
                print("The subtraction of "+str(num1) + " and " +str(num2) + " is:-" +str(num1-num2))
            else:
                print("The subtraction of "+str(num1) + " and " +str(num2) + " is:-" +str(num2-num1))
        elif option == 3:
            print("The multiplication of "+str(num1) + " and " +str(num2) + " is:-" +str(num1*num2))
        elif option == 4:
            if num1 >= num2:
                print("The division of "+str(num1) + " and " +str(num2) + " is:-" +str(num1/num2))   
            else:
                print("The division of "+str(num1) + " and " +str(num2) + " is:-" +str(num2/num1))
        elif option == 5:
            if num1 >= num2:
                print("The remainder of "+str(num1) + " and " +str(num2) + " is:-" +str(num1%num2))
            else:
                print("The remainder of "+str(num1) + " and " +str(num2) + " is:-" +str(num2%num1))
        elif option == 6:
            print(str(num1) + " raise to " +str(num2) + " is:-"+str(num1**num2))
        
        x = input("Do you wish to continue:-")
        if x == "Yes" or x == "yes":
            continue
        else:
            break
