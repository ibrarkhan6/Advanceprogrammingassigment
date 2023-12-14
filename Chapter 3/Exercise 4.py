# At first we need to import tkinter as tk.
import tkinter as tk
# From tkinter import ttk.
from tkinter import ttk
# Now I am going to select the class as MyShapedrawer.

class MyShapeDrawer:
    # Now I am going to use the def function below.
    def __init__(myself, root):
        myself.root = root
        myself.root.title("Shape Drawer")
   # Canvas 
        myself.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        myself.canvas.pack(pady=10)
    # Now we need to create a label for the shapes.
        myself.shape_label = ttk.Label(root, text="Select Shape:")
        myself.shape_label.pack(pady=5)

        myself.shape_var = tk.StringVar()
        myself.shape_combo = ttk.Combobox(root, textvariable=myself.shape_var, values=["Oval", "Rectangle", "Square", "Triangle"])
        myself.shape_combo.pack(pady=5)
        myself.shape_combo.set("Oval")
     # Now we need to make a button for the shapes.
        myself.draw_button = ttk.Button(root, text="Draw Shape", command=myself.draw_shape)
        myself.draw_button.pack(pady=10)
# Now I am going to use the def function below.
    def draw_shape(myself):
        selected_shape = myself.shape_var.get()
# Using the class function if function below for the selected shape.
        if selected_shape == "Oval":
            myself.canvas.create_oval(50, 50, 350, 200, outline="black")
            # Using the elif function.
        elif selected_shape == "Rectangle":
            myself.canvas.create_rectangle(50, 50, 350, 200, outline="black")
             # Using the elif function.
        elif selected_shape == "Square":
            myself.canvas.create_rectangle(50, 50, 200, 200, outline="black")
             # Using the elif function.
        elif selected_shape == "Triangle":
            myself.canvas.create_polygon(50, 200, 200, 50, 350, 200, outline="black")
# Now I am going to use the if function below for the name.

if __name__ == "__main__":
    finalroot = tk.Tk()# Renaming the root to finalroot.
    app = MyShapeDrawer(finalroot) # The name of application is MyShapeDrawer.
    finalroot.mainloop()# Now start the mainloop.
