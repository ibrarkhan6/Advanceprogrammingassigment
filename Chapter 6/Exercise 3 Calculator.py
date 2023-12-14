# Now we need to import operator.
import operator
# Now using the def funtion below.
def calculate(op, a, b):
    myoperations = {
        '1': operator.add,
        '2': operator.sub,
        '3': operator.mul,
        '4': operator.truediv,
        '5': operator.mod,
        '6': max  # Now we need to check greater number.
    }

    myoperation = myoperations[op]
    # Now I am going to use the return function below.
    return myoperation(a, b)
# Now I am going to use the while function below.
while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Q. Quit")

    mychoice = input("Enter your choice (1-6, Q to quit): ").upper()
# Now I am going to use the if function below.
    if mychoice == 'Q':
        print("Exiting the calculator. Goodbye!")
        # Now I am going to use the break function  below.
        break
# Now I am going to use the if function below.
    if mychoice in ('1', '2', '3', '4', '5', '6'):
        # Now I am going to use the try function below.
        try:
            usernum1 = float(input("Enter the first number: "))
            usernum2 = float(input("Enter the second number: "))
            # Now I am going to use the except below.
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            # Now I am going to use the continue function below.
            continue

        myresult = calculate(mychoice, usernum1, usernum2)
        print(f"Result: {myresult}")

    else:
        # Now we need to enter a number between 1 and 6, or Q to quit.
        print("Invalid choice. Please enter a number between 1 and 6, or Q to quit.")
