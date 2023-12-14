# At first we need to import tkinter as tk.
import tkinter as tk

# Now we need to create the main window.
myroot = tk.Tk()
myroot.title(" My Line Graph with Canvas")

# Now we need to create a canvas widget.
mycanvas = tk.Canvas(myroot, width=300, height=300, bg="white")
mycanvas.pack()

#  Now the line will pass from (1, 2) to (6, 8).
mycanvas.create_line(10, 290, 260, 10, fill="blue", width=2)

# Where as the dotted line will pass  from (1, 3) to (2, 8) to (6, 1) to (8, 10).
mycanvas.create_line(10, 290, 30, 10, fill="red", width=1, dash=(2, 2))
mycanvas.create_line(30, 10, 130, 10, fill="red", width=1, dash=(2, 2))
mycanvas.create_line(130, 10, 260, 240, fill="red", width=1, dash=(2, 2))
mycanvas.create_line(260, 240, 290, 10, fill="red", width=1, dash=(2, 2))

# Now run the main loop to get the output.
myroot.mainloop()
