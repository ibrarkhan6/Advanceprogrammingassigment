# Now I am going to import tkinter as tk.
import tkinter as tk
# And from tkinter import ttk.
from tkinter import ttk

# Now I am going to make class with Animal name.
class Animal:
    def __init__(myself, animal_type, name, colour, age, weight, noise):
        myself.type = animal_type
        myself.name = name
        myself.colour = colour
        myself.age = age
        myself.weight = weight
        myself.noise = noise
# Now I am going to use the def function.
    def sayHello(myself):
        print(f"{myself.name} says hello!")
# Now I am going to use the def function.
    def makeNoise(myself):
        print(f"{myself.name} makes a {myself.noise} noise!")
# Now I am going to use the def function.
    def animalDetails(myself):
        details = (
            f"Type: {myself.type}\nName: {myself.name}\nColour: {myself.colour}\n"
            f"Age: {myself.age}\nWeight: {myself.weight} kg\nNoise: {myself.noise}"
        )
        # Now I am going to use the return.
        return details

# Now I am going to use the class with name OperationChooserGUI.
class OperationChooserGUI:
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Operation Chooser")

        # Entry widgets for Animal information
        myself.type_label = tk.Label(master, text="Enter Type:")
        myself.type_label.pack(pady=10)

        myself.type_entry = tk.Entry(master)
        myself.type_entry.pack(pady=10)

        myself.name_label = tk.Label(master, text="Enter Name:")
        myself.name_label.pack(pady=10)

        myself.name_entry = tk.Entry(master)
        myself.name_entry.pack(pady=10)

        myself.colour_label = tk.Label(master, text="Enter Colour:")
        myself.colour_label.pack(pady=10)

        myself.colour_entry = tk.Entry(master)
        myself.colour_entry.pack(pady=10)

        myself.age_label = tk.Label(master, text="Enter Age:")
        myself.age_label.pack(pady=10)

        myself.age_entry = tk.Entry(master)
        myself.age_entry.pack(pady=10)

        myself.weight_label = tk.Label(master, text="Enter Weight:")
        myself.weight_label.pack(pady=10)

        myself.weight_entry = tk.Entry(master)
        myself.weight_entry.pack(pady=10)

        myself.noise_label = tk.Label(master, text="Enter Noise:")
        myself.noise_label.pack(pady=10)

        myself.noise_entry = tk.Entry(master)
        myself.noise_entry.pack(pady=10)

        # Combobox for selecting operation type
        myself.operation_label = tk.Label(master, text="Select Operation Type:")
        myself.operation_label.pack(pady=10)

        myself.operation_var = tk.StringVar()
        myself.operation_combobox = ttk.Combobox(
            master, textvariable=myself.operation_var, values=["Animal Info", "Arithmetic", "Relational"]
        )
        myself.operation_combobox.pack(pady=10)
        myself.operation_combobox.set("Animal Info")

        # Now I am going to make buttons to create and display result based on the selected operation for the user.
        myself.display_button = tk.Button(master, text="Perform Operation", command=myself.perform_operation)
        myself.display_button.pack(pady=10)
    # Now I am goung to use the def function below again.
    def perform_operation(myself):
        animal_type = myself.type_entry.get()
        name = myself.name_entry.get()
        colour = myself.colour_entry.get()
        age = int(myself.age_entry.get())
        weight = float(myself.weight_entry.get())
        noise = myself.noise_entry.get()

        animal = Animal(animal_type, name, colour, age, weight, noise)

        selected_operation = myself.operation_var.get()

        if selected_operation == "Animal Info":
            # Now I am going to display animal information for the user.
            animal.sayHello()
            animal.makeNoise()
            details = animal.animalDetails()
            myself.display_info("Animal Information", details)

        elif selected_operation == "Arithmetic":
            # Now I am going to perform arithmetic operation (for illustration).
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2  # Now you can also  modify this for different arithmetic operations.
            myself.display_info("Arithmetic Result", f"Result: {result}")

        elif selected_operation == "Relational":
            # Now I also need to perform relational operation (for illustration) for  the user.
            value1 = int(input("Enter the first value: "))
            value2 = int(input("Enter the second value: "))
            result = value1 == value2  # Now you can modify this for different relational operations
            myself.display_info("Relational Result", f"Result: {result}")

    def display_info(myself, title, details):
        # Now you also need to  display the result in a new window  for the user.
        result_window = tk.Toplevel(myself.master)
        tk.Label(result_window, text=title, font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Label(result_window, text=details).pack(padx=10, pady=10)

# Now I am going to use the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = OperationChooserGUI(finalroot) # The name of this GUIApp will have a title of OperationChooserGUI.
    finalroot.mainloop() # Now start the mainloop.
