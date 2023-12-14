# At first we need to import tkinter as tk.
import tkinter as tk
# And from tkinter import Label, font.
from tkinter import Label, font
# Using the class below.
#The name of the application will be called as MyWelcomeApp.
class MyWelcomeApp:
    def __init__(myself, root):
        myself.root = root
        myself.root.title("My Welcome App")# The title for this GUI program will be  "My Welcome App".
        myself.root.geometry("400x200")  # Now we need to  set default window size.
        myself.root.resizable(False, False)  # Now we also need to  disable resizing.
        myself.root.configure(bg="#e6e6e6")  # Now we also need to set the background color.

        myself.create_label()

    def create_label(myself):
        # Now we need to create a custom font for this GUI program.
        mycustom_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Now we also need to create and configure the label for this GUI program.
        mywelcome_label = Label(myself.root, text="Welcome to the GUI App!", font=mycustom_font, bg="#e6e6e6")
        mywelcome_label.pack(pady=20)
# Using the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = MyWelcomeApp(finalroot)
    finalroot.mainloop()#Now start the mainloop.
