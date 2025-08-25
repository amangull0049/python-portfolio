print("Simple Calculator")
print("Operations: + , - , * , /")
print("Type 'exit' to quit.\n")

while True:
    num1 = input("Enter first number (or 'exit' to quit): ")
    if num1.lower() == "exit":
        print("Calculator Closed. Bye!")
        break
    
    num2 = input("Enter second number: ")
    operation = input("Enter operation (+, -, *, /): ")

    num1 = float(num1)
    num2 = float(num2)

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by Zero not allowed!")
    else:
        print("Invalid operation!")
    
    print("-------------------------")
