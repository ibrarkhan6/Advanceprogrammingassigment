# At first we need to  import tkinter as tk.
import tkinter as tk
#Using the  def function now to write the file.
def write_to_file():#The file name is "bio.txt"
    with open("bio.txt", "w") as myfile:
        #The first value is "Name" and the code used is myname_entry.
        myfile.write(f"Name: {myname_entry.get()}\n")
        #The second value is "Age" and the code used is myname_entry.
        myfile.write(f"Age: {yourage_entry.get()}\n")
        #The third entry is "Hometown" and the code used is myname_entry.
        myfile.write(f"Hometown: {myhometown_entry.get()}\n")
        #The user have to type in the  values in order to get the result.
# Again using the def to read from the file.
def read_from_file():
    try:
        #Again the file name is mentioned as "bio.text" which is saved inside the file.
        with open("bio.txt", "r") as myfile:
            content = myfile.read()
            myoutput_text.config(state=tk.NORMAL)
            myoutput_text.delete(1.0, tk.END)
            myoutput_text.insert(tk.END, content)
            myoutput_text.config(state=tk.DISABLED)
# Except is used for FileNotFoundError as below.
    except FileNotFoundError:
        myoutput_text.config(state=tk.NORMAL)
        myoutput_text.delete(1.0, tk.END)
        myoutput_text.insert(tk.END, "File not found.")
        myoutput_text.config(state=tk.DISABLED)

#Now we have to create a main window for this task.
myapp = tk.Tk()
#My application title is "Bio Information".
myapp.title("Bio Information")

#Now we have to create an entry widgets below for the labels for "Name" value.
myname_label = tk.Label(myapp, text="Name:")#The code mentioned for labels is myname_label for "Name" value.
myname_label.grid(row=0, column=0, sticky=tk.E)#Here is the myname_label.grid with no rows and columns.
myname_entry = tk.Entry(myapp)#Here is myname_entry code.
myname_entry.grid(row=0, column=1)#myname_entry.grid have one coulum however it have no rows.
#Now we have to create an entry widgets below for the labels for "Age" value.
yourage_label = tk.Label(myapp, text="Age:")#The code mentioned for labels is yourage_label for "Age" value.
yourage_label.grid(row=1, column=0, sticky=tk.E)#Here is the yourname_label.grid with one row and zero columns.
yourage_entry = tk.Entry(myapp)#Here is your_entry code.
yourage_entry.grid(row=1, column=1)#yourage_entry.grid have one row and column.

#Now we have to create an entry widgets below for the labels for "Hometown" value.
myhometown_label = tk.Label(myapp, text="Hometown:")#The code mentioned for labels is myhometown_label for "Name" value.
myhometown_label.grid(row=2, column=0, sticky=tk.E)#Here is the myhometown_label.grid with 2 rows and zero columns.
myhometown_entry = tk.Entry(myapp)#Here is myhometown_entry code.
myhometown_entry.grid(row=2, column=1)#yourage_entry.grid have two rows and one column.

#Now below I have to create a button for my all my 3 values.
mywrite_button = tk.Button(myapp, text="Write to File", command=write_to_file)# The code that I have used for creating a button is mywrite_button.
mywrite_button.grid(row=3, column=0, columnspan=2, pady=10)#mywrite_button.grid is used and it has 3 rows and no columns with columnspan is 2 and have pady of 10.

myread_button = tk.Button(myapp, text="Read from File", command=read_from_file)
myread_button.grid(row=4, column=0, columnspan=2, pady=10)#myread_button.grid is used and it has 4 rows and no columns with columnspan is 2 and have pady of 10.

# Now we have to make text width for the output.
# It has height of 6 width of 30 and state of tk.DISABLED.
myoutput_text = tk.Text(myapp, height=6, width=30, state=tk.DISABLED)
myoutput_text.grid(row=5, column=0, columnspan=2)#myoutput_text.grid have 5 rows with no column and with columnspan is 2.

#Now start the mainloop at the very end.
myapp.mainloop()