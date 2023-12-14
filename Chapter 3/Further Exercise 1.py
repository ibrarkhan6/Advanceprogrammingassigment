#In this task I am using my last years vending machine program as well.
# At first we need to import tkinter as tk.
import tkinter as tk
# And than from tkinter import messagebox.
from tkinter import messagebox
# Below are the items that are available in my stock.
myitems_in_stock = [
    {"item_id": 0, "item_name": "Milky Bar", 'item_price': 60},
    {"item_id": 1, "item_name": "Fanta", 'item_price': 90},
    {"item_id": 2, "item_name": "Kurkure", 'item_price': 25},
    {"item_id": 3, "item_name": "Thumbs Up", 'item_price': 90},
    {"item_id": 4, "item_name": "Wai-Wai", 'item_price': 20},
]
# Now mentioning and selecting class as MyVendingMachineApp.s
class MyVendingMachineApp:
    def __init__(myself, root):
        myself.root = root
        myself.root.title("Vending Machine")

        # Now I am going to use the variables which I have mentioned below.
        myself.the_item = []
        myself.reciept = tk.StringVar(value="PRODUCT -- PRICE")

        # Now I am also going to use the  GUI components below.
        myself.label_title = tk.Label(root, text="Vending Machine", font=("Bold", 18))
        myself.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        myself.label_instruction = tk.Label(root, text="Select items to purchase:")
        myself.label_instruction.grid(row=1, column=0, columnspan=2)

        # Now we have to  create a button for each and every item.
        for i, item in enumerate(myitems_in_stock):
            btn_item = tk.Button(root, text=f"{item['item_name']} - ${item['item_price']}", command=lambda idx=i: myself.add_item(idx))
            btn_item.grid(row=i + 2, column=0, pady=5)

        myself.label_total = tk.Label(root, text="Total: $0")
        myself.label_total.grid(row=len(myitems_in_stock) + 2, column=0, pady=10)

        myself.button_print_receipt = tk.Button(root, text="Print Receipt", command=myself.print_receipt)
        myself.button_print_receipt.grid(row=len(myitems_in_stock) + 3, column=0, pady=10)
# Now I am going to use the def function below for the add_item.
    def add_item(myself, idx):
        myself.the_item.append(myitems_in_stock[idx])
        myself.update_total_label()
# Now I am going to use the def function below for the update_total_label.
    def update_total_label(myself):
        total_price = sum(item['item_price'] for item in myself.the_item)
        myself.label_total.config(text=f"Total: ${total_price}")
# Now I am going to use the def function below for the print_receipt.
    def print_receipt(myself):
        receipt_text = create_receipt(myself.the_item)
        messagebox.showinfo("Receipt", receipt_text)
    # Now I am going to use the def function below to create_receipt.
def create_receipt(the_items):
    myreceipt_text = "PRODUCT -- PRICE\n"

    for item in the_items:
        myreceipt_text += f"{item['item_name']}-- {item['item_price']}\n"

    total_price = sum(item['item_price'] for item in the_items)
    receipt_text += f"\nTotal --- ${total_price}\n"

    return receipt_text
# Now using the if function below.
if __name__ == "__main__":
    root = tk.Tk()# Renaming the root to as a finalroot.
    app = MyVendingMachineApp(root)
    root.mainloop()# Now start the
