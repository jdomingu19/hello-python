# Infinite Calculator
# A simple calculator that can perform basic arithmetic operations

# infinite loop
while True:
    # user input
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'quit' to end the program")

    # user input
    user_input = input(": ")

    # check user input
    if user_input in ['add', 'sub', 'mul', 'div', 'quit']:
        # quit the program
        if user_input == 'quit':
            break
        else:
            # perform arithmetic operations
            while True:
                # try block to handle exceptions
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    # check user input
                    if user_input == 'add':
                        print(f"{num1} + {num2} = {num1 + num2}")

                    elif user_input == 'sub':
                        print(f"{num1} - {num2} = {num1 - num2}")

                    elif user_input == 'mul':
                        print(f"{num1} * {num2} = {num1 * num2}")

                    elif user_input == 'div':
                        print(f"{num1} / {num2} = {num1 / num2}")

                # raise value error      
                except ValueError:
                    print("Invalid input")
                    
    # show invalid input
    else:
        print("Invalid input")

