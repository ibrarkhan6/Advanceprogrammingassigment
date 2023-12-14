# Now is this program we need to help the user  to display the calculators menu.
# Chosing values as (a,b)
# Using the def function below for the addition.
def add(a, b):
    return a + b
# Using the def function below for the subtraction.
def subtract(a, b):
    return a - b
# Using the def function below for the multiplication.
def multiply(a, b):
    return a * b
# Using the def function below for the divison.
def divide(a, b):
    if b == 0:
        return "Error: Kindly note really well that divison  cannot be  divide by zero"
    return a / b
# Using the def function below for the modulus.
def modulus(a, b):
    if b == 0:
        return "Error: Kindly note really well that we cannot compute modulus with zero divisor"
    return a % b
# Using the while function below.
while True:
    # The calculator menus are given below.
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
# Using below the choice function.
    choice = input(" Kindly enter choice your choice(1-5): ")
# Using below the if function.
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
# Using below the if function.
        if choice == '1':
            print("Result: ", add(num1, num2))
          # Using below the elif function.  
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
            # Using below the elif function. 
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
            # Using below the elif function. 
        elif choice == '4':
            print("Result: ", divide(num1, num2))
            # Using below the elif function. 
        elif choice == '5':
            print("Result: ", modulus(num1, num2))
            # Using below the elif function. 
    else:
        print("Invalid choice")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break