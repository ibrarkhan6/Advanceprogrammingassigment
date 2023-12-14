# At first we need to import tkinter as tk.
import tkinter as tk
# Secondly from tkinter import filedialog.
from tkinter import filedialog
# Below is used class fucction.
class MyLetterCounterApp: #The title  is named as "MyLetterCounterApp".
    # Below def function is used as well.
    def __init__(myself, root):#Def function.
        myself.root = root
        # The title is mentioned below which is "My Letter Counter App".
        myself.root.title("My Letter Counter App")

        # Now I am creating labels with code which is myself.label.
        myself.label = tk.Label(root, text="Select a file:")# Text mentioned is "Select a file".
        myself.label.pack(pady=10)# myself.label.pack has a pady of 10.

        # Now below I am creating buttons with the code  which is myself.browse_button text mentioned in it will be "Browse".
        myself.browse_button = tk.Button(root, text="Browse", command=myself.browse_file)
        myself.browse_button.pack(pady=10) #myself.browse_button.pack have a pady of 10.

        # Now I am creating entry widget for user to enter a character over a period of time.
        myself.char_entry = tk.Entry(root, width=5)
        myself.char_entry.pack(pady=10) # myself.char_entry.pack has a pady of 10.

        myself.count_button = tk.Button(root, text="Count Letter", command=myself.count_letter)
        myself.count_button.pack(pady=10)# myself.count_button.pack has a pady of 10.

        # Now below are the string variables for storing file path and letter count for the user.
        myself.file_path = tk.StringVar()
        myself.letter_count = 0
        # Now again using def function below for browse_file.
    def browse_file(myself):
        myfile_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if myfile_path: # Now again using if function.
            myself.file_path.set(myfile_path)
      
        # Now again using def function below for counter_letter.
    def count_letter(myself):
        myfile_path = myself.file_path.get()
       # Now again using if not function for myfile_path.
        if not myfile_path:
            myself.show_error("Please select a file.")
            return# Now again using the return function.

        # Now we  have to get the letter entered by the user over a period of time.
        myletter_to_count = myself.char_entry.get()
         # Now again using the if not function for myletter_to_count code.
        if not myletter_to_count:
            myself.show_error("Please enter a letter.")
            return # Now again using return function.
        # Now using the try function below.
        try:
            with open(myfile_path, "r") as file:
                content = file.read()

                # Now I have to  count occurrences of the specified letter in this task.
                myself.letter_count = content.lower().count(myletter_to_count.lower())

                # Now I have to display the result which the user requires.
                myself.show_result()
       # Now using below except function.
        except Exception as e:
            myself.show_error(f"Error: {str(e)}")
        # Now below using def function.
    def show_result(myself):
        myresult_window = tk.Toplevel(myself.root)
        myresult_window.title("Result")

        myresult_label = tk.Label(myresult_window, text=f"Occurrences of the letter: {myself.letter_count}")
        myresult_label.pack()
    # Now again using below the def function.
    def show_error(myself, message):
        myerror_label = tk.Label(myself.root, text=message, fg="red")
        myerror_label.pack(pady=10)
  #  Below again below using the if function below.
if __name__ == "__main__":
    root = tk.Tk()
    app = MyLetterCounterApp(root) #The name of the application is MyLetterCounterApp.
    root.mainloop()# Now run the mainloop  at the end.
    #By this program a gui app is developed that will ask user to enter a character and also reads the content of the sentences.txt 
    # file that is present in the folder. 
