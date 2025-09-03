num1 = int(input("Enter 1st Number:"))
choice = input("Enter choice(+,-,*,/)")
num2 = int(input("Enter 2nd Number:"))

if(choice == '+'):
    print("your sum of two numbers is: ", num1 + num2)
elif(choice == '-'):
    print("your subtraction of two numbers is: ", num1 - num2)
elif(choice == '*'):
    print("your multiplication of two numbers is: ", num1 * num2)
elif(choice == '/'):
    if(num2 != 0):
        print("your division of two numbers is: ", num1 / num2)
    else:
        print("Denominator can't be ZERO!...")
else:
    print("Invalid choise!")

