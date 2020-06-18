age1 = int(input("Enter age of user1:-"))
age2 = int(input("Enter age of user2:-"))
age3 = int(input("Enter age of user3:-"))

if age1 > age2 and age1 > age3:
    print("The age of user1 is the greatest")
elif age2 > age1 and age2 > age3:
    print("The age of user2 is the greatest")
elif age3 > age1 and age3 > age2:
    print("The age of user3 is the greatest")
else:
    print("All are of same age")
