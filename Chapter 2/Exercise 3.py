# At first we need to import tkinter as tk.
import tkinter as tk
#  Now using def function below.
def validate_login():
    # Now we also need to placeholder validation function.
    print("My Login button pressed")# The page title will be "My Login button pressed".
# Now naming the root as finalroot.
finalroot = tk.Tk()
finalroot.title("User Login Page")

# Now we need to make username label and entry for this  login page.
tk.Label(finalroot, text="Username:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
myusername_entry = tk.Entry(finalroot)
myusername_entry.grid(row=0, column=1, padx=10, pady=5)

# Now we also need to create a password label and entry for this login page.
tk.Label(finalroot, text="Password:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
mypassword_entry = tk.Entry(finalroot, show="")  # Now we should also show '' for password.
mypassword_entry.grid(row=1, column=1, padx=10, pady=5)

# Now we should also make a login button for this login page.
mylogin_button = tk.Button(finalroot, text="Login", command=validate_login)
mylogin_button.grid(row=2, column=0, columnspan=2, pady=10)
# Now start the mainloop.
finalroot.mainloop()