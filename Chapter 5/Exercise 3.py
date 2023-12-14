# Now below I am going to import tkinter as tk.
import tkinter as tk
# Now I am going to  use the class and it will be called  as Employee.
class Employee:
    # Now  I am going to use the def function below.
    def __init__(myself):
        myself.name = ""
        myself.position = ""
        myself.salary = 0.0
        myself.id = ""
    # Now  I am going to use the def function below.
    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id
    # Now I am going to  use the def function again below.
    def getData(self):
        # Now I am going to use the return function below.
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

# Now I am going to use the class and it will be called as  EmployeeGUI.
class EmployeeGUI(tk.Tk):
    def __init__(myself):
        super().__init__()
        myself.title("Employee Details")
        myself.geometry("400x300")
        myself.employees_added = 0
        myself.create_employee_data_fields()

        # Now I am creating a bbutton to add employee.
        add_button = tk.Button(myself, text="Add Employee", command=myself.add_employee)
        add_button.pack() #add_button.pack() have a pady of 10.
    # Uisng the def function below.
    def create_employee_data_fields(myself):
        myself.name_label = tk.Label(myself, text="Name")
        myself.name_label.pack()
        myself.name_entry = tk.Entry(myself)
        myself.name_entry.pack()

        myself.position_label = tk.Label(myself, text="Position")
        myself.position_label.pack()
        myself.position_entry = tk.Entry(myself)
        myself.position_entry.pack()

        myself.salary_label = tk.Label(myself, text="Salary")
        myself.salary_label.pack()
        myself.salary_entry = tk.Entry(myself)
        myself.salary_entry.pack()

        myself.id_label = tk.Label(myself, text="ID")
        myself.id_label.pack()
        myself.id_entry = tk.Entry(myself)
        myself.id_entry.pack()
    # Now I am going to use the def function again below.
    def add_employee(myself):
        if myself.employees_added >= 5:
            print("Maximum number of employees reached (5 employees).")
        else:
            name = myself.name_entry.get()
            position = myself.position_entry.get()
            salary = float(myself.salary_entry.get())
            emp_id = myself.id_entry.get()

            employee = Employee()
            employee.setData(name, position, salary, emp_id)
            222
            print(employee.getData())

            myself.employees_added += 1


#  Now we need to instantiate the EmployeeGUI class at end.
app = EmployeeGUI() # Also add employeeGUI
app.mainloop()# Start the mainloop now.