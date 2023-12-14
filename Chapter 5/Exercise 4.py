# At first we need to import tkinter as tk.
import tkinter as tk
# And from math import pi
from math import pi
# Now I am going select the class below with name Shape.
class Shape:
    #Now using the def function below.
    def _init_(myself):
        myself.sides = []
    #Now using the def function below.
    def inputSides(myself):
        pass  #Used for the  subclass
    #Now using the def function below.
    def area(myself):
        pass  # Used for the subclass
# Now I am going select the class below with name Circle.
class Circle(Shape):
    def inputSides(myself):
        radius = float(radius_entry.get())
        myself.sides.append(radius)
# Now I am going to use the def function  below.
    def area(myself):
        radius = myself.sides[0]
        return pi * radius**2 #Using the return function.
# Now I am going select the class below with name Rectangle.
class Rectangle(Shape):
    # Now I am going to use the def function  below.
    def inputSides(myself):
        length = float(length_entry.get())
        width = float(width_entry.get())
        myself.sides.extend([length, width])
# Now I am going to use the def function  below.
    def area(myself):
        length, width = myself.sides
        return length * width  # Using the def function.
# Now I am going select the class below with name Triangle.
class Triangle(Shape):
    # Now I am going to use the def function  below.
    def inputSides(myself):
        base = float(base_entry.get())
        height = float(height_entry.get())
        myself.sides.extend([base, height])
# Now I am going to use the def function  below.
    def area(myself):
        base, height = myself.sides
        return 0.5 * base * height
# Now I am going to use the def function  below.
def calculate_area(myshape):
    myshape.inputSides()
    result_label.config(text=f"Area: {Shape.area()}")
# Remaning the root to finalroot.
finalroot = tk.Tk()
finalroot.title("Shapes")
# Now creating the labels.
radius_label = tk.Label(finalroot, text="Enter Radius (for Circle):")
radius_label.pack()
# Radius.
radius_entry = tk.Entry(finalroot)
radius_entry.pack()
# Label.
length_label = tk.Label(finalroot, text="Enter Length (for Rectangle):")
length_label.pack()
# Entry Label.
length_entry = tk.Entry(finalroot)
length_entry.pack()
# Now we need label for width.
width_label = tk.Label(finalroot, text="Enter Width (for Rectangle):")
width_label.pack()
# Now we need with for the entry.
width_entry = tk.Entry(finalroot)
width_entry.pack()

base_label = tk.Label(finalroot, text="Enter Base (for Triangle):")
base_label.pack()

base_entry = tk.Entry(finalroot)
base_entry.pack()

height_label = tk.Label(finalroot, text="Enter Height (for Triangle):")
height_label.pack()

height_entry = tk.Entry(finalroot)
height_entry.pack()

# Now we need to make and use buttons for every shape below.s
circle_button = tk.Button(finalroot, text="Calculate Circle Area",
                          command=lambda: calculate_area(Circle()))
circle_button.pack()

rectangle_button = tk.Button(finalroot, text="Calculate Rectangle Area",
                             command=lambda: calculate_area(Rectangle()))
rectangle_button.pack()

triangle_button = tk.Button(finalroot, text="Calculate Triangle Area",
                            command=lambda: calculate_area(Triangle()))
triangle_button.pack()

result_label = tk.Label(finalroot, text="")
result_label.pack()

# Now start the mainloop to start the GUI.
finalroot.mainloop()