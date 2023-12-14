# First we need to import tkinter as tk at begining
import tkinter as tk 
# After that from tkinter we need to import filedialog.
from tkinter import filedialog
# I would like to the class as MyStringCounterApp to make sure the app have a unique name. 
class MyStringCounterApp:
    # Using below the def function.
    def __init__(myself, root):
        myself.root = root #Using root.
        # myself.root.title is My String Counter App
        myself.root.title("My String Counter App")

        #  Now below I am creating labels to  go further ahead in this task.
        # I am creating labels by keeping  its name  as myself.label 
        myself.label = tk.Label(root, text="Select a file:") # Text is "Select a file" 
        myself.label.pack(pady=10) # pady is 10.

        # Now below I am creating buttons below in order to  go further ahead in this task.
        # Now text is browse and command is myself.browse_file.
        myself.browse_button = tk.Button(root, text="Browse", command=myself.browse_file)
        myself.browse_button.pack(pady=10) # pady is 10.

        myself.count_button = tk.Button(root, text="Count Strings", command=myself.count_strings)
        myself.count_button.pack(pady=10)

        # Below  are string variables for storing file path and string counts in this task.
        myself.file_path = tk.StringVar()
        myself.string_counts = {}
        # Using def function below.
    def browse_file(myself):
        myfile_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if myfile_path:
            myself.file_path.set(myfile_path)
        # Using def function below.
    def count_strings(myself):
        file_path = myself.file_path.get()
        #Using the if  function below and therefore to show the error.
        if not file_path:
            myself.show_error("Please select a file.")# "Please select a file"
            return
        # Below is strings to count.
        mystrings_to_count = [
            "Hello my name is Peter Parker",
            "I love Python Programming",
            "Love",
            "Enemy",
        ]

        try:
            with open(file_path, "r") as file:
                content = file.read()

                # Now we have to count occurrences of each string below.
                for yourstring_to_count in mystrings_to_count:
                    count = content.count(yourstring_to_count)
                    myself.string_counts[yourstring_to_count] = count

                # Now kindly display the results
                myself.show_results()

        except Exception as e:
            myself.show_error(f"Error: {str(e)}")

    def show_results(myself):
        myresult_window = tk.Toplevel(myself.root)
        myresult_window.title("Results")

        # Now kindly display the counts below.
        for yourstring_to_count, count in myself.string_counts.items():
            myresult_label = tk.Label(myresult_window, text=f"{yourstring_to_count}: {count} occurrences")
            myresult_label.pack()
     # Using def function to show errors.
    def show_error(myself, message):
        myerror_label = tk.Label(myself.root, text=message, fg="red")
        myerror_label.pack(pady=10)
      # Using if function.
if __name__ == "__main__":
    root = tk.Tk()
    app = MyStringCounterApp(root) #The name of application is MyStringCounterApp.
    root.mainloop() # Now start mainloop and kindly note the sentences.txt file and created and saved in folder.

