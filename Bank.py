# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:03:38 2020

@author: Rajesh
"""

from time import sleep

trans = 0
info1 = ["Gauri","Tejanshi","Aditi","Shreya"]#User Name
info2 = [12340,24680,13579,56789]#Account Number
info3 = ["Password","Infinity","Cool!","Bank@"]#Password
info4 = [1000,2500,5000,7500]#Balance

AN = int(input("Account Number Please:-"))#Asking the Account number


while AN not in info2:
    AN = int(input("Account Number does not exist:-"))
x = info2.index(AN)    

P = input("Correct Account Number. Now please enter the Password:-")#Asking the password


while P != info3[x]:
    P = input("Incorrect Password. Please try again:-")
sleep(1)    
if P == info3[x]:
    print("Welcome "+str(info1[x]))

while trans != 5:#Transcation type
    print("""Which type of transcation you are going to do:-
1.Balance Inquire
2.Cash Withdrawal
3.Cash Deposit
4.Loan
5.Exit
""")
          
    trans =int(input("Enter one of the option number:-"))
    
    if trans == 1:#Balance inquire
        print("The current amount you have in your account is: "+str(info4[x]))   
        
    elif trans == 2:#Cash withdrawl
        print("How much money do you want to withdraw. You can withdraw "+str(info4[x]-500) + "rupees or less:-")              
        cash = int(input())
        info4[x] = info4[x] - cash
        print("Now you have "+str(info4[x]) + "Rupees left")
    
    elif trans == 3:#Cash deposit
        print("How much money do you want to deposit:-")
        cash1 = int(input())
        info4[x] =info4[x] + cash1
        print("Now you have "+str(info4[x]) + "Rupees in your bank")
    
    elif trans == 4:#Loan
        print("Welome. Here you can get loan if you like.")
        ans = input("Enter Y for yes or enter N for no")
        if ans == "Y" or ans == "y":
            print("Enter the amount of loan you want.")
            print("You can have loan of "+str(info4[x]/2) + "or more")
            loan = int(input("Amount Please:-"))
            info4[x] = info4[x] + loan
            print("You are approved for the loan.")
            print("The loan is transfered to your bank account.Now the current amount you have in your account is: "+str(info4[x]))
        
    elif trans == 5:#Quit
          print("Are you sure you want to leave")
          L = input("Yes or No")
          if L == "No" or L == "no":
              continue
          else:
              print("""Thank you.
Have a great day.
Bye""")
              break
    sleep(1)
    print("Do you want to continue?")  
    ans = input("Type yes or no")
    if ans == "Yes" or ans == "yes":
        continue
    else:
        print("""Thank you .
Have a great day.
Bye""")    
    break
