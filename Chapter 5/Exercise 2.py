# First we need to import tkinter as  tk.
import tkinter as tk
# Now below I am going to use the class below with name Students.
class Students:
    def __init__(myself, name, mark1, mark2, mark3):
        myself.name = name
        myself.mark1 = mark1 #Mark 1
        myself.mark2 = mark2 # Mark 2
        myself.mark3 = mark3 #Mark 3s
# Now below I am going to use the def function.
    def calcGrade(myself):
        # Using below the return function.
        return (myself.mark1 + myself.mark2 + myself.mark3) / 3
# Now I am going to use the def function below.
    def display(myself):
        average = myself.calcGrade() # Average
        return f"Name: {myself.name}\nAverage Grade: {average:.2f}"
# Now again below I am going to use the class and name it as StudentGUI.
class StudentGUI:
    # Now again I am going to use the def function.
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Student Information")

        # Now again I  am going to create 4 labels below.
        tk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=10)# First label will have text inside which is going to be "Name".
        tk.Label(master, text="Mark 1:").grid(row=1, column=0, padx=10, pady=10)# Second label will have text inside which is going to be "Mark 1".
        tk.Label(master, text="Mark 2:").grid(row=2, column=0, padx=10, pady=10)# Third label will have text inside which is going to be "Mark 2".
        tk.Label(master, text="Mark 3:").grid(row=3, column=0, padx=10, pady=10)# Fourth label will have text inside which is going to be "Mark 3".

        # Now we need to create entry widgets.
        myself.name_entry = tk.Entry(master)
        myself.mark1_entry = tk.Entry(master)
        myself.mark2_entry = tk.Entry(master)
        myself.mark3_entry = tk.Entry(master)

        myself.name_entry.grid(row=0, column=1, padx=10, pady=10)
        myself.mark1_entry.grid(row=1, column=1, padx=10, pady=10)
        myself.mark2_entry.grid(row=2, column=1, padx=10, pady=10)
        myself.mark3_entry.grid(row=3, column=1, padx=10, pady=10)

        # Now I am going to create buttons below and the text inside will be written as "Display Info". 
        tk.Button(master, text="Display Info", command=myself.display_info).grid(row=4, column=0, columnspan=2, pady=10)
    # Now below I am going to use the def function.
    def display_info(self):
        name = self.name_entry.get()
        mark1 = int(self.mark1_entry.get())
        mark2 = int(self.mark2_entry.get())
        mark3 = int(self.mark3_entry.get())
        
        student_obj = Students(name, mark1, mark2, mark3)
        result = student_obj.display()

        # Now I am going to display the result in a new window for the user.
        result_window = tk.Toplevel(self.master)
        tk.Label(result_window, text=result).pack(padx=10, pady=10)
# Using the if function below.
if __name__ == "__main__":
    finalroot = tk.Tk()
    app = StudentGUI(finalroot) # The application will be called as StudentGUI.
    finalroot.mainloop()# Now start the mainloop in the end.
#  By this GUI App the class will have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int).
#  This app  class will also  have the following methods calcGrade() - and will  return an average from the three marks.display()- should output the student name and calculated grade average.
# This GUIApp will also create one object using a constructor that contains parameters to initialize all of the variables.
# Will alsp ask the user to input the variable values using input() and pass the values to the second object.