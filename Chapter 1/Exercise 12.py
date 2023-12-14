# First we need to import maths to move further ahead.

import math

# We need to use the function to calculate the area of a square which is very
# import to for the endz
def calculate_square_area():
  side_length = float(input("Enter the length of a side of the square: "))
  area = side_length * side_length
  print("The area of the square is:", area)

# We need to use the function to calculate the area of a circle.
def calculate_circle_area():
  radius = float(input("Enter the radius of the circle: "))
  area = math.pi*radius**2
  print("The area of the circle is:", area)

# We need to use the function to calculate the area of a triangle.
def calculate_triangle_area():
  base = float(input("Enter the length of the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = 0.5 * base * height
  print("The area of the triangle is:", area)

# Main function to display the menu
def main():
  while True:
    print("Menu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      calculate_square_area()
    elif choice == '2':
      calculate_circle_area()
    elif choice == '3':
      calculate_triangle_area()
    elif choice == '4':
      print("Exitiing the program. Goodbye and Take Care!")
      break
    else:
      print("Invalid choice.Please try again.")


main()