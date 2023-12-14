# At first we need to import tkinter as tk.
import tkinter as tk
# Now I am going to use the class with Animal.
class Animal:
    #  Now I am going to use the def function below.
    def __init__(myself, animal_type, name, colour, age, weight, noise):
        myself.type = animal_type
        myself.name = name
        myself.colour = colour
        myself.age = age
        myself.weight = weight
        myself.noise = noise
    #  Now I am going to use the def function below.
    def sayHello(myself):
        print(f"{myself.name} says hello!")
    #  Now I am going to use the def function below.
    def makeNoise(myself):
        print(f"{myself.name} makes a {myself.noise} noise!")
    #  Now I am going to use the def function below.
    def animalDetails(myself):
        details = (
            f"Type: {myself.type}\nName: {myself.name}\nColour: {myself.colour}\n"
            f"Age: {myself.age}\nWeight: {myself.weight} kg\nNoise: {myself.noise}"
        )
        # Now I am going to use the return function below.
        return details

# Now I am to use the class with name AnimalGUI.
class AnimalGUI:
# Now I am  going to use the def function below.
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Animal Information")

        #  Now  I am going to entry widgets for Animal information.
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

        #  Now I need to make  button to create and display Animal for this user.
        myself.display_button = tk.Button(master, text="Create Animal", command=myself.create_animal)
        myself.display_button.pack(pady=10)
    # Using the def function below.
    def create_animal(myself):
        animal_type = myself.type_entry.get()
        name = myself.name_entry.get()
        colour = myself.colour_entry.get()
        age = int(myself.age_entry.get())
        weight = float(myself.weight_entry.get())
        noise = myself.noise_entry.get()

        # Now we need to instantiate Animal object with user-input values.
        animal = Animal(animal_type, name, colour, age, weight, noise)

        # Now we need to invoke class functions for the user.
        animal.sayHello()
        animal.makeNoise()
        details = animal.animalDetails()
        myself.display_info("Animal Information", details)
    # Using the def function below.
    def display_info(myself, title, details):
        #  Now we need to display the result in a new window for  the user.
        result_window = tk.Toplevel(myself.master)
        tk.Label(result_window, text=title, font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Label(result_window, text=details).pack(padx=10, pady=10)
# Using the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = AnimalGUI(finalroot)# The name of this GUIAPP is called AnimalGUI. 
    finalroot.mainloop() # Now start the mainloop.
