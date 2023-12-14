# At first we need to import tkinter as tk.
import tkinter as tk
# Secondly from tkinter import messagebox.
from tkinter import messagebox
# Using below class function.
#The name of this gui application will be ThePasswordCheckerApp.
class ThePasswordCheckerApp:
    #Using the def function below.
    def __init__(yourself, root):
        yourself.root = root
        yourself.root.title("The Password Checker App")

        # Now below making labels for this task and inside the label will be text mentioned called "Enter Password".
        yourself.label = tk.Label(root, text="Enter Password:")
        yourself.label.pack(pady=10) # and yourself.label.pack has a pady of 10.

        # Now we need to entry widget for user to enter a password as he requires.
        yourself.password_entry = tk.Entry(root, show="*")
        yourself.password_entry.pack(pady=10) # yourself.password_entry.pack have a pady of 10.

        # Now I am creating button below using the  codes below and text inside the button will be "Check Password".
        yourself.check_button = tk.Button(root, text="Check Password", command=yourself.check_password)
        yourself.check_button.pack(pady=10) # Now yourself.check_button.pack have a pady of 10.

        #Below is the variable  to store the number of remaining attempts for the user and therefor the attempts are 5.
        yourself.remaining_attempts = 5
     # Now using below the def function.
    def check_password(yourself):
        # Now we need to get the password entered by the user.
        myuser_password = yourself.password_entry.get()

        # Now we need to check password validity for the user.
        # Now again using below the if function.
        if yourself.is_valid_password(myuser_password):
            messagebox.showinfo("Success", "Password is valid!")
            yourself.root.destroy()
            # Now again using the else function.
        else:
            yourself.remaining_attempts -= 1
             # Now again using below the if function.
            if yourself.remaining_attempts > 0:
                messagebox.showwarning("Invalid Password", f"Invalid password! {yourself.remaining_attempts} attempts remaining.")
                 # Now again using the else function.
            else:
                messagebox.showerror("Alert", "Authorities have been alerted! Too many failed attempts.")
                yourself.root.destroy()

    def is_valid_password(myself, themainpassword):
        # now we need to check password criteria for the user.
        return (
            any(c.islower() for c in themainpassword) and
            any(c.isdigit() for c in themainpassword) and
            any(c.isupper() for c in themainpassword) and
            any(c in ['$', '#', '@'] for c in themainpassword) and
            6 <= len(themainpassword) <= 12
        )
# Now using below if function.
if __name__ == "__main__":
    # Root is name as finalroot.
    finalroot = tk.Tk()
    #The gui app will be called as ThePasswordCheckerApp.
    app = ThePasswordCheckerApp(finalroot)
    finalroot.mainloop()# Now run the mainloop.
