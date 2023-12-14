# At first we need to import tkinter tk.
import tkinter as tk
# Second from tkinter import ttk.
from tkinter import ttk
#Using the class below with name ArithmeticOperations.
class ArithmeticOperations:
    # Using the def function below.
    def __init__(myself):
        myself.result = 0
    # Using the def function below.
    def calculate(myself, operation, num1, num2):
        # Using the if function below.
        if operation == "Addition":
            myself.result = num1 + num2
            # Using the def function below.
        elif operation == "Subtraction":
            myself.result = num1 - num2
             # Using the def function below.
        elif operation == "Multiplication":
            myself.result = num1 * num2
             # Using the def function below.
        elif operation == "Division":
            # Using the if function below.
            if num2 != 0:
                myself.result = num1 / num2
                 # Using the def function below.
            else:
                myself.result = "Cannot divide by zero"
# Using the class below with the name CalculatorGUI.
class CalculatorGUI:
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Arithmetic Calculator")

        myself.arithmetic_operations = ArithmeticOperations()

        # Now I am going to operation combobox
        myself.operation_label = tk.Label(master, text="Select Operation:")
        myself.operation_label.pack(pady=10)

        myself.operation_var = tk.StringVar()
        myself.operation_combobox = ttk.Combobox(
            master, textvariable=myself.operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"]
        )
        myself.operation_combobox.pack(pady=10)
        myself.operation_combobox.set("Addition")

        # Now I am goint to  entry widgets for numbers for the user.
        myself.num1_label = tk.Label(master, text="Enter Number 1:")
        myself.num1_label.pack(pady=10)

        myself.num1_entry = tk.Entry(master)
        myself.num1_entry.pack(pady=10)

        myself.num2_label = tk.Label(master, text="Enter Number 2:")
        myself.num2_label.pack(pady=10)

        myself.num2_entry = tk.Entry(master)
        myself.num2_entry.pack(pady=10)

        # Now I need to calculate button.
        myself.calculate_button = tk.Button(master, text="Calculate", command=myself.calculate)
        myself.calculate_button.pack(pady=10)

        #  Now I need to result label below.
        myself.result_label = tk.Label(master, text="")
        myself.result_label.pack(pady=10)
    # Now I am going to use def function to calculate.
    def calculate(myself):
    # Now I am going to  use the try function.
        try:
            num1 = float(myself.num1_entry.get())
            num2 = float(myself.num2_entry.get())
            operation = myself.operation_var.get()

            myself.arithmetic_operations.calculate(operation, num1, num2)
            result = myself.arithmetic_operations.result

            myself.result_label.config(text=f"Result: {result}")
    # Now I am going to use the except function below.
        except ValueError:
            myself.result_label.config(text="Please enter valid numbers.")

# Using the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = CalculatorGUI(finalroot) # This GUIApp have a title of CalculatorGUI.
    finalroot.mainloop() # Now start the mainloop.
