# At first we need to import tkinter as tk.
import tkinter as tk

#  The data which we needs to use is mentioned below.
companybrands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
myvalues = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Now we need to create a tkinter window for the window.
finalroot = tk.Tk()
finalroot.title('Most Valuable Brands Worldwide in 2023')

# Now we also need to create a canvas for this task.
mycanvas = tk.Canvas(finalroot, height=500,width=500,)
mycanvas.pack()

# Now we need to make sure to Draw horizontal barsgraph.
bar_height = 20
for brand, value in zip(companybrands, myvalues):
    mycanvas.create_rectangle(10, bar_height, value, bar_height + 15, fill='skyblue')
    mycanvas.create_text(value + 20, bar_height + 7, anchor='w', text=f"{brand}: {value}B")

    # Now we also need to increase the y-coordinate for the next bar as followed.
    bar_height += 30

#Now start the mainloop to get the output.
finalroot.mainloop()
