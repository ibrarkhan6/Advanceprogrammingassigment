# At first from datetime import datetime.
from datetime import datetime
# Now we need to use the def function.
def calculate_age(mydob_str):
    # Now I am going to use the try function below.
    try:
        mydob_date = datetime.strptime(mydob_str, "%m/%d/%Y")
        
        mytoday = datetime.today()
        myage = mytoday.year - mydob_date.year - ((mytoday.month, mytoday.day) < (mydob_date.month, mydob_date.day))
    # Now I am going to use the return function below.
        return f"Your age is {myage} years"
    # Now I am going to use the except function below.
    except ValueError:
        # Now I am going to use thr return function.
        return "Invalid date format"

# Now we need to get user input for this program.
mydob_input = input("Enter your date of birth (mm/dd/yyyy): ")# Setting the date as mm/dd/yyyy


# Now we also need to calculate age and display result for this program.
myresult = calculate_age(mydob_input)
print(myresult)
