7
# Using the def function below and the triangle have 3 sides.
def classify_triangle(thetriangleside1, thetriangleside2, thetriangleside3):
    # Using the if function below.
    if thetriangleside1 == thetriangleside2 == thetriangleside3:
         # Using the return function below.
        return "Equilateral"
        # Using the elif function below.
    elif thetriangleside1 == thetriangleside2 or thetriangleside1 == thetriangleside3 or thetriangleside2 == thetriangleside3:
        # Using the return function below.
        return "Isosceles"
     # Using the else function below.
    else:
         # Using the return function below.
        return "Scalene"
# Using the def function below once again.
def main():
    print("Enter the lengths of the three sides of a triangle:")
    thetriangleside1 = float(input("Enter the length of side 1: "))
    thetriangleside2 = float(input("Enter the length of side 2: "))
    thetriangleside3 = float(input("Enter the length of side 3: "))

    #Now we also need to  check the triangle inequality for the user.
    if thetriangleside1 + thetriangleside2 > thetriangleside3 and thetriangleside1 + thetriangleside3 > thetriangleside2 and thetriangleside2 + thetriangleside3 > thetriangleside1:
        print("These sides form a valid triangle.")

        # Now we also need to  classify the type of triangle for the user.
        mytriangle_type = classify_triangle(thetriangleside1, thetriangleside2, thetriangleside3)
        print(f"The triangle is {mytriangle_type}.")
        # Now using the else function once again.
    else:
        print("These sides do not form a valid triangle.")
# Using the if function below once again at the end.
if __name__ == "__main__":
    main()
