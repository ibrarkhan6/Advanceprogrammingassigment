# First import tkinter as tk.
import tkinter as tk
#Secondly from tkinter import filedialog
from tkinter import filedialog
# Now below we have to use class function.
class PetrolCostCalculatorApp:
# The application name will be called as ThePetrolCostCalculatorApp.
    def __init__(myself, root):
        myself.root = root
        myself.root.title(" The Petrol Cost Calculator App")
      # Now below I am creating label and the text inside the labels will be "Select the petrol price file". 
        myself.label = tk.Label(root, text="Select the petrol price file:")
        myself.label.pack(pady=10)# myself.label.pack with pady 10.
      # Now below I am creating button and the text inside in it will be called as "Browse".
        myself.browse_button = tk.Button(root, text="Browse", command=myself.browse_file)
        myself.browse_button.pack(pady=10)# myself.browse_button.pack will have a pady of 10.
      # Now below I am creating button and the text inside in it will be called as "Calculate".
        myself.calculate_button = tk.Button(root, text="Calculate", command=myself.calculate)
        myself.calculate_button.pack(pady=10)
      # Labels.
        myself.result_label = tk.Label(root, text="")
        myself.result_label.pack(pady=10)
    # Using below the def function.
    def browse_file(myself):
        myfile_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if myfile_path:
            myself.file_path = myfile_path
            myself.label.config(text=f"Selected file: {myfile_path}")
    # Below using the def function to calculate.
    def calculate(myself):
        # Using below try function.
        try:
            # Using below the with function.
            with open(myself.file_path, 'r') as file:
                lines = file.readlines()[1:]  # Skip the header line
                total_cost = 0
                total_liters = 0
                under_3_5_liters = 0
            # Using below for function.
                for line in lines:
                    liters, cost = map(float, line.strip().split('\t'))
                    total_cost += cost
                    total_liters += liters
            # Using below the if function.
                    if cost/liters < 3.5:
                        under_3_5_liters += liters

                cost_per_liter = total_cost / total_liters
                average_price_per_liter = cost_per_liter

                theresult_text = f"Cost per liter: {cost_per_liter:.2f} AED\n" \
                              f"Average price per liter: {average_price_per_liter:.2f} AED\n" \
                              f"Liters bought at under 3.5 AED per liter: {under_3_5_liters:.2f} liters"

                myself.result_label.config(text=theresult_text)
        # Using below the except function.
        except Exception as e:
            myself.result_label.config(text=f"Error: {str(e)}")
# Using below the if function.
if __name__ == "__main__":
# Now root is also called the finalroot.
    finalroot = tk.Tk()
# Now the app will be called PetrolCostCalculatorApp.
    app = PetrolCostCalculatorApp(finalroot)
    # Now the root will be called as final root.
    # Now start the mainloop.
    finalroot.mainloop()
