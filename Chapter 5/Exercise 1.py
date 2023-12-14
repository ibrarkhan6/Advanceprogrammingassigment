# At first we need ti import tkinter as tk.
import tkinter as tk

# Using the class below.
class Dog:
    def __init__(myself, animalname, animalage):
        myself.name = animalname
        myself.age = animalage
# Using the def function below.
    def woof(myself):
        return f"{myself.name} says woof!"


# Now we need  to create two dog objects.
dog1 = Dog("German Shephard",13)
dog2 = Dog("Husky", 9)

# Now we need determine the oldest dog.
oldest_dog = dog1 if dog1.age > dog2.age else dog2


# Now using tkinter  GUI.
class DogGUI(tk.Tk):
    def __init__(myself):
        super().__init__()
        myself.title("Dog Information")
        myself.geometry("300x200")
        myself.display_dog_info()
# Now using the def function below.
    def display_dog_info(myself):
        label1 = tk.Label(myself, text=f"Dog 1: {dog1.name}, {dog1.age} years old")
        label1.pack()
        label2 = tk.Label(myself, text=f"Dog 2: {dog2.name}, {dog2.age} years old")
        label2.pack()
        oldest_dog_label = tk.Label(myself, text=f"The oldest dog is {oldest_dog.name}")
        oldest_dog_label.pack()
        woof_button = tk.Button(myself, text="Make the oldest dog woof", command=myself.woof)
        woof_button.pack()
# Now using the def function below again.
    def woof(myself):
        result = oldest_dog.woof()
        woof_label = tk.Label(myself, text=result)
        woof_label.pack()


# Now we need to nnstantiate the DogGUI class.
app = DogGUI()
app.mainloop()
