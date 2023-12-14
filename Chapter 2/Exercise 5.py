# At first we need to import tkinter as tk.
import tkinter as tk

# Now using the def function below.
def perform_operation():
    # Using the try function below.
    try:
        mynum1 = float(myentry1.get())
        mynum2 = float(myentry2.get())
        operation = myoperation_var.get()
    # Now using the if function below.
        if operation == "Addition":
            result = mynum1 + mynum2
            # Now using the elif function below.
        elif operation == "Subtraction":
            result = mynum1 - mynum2
            # Now using the elif function below.
        elif operation == "Multiplication":
            result = mynum1 * mynum2
            # Now using the elif function below.
        elif operation == "Division":
            result = mynum1 / mynum2
            # Now using the elif function below.
        elif operation == "Modulo":
            result = mynum1 % mynum2
            # Now using the else function below.
        else:
            result = "Invalid Operation"
 
        result_label.config(text=f"Result: {result}")
        # Now using the except function below.
    except ValueError:
        result_label.config(text="The Invalid Input")

# Now we need to create the main window for this GUI.
mywindow = tk.Tk()
mywindow.title("The Basic Arithmetic Calculator") # The title for this GUI is "The Basic Arithmetic Calculator".

# Now we need to make sure to  entry widgets for user input.
myentry1 = tk.Entry(mywindow, width=10)
myentry2 = tk.Entry(mywindow, width=10)

# Now we need the dropdown menu for selecting operations below.
myoperations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo"]
myoperation_var = tk.StringVar(mywindow)
myoperation_var.set(myoperations[0])  # Now we need to set default value.
myoperation_menu = tk.OptionMenu(mywindow, myoperation_var, *myoperations)

# Now we need to create a button to perform the operations.
mycalculate_button = tk.Button(mywindow, text="Calculate", command=perform_operation)

# Now we need to create a Label to display the result for this GUI.
result_label = tk.Label(mywindow, text="Result: ")

# Now we also need to make sure to arrange widgets using grid layout.
myentry1.grid(row=0, column=0, padx=5, pady=5)
myoperation_menu.grid(row=0, column=1, padx=5, pady=5)
myentry2.grid(row=0, column=2, padx=5, pady=5)
mycalculate_button.grid(row=1, column=0, columnspan=3, pady=5)
result_label.grid(row=2, column=0, columnspan=3)

# Now we need to start the GUI event loop and therefore run the mainloop.
mywindow.mainloop()
