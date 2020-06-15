# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:59:56 2020

@author: Rajesh
"""


passwd = str(input("Please enter the password:-"))

x = len(passwd)
if x < 6:
    print("The password is to small")
elif x > 16:
    print("The password is to large")
else:
    for y in passwd:
        if y.isdigit():
            if passwd in("!" or "@" or "#" or "$" or "%" or "^"):
                print("Valid Password")
                break
            else:
                print("The password should contain aleast 1 special symbol")
                print("So the password is invalid")
        else:
            continue
    else:
        print("The password should contain aleast 1 digit")
