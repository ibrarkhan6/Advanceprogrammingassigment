# At first we need to import tkinter as tk.
import tkinter as tk
# Now from tkinter import messagebox.
from tkinter import messagebox
# Now selecting class as RakBurgerShackGUI
class RakBurgerShackGUI:
    def __init__(myself, root):
        myself.root = root
        myself.root.title("Burger Shack Ordering System")

        myself.burger_var = tk.StringVar()
        myself.toppings_var = tk.StringVar()
        myself.condiments_var = tk.StringVar()
        myself.sides_var = tk.StringVar()
        myself.payment_var = tk.DoubleVar()

        myself.create_widgets()
# Now I am going to use the def function in oorder to create the widgets. 
    def create_widgets(myself):
        # Now I am going to mention the three types of burgers that will be available for the user which are "Beef", "Chicken", "Vegetarian".
        tk.Label(myself.root, text="Choose a Burger:").pack()
        myburger_options = ["Beef", "Chicken", "Vegetarian"]
        for option in myburger_options:
            tk.Radiobutton(myself.root, text=option, variable=myself.burger_var, value=option).pack()

        # Now below I am going to mentioned the toppings which will be available for the user as choose  of toppings.
        tk.Label(myself.root, text="Choose Toppings (comma-separated):").pack()
        toppings_options = ["Cheese", "Peanut Butter", "Avocado"]
        tk.Entry(myself.root, textvariable=myself.toppings_var).pack()

        # Now below I am going to mentioned the condiments which will be available for the user as choose  of condiments while placing order for burger.
        tk.Label(myself.root, text="Choose Condiments (comma-separated):").pack()
        condiments_options = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
        tk.Entry(myself.root, textvariable=myself.condiments_var).pack()

        # Now below I am going to mention the sides that will be available for the users to select while placing the orders for the burgers and the toppings mentioned below are Fries and drinks.
        tk.Label(myself.root, text="Choose Sides (comma-separated):").pack()
        sides_options = ["Fries", "Drink"]
        tk.Entry(myself.root, textvariable=myself.sides_var).pack()

        # Now I am going to mentioned the payment method on how the user can make the payment while placing the order for the burger.
        tk.Label(myself.root, text="Enter Payment Amount: $").pack()
        tk.Entry(myself.root, textvariable=myself.payment_var).pack()

        tk.Button(myself.root, text="Place Order", command=myself.place_order).pack()
# Using the def function below for the payment part.
    def place_order(myself):
        myburger = myself.burger_var.get()
        mytoppings = myself.toppings_var.get().split(',')
        mycondiments = myself.condiments_var.get().split(',')
        mysides = myself.sides_var.get().split(',')
        mypayment = myself.payment_var.get()

        order_items = [myburger] + mytoppings + mycondiments + mysides
        yourtotal_cost = myself.calculate_total(order_items)
        # Using the if function below for the payment part.
        if mypayment < yourtotal_cost:
            messagebox.showerror("Error", "Insufficient payment. Please enter a valid amount.")
        else:
            change = mypayment - yourtotal_cost
            messagebox.showinfo("Order Placed", f"Total: ${yourtotal_cost:.2f}\nChange: ${change:.2f}\nThank you for ordering at Burger Shack!")
    # Using the def function below to calculate the total payment the user name to make for placing an order for a particular burger.
    def calculate_total(myself, items):
        myprices = {"Beef": 6.99, "Chicken": 5.99, "Vegetarian": 3.99,
                  "Cheese": 1.50, "Peanut Butter": 1.75, "Avocado": 1.00,
                  "Ketchup": 1.25, "Mayonnaise": 1.30, "BBQ Sauce": 1.50,
                  "Fries": 3.50, "Drink": 2.99}
        total = sum(myprices[item] for item in items)
        return total
# Now using the if function for the name.
if __name__ == "__main__":
    finalroot = tk.Tk() # Renaming the root to finalroot
    app = RakBurgerShackGUI(finalroot)# The title of this GUI will be RakBurgerShackGUI.
    finalroot.mainloop()# Now start the mainloop.
