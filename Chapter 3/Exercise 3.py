# Now we need to import tkinter as tk.
import tkinter as tk
# And from tkinter import ttk,messsage
from tkinter import ttk, messagebox
# Import math as well.
import math
# Now I am use the class below.
class AreaCalculator:
    def __init__(myself, root):
        myself.root = root
        myself.root.title("Area Calculator")

        # Now we also need to create a good  notebook as a(tabbed interface).
        myself.notebook = ttk.Notebook(root)
        myself.notebook.pack(padx=10, pady=10)

        # Now we also need to create tabs for each of the shape below.
        myself.create_circle_tab()
        myself.create_square_tab()
        myself.create_rectangle_tab()
# Now I am going to use the def function below.
    def create_circle_tab(myself):
        circle_tab = ttk.Frame(myself.notebook)
        myself.notebook.add(circle_tab, text="Circle")

        # Now I am going to create the labels for the shapes as well.
        myradius_label = tk.Label(circle_tab, text="Enter Radius:")
        myradius_label.grid(row=0, column=0, padx=10, pady=10)
        myself.radius_entry = tk.Entry(circle_tab)
        myself.radius_entry.grid(row=0, column=1, padx=10, pady=10)

        # Now we need to calculate button for ths buttons for each of the shapes.
        calculate_button = tk.Button(circle_tab, text="Calculate", command=myself.calculate_circle_area)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
# Now I am going to calculate the button for each shapes
    def calculate_circle_area(myself):
        # Now I am going to use the try fuction below.
        try:
            radius = float(myself.radius_entry.get())
            area = math.pi * radius**2
            messagebox.showinfo("Result", f"The area of the circle is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for the radius.")
# Now I am again using the def function for the shape which is square.
    def create_square_tab(myself):
        square_tab = ttk.Frame(myself.notebook)
        myself.notebook.add(square_tab, text="Square")

        # Now we need to put square inputs.
        side_label = tk.Label(square_tab, text="Enter Side Length:")
        side_label.grid(row=0, column=0, padx=10, pady=10)
        myself.side_entry = tk.Entry(square_tab)
        myself.side_entry.grid(row=0, column=1, padx=10, pady=10)

        # Now I am going to calculate the button for square shape.
        mycalculate_button = tk.Button(square_tab, text="Calculate", command=myself.calculate_square_area)
        mycalculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        # Now I am going to use the def function below.
    def calculate_square_area(myself):
        # Now I am going to use the try function below.
        try:
            side = float(myself.side_entry.get())
            area = side**2
            messagebox.showinfo("Result", f"The area of the square is: {area:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for the side length.")
# Now I am going to use the def function to create rectangle tab.
    def create_rectangle_tab(myself):
        rectangle_tab = ttk.Frame(myself.notebook)
        myself.notebook.add(rectangle_tab, text="Rectangle")

        # Now we need to make rectangle inputs for the shapes.
        mylength_label = tk.Label(rectangle_tab, text="Enter Length:")
        mylength_label.grid(row=0, column=0, padx=10, pady=10)
        myself.length_entry = tk.Entry(rectangle_tab)
        myself.length_entry.grid(row=0, column=1, padx=10, pady=10)
       # Now I am going to create  the lables width for the shapes.
        mywidth_label = tk.Label(rectangle_tab, text="Enter Width:")
        mywidth_label.grid(row=1, column=0, padx=10, pady=10)
        myself.width_entry = tk.Entry(rectangle_tab)
        myself.width_entry.grid(row=1, column=1, padx=10, pady=10)

        # Now we also need to calculate button the butto for the rectangle shape.
        mycalculate_button = tk.Button(rectangle_tab, text="Calculate", command=myself.calculate_rectangle_area)
        mycalculate_button.grid(row=2, column=0, columnspan=2, pady=10)
# Now I am going to use the def function for the rectangle area.
    def calculate_rectangle_area(myself):
        try:
            length = float(myself.length_entry.get())
            width = float(myself.width_entry.get())
            area = length * width
            messagebox.showinfo("Result", f"The area of the rectangle is: {area:.2f}")
            # Now I am going to use the except function.
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for length and width.")
# Now I am going to use the if function for  the name.
if __name__ == "__main__":
    finalroot = tk.Tk()# root is rename into to finalroot.
    app = AreaCalculator(finalroot)
    finalroot.mainloop()# Now start the loop to run the output.

