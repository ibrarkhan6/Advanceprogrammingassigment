# At first we need to import tkinter as tk.
import tkinter as tk
# Now using the def function below.
def count_letters():
    myinput_string = myentry_string.get().lower()  # Convert to lowercase for case-insensitive counting
    myvowels = "aeiou"
    myconsonants = "bcdfghjklmnpqrstvwxyz"
    
    mytotal_letters = len(myinput_string)
    mynum_vowels = sum(1 for char in myinput_string if char in myvowels)
    mynum_consonants = sum(1 for char in myinput_string if char in myconsonants)
    mynum_special = mytotal_letters - (mynum_vowels + mynum_consonants)

    myresult_label.config(text=f"Total number of letters: {mytotal_letters}\n"
                             f"Number of vowels: {mynum_vowels}\n"
                             f"Number of consonants: {mynum_consonants}\n"
                             f"Number of special characters: {mynum_special}")

# Now we need to create the main window for this GUI.
mywindow = tk.Tk()
mywindow.title("Letter Counter")

# Now we need to make sure to entry widget for user input.
myentry_string = tk.Entry(mywindow, width=30)

# Now we need to create the button to count letters.
mycount_button = tk.Button(mywindow, text="Count Letters", command=count_letters)

# Now we need to label in order to display the result.
myresult_label = tk.Label(mywindow, text="Result:")

# Now we need to arrange widgets using grid layout.
myentry_string.grid(row=0, column=0, padx=5, pady=5)
mycount_button.grid(row=1, column=0, pady=5)
myresult_label.grid(row=2, column=0, pady=5)

# Now  we need to start the GUI event loop and get the final GUI result.
mywindow.mainloop()
