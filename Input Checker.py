input1 = input("Enter anything you want:-")
input2 = input("Enter anything you want:-")

if input1.isdigit() and input2.isdigit():
    x = int(input1) + int(input2)
    print(x)
    
elif input1.isalpha() and input2.isalpha():
    print(input1+input2)

else:
    print("It is something different")

