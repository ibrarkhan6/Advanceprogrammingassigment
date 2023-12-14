# At first we need to import tkinter as tk.
import tkinter as tk
# Now we have a class with Animal name.
class Animal:
    # Using the def function.
    def __init__(myself, animal_type, name, colour, age, weight, noise):
        myself.type = animal_type
        myself.name = name
        myself.colour = colour
        myself.age = age
        myself.weight = weight
        myself.noise = noise
# Now using the def function below.
    def sayHello(self):
        print(f"{self.name} says hello!")# Using print.
# Now using the def function below again.
    def makeNoise(self):
        print(f"{self.name} makes a {self.noise} noise!")
# Now using the def function below again.
    def animalDetails(self):
        details = (
            f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\n"
            f"Age: {self.age}\nWeight: {self.weight} kg\nNoise: {self.noise}"
        )
        # Using the return function below again.
        return details

# Using the below with the class name AnimalGUI. 
class AnimalGUI:
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Animal Information")

        # INow we need to instantiate Dog and Cow objects
        myself.dog = Animal("Dog", "Jupiter", "White", 2, 14, "Woof-Woof")
        myself.cow = Animal("Cow", "Jobet", "Black", 6, 600, "Moo-Moo")

        # Now  we also need to create buttons for Dog and Cow.
        myself.dog_button = tk.Button(master, text="Dog", command=myself.show_dog_info)
        myself.dog_button.pack(pady=10) #myself.dog_button.pack have a pady of 10

        myself.cow_button = tk.Button(master, text="Cow", command=myself.show_cow_info)
        myself.cow_button.pack(pady=10)
    # Using the def function below.
    def show_dog_info(myself):
        # Invoke class functions for Dog
        myself.dog.sayHello()
        myself.dog.makeNoise()
        details = myself.dog.animalDetails()
        myself.display_info("Dog Information", details)
    # Using the def function below once again for the show_cow_info.
    def show_cow_info(myself):
        # Invoke class functions for Cow
        myself.cow.sayHello()
        myself.cow.makeNoise()
        details = myself.cow.animalDetails()
        myself.display_info("Cow Information", details)
    # Using the def function below once again for the display_info.
    def display_info(myself, title, details):
        #  Now we need to display the result in a new window for the user.
        result_window = tk.Toplevel(myself.master)
        tk.Label(result_window, text=title, font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Label(result_window, text=details).pack(padx=10, pady=10)

# Now I am below going to use the if  funtion.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = AnimalGUI(finalroot)# Now this GUIAPP will have a title of AnimalGUI. 
    finalroot.mainloop()# Now  start the mainloop.
