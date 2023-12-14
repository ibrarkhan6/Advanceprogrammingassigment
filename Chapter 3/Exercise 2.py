# At first we need to import tkinter as tk.
import tkinter as tk
# And from tkinter import ttk as messagebox.
from tkinter import ttk, messagebox



# Now I am going to select the class as MyCoffeeVendingMachine.
class MyCoffeeVendingMachine:
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Coffee Vending Machine")

        myself.coffee_var = tk.StringVar()
        myself.options_var = tk.StringVar()

        myself.create_widgets()
# Now I am going to use the def function below to create_widgets.
    def create_widgets(myself):
        # Now we have to  the chance for the coffee Selection.
        mycoffee_label = tk.Label(myself.master, text="Select Coffee:")
        mycoffee_label.pack()
# Now below are the options availabel for the user while selecting and making the coffe.
        coffee_options = ["Espresso", "Cappuccino", "Latte", "Americano"]
        coffee_combobox = ttk.Combobox(myself.master, values=coffee_options, textvariable=myself.coffee_var)
        coffee_combobox.pack()

    
        # Now below are mentioned the options selection for the user.
        myoptions_label = tk.Label(myself.master, text="Select Options:")
        myoptions_label.pack()

        mysugar_checkbox = tk.Checkbutton(myself.master, text="Sugar", variable=myself.options_var)
        mysugar_checkbox.pack()

        mymilk_checkbox = tk.Checkbutton(myself.master, text="Milk", variable=myself.options_var)
        mymilk_checkbox.pack()

        # Now we need to make and design the submit button for the user.
        mysubmit_button = ttk.Button(myself.master, text="Submit", command=myself.display_order)
        mysubmit_button.pack()

# Now I am going to use the def function for display_order.
    def display_order(self):
        mycoffee = self.coffee_var.get()
        options = self.options_var.get()

        order_message = f"Your order: {mycoffee}"
        # Now I am going to use the if function for the options.
        if options:
            order_message += f" with {options}"

        messagebox.showinfo("Order Confirmation", order_message)
# Now we I am going to use the def function again for the mainloop.
def main():
    finalroot = tk.Tk() # Renaming the root to finalroot.
    app = MyCoffeeVendingMachine(finalroot)
    finalroot.mainloop()
# Now using the if function below for name.
if __name__ == "__main__":
    main()





# script_path = os.path.dirname(os.path.realpath(_file_))
# img = Image.open(os.path.join(script_path, "image.png"))
# coffeeimg = ImageTk.PhotoImage(img)

# creating a label which will contain the image
# imgcontainer = tk.Label(finalroot, image=coffeeimg)
#  imgcontainer.pack()
