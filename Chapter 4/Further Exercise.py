# Import tkinter as tk.
import tkinter as tk
# Than import as re.
import re
# Using the class function below.
class TheRegexCheckerApp:
    # Using the def function again.
    def __init__(yourself, root):
        yourself.root = root
        yourself.root.title("The Regex Checker")
    # Creating label below and the text inside should be "Enter a string".
        yourself.label = tk.Label(root, text="Enter a string:")
        yourself.label.pack(pady=10)#yourself.label.pack has pady of 10.
    
        yourself.entry = tk.Entry(root)
        yourself.entry.pack(pady=10)
    # Below mentioned is label.
        yourself.result_label = tk.Label(root, text="")
        yourself.result_label.pack(pady=10)

        yourself.create_buttons()
    # Using the def function again to create button.
    def create_buttons(yourself):
        patterns = [
            (r'^[a-zA-Z0-9_]+$', "Letters, numbers, and underscores"),
            (r'^[0-9].*', "Starts with a specific number"),
            (r'\b\w+\b', "Substrings within a string"),
            (r'^\w+', "Word at the beginning of a string")
        ]
    # Using the for function below for descriptions in patterns.
        for pattern, description in patterns:
            button = tk.Button(yourself.root, text=description, command=lambda p=pattern: yourself.check_regex(p))
            button.pack(pady=5)
    # Using the def function below,
    def check_regex(yourself, pattern):
        user_input = yourself.entry.get()
        match = re.match(pattern, user_input)
        # Using the if function below.
        if match:
            yourself.result_label.config(text=f"Matched: {match.group()}")
            # Using the else function below.
        else:
            yourself.result_label.config(text="No match.")
# Using the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk() # Root is renamed as finalroot.
     # The app title is  TheRegexCheckerApp.
    app = TheRegexCheckerApp(finalroot)
    finalroot.mainloop() # Now start the mainloop.

    # By this program the user will match a string that contains only upper and lowercase letters, numbers, and underscores.
    # By this program the user will match a string will start with a specific number.
    # By this program the user will be able  to find the substrings within a string.
    # By this program the user will be able to match a word at the beginning of a string