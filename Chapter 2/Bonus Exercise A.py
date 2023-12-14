# At first we need to import tkinter as tkk.
import tkinter as tk
# Now using the def  function below.
def convert_temperature():
    # Now using the try function below.
    try:
        mytemperature = float(myentry_temperature.get())
        myunit = mytemperature_unit.get()
    # Now using the if function below.
        if myunit == "Celsius":
            result = f"{mytemperature} °C is {mytemperature * 9/5 + 32:.2f} °F"
            # Now using the elif function below.
        elif myunit == "Fahrenheit":
            result = f"{mytemperature} °F is {(mytemperature - 32) * 5/9:.2f} °C"
            # Now using the else function below.
        else:
            result = "The Invalid unit"
    # Now using the except function.
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input")

# Now we need to create the main window for this GUI.
mywindow = tk.Tk()
mywindow.title("Temperature Converter")

# Now we need to make sure to entry widget for user input.
myentry_temperature = tk.Entry(mywindow, width=10)

# Now we need the dropdown menu for selecting temperature unit as required.
mytemperature_units = ["Celsius", "Fahrenheit"]
mytemperature_unit = tk.StringVar(mywindow)
mytemperature_unit.set(mytemperature_units[0])  # Now we need to make sure to set the default value.
unit_menu = tk.OptionMenu(mywindow, mytemperature_unit, *mytemperature_units)

# Now we need to create a  button in ordee to convert temperature
myconvert_button = tk.Button(mywindow, text="Convert", command=convert_temperature)

#Now we also need the label in order  to display the results.
result_label = tk.Label(mywindow, text="Result: ")

# Now we also need to arrange widgets using grid layout for this gui.
myentry_temperature.grid(row=0, column=0, padx=5, pady=5)
unit_menu.grid(row=0, column=1, padx=5, pady=5)
myconvert_button.grid(row=1, column=0, columnspan=2, pady=5)
result_label.grid(row=2, column=0, columnspan=2)

# Now need to run the loop and start the GUI event loop at the end in order to get the final GUI result.
mywindow.mainloop()
