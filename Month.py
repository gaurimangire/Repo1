# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:29:47 2020

@author: Rajesh
"""

month = input("Enter the ful name of any month. Please write the first letter capital:-")
if month in ("January" or "March" or "May" or "July" or "August" or "October" or "December"):
    print("The month of "+str(month) + " has 31 days")
elif month == "February":
    print("The month of "+str(month) + " has 28 days.When it's leap year it has 29 days")
elif month in ("April" or "June" or "September" or "November"):
    print("The month of "+str(month) + " has 30 days")
else:
    print(str(month) + " is not a month")
