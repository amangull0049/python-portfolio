# Calculator, To find solution between two numbers 
num1 = int (input("Enter 1st Number: "))
num2 = int (input("Enter 2nd Number: "))
operator = input("Enter your Operator (+,-,*,/): ")

if (operator == "+"):
    print("The sum of two numbers: ", num1+num2)
elif (operator == "-"):
    print("The subtract of two numbers: ", num1-num2)
elif (operator == "*"):
    print("The multiple of two numbers: ", num1*num2)
elif (operator == "/"):
    print("The division between two numbers: ", num1/num2)
else:
    print("Invalid Input")