# Generate a file with 100 integers from 0 to 100, each on a new line in order to go further ahead of the text.
with open("numbers.txt", "w") as file: #Below is file created and saved in folder with the name "numbers.txt".
    for num in range(101):#Below is the code number for the integers for the ranges in from 1 to 101.
        file.write(str(num) + "\n")
#Print function is used the file "numbers.txt" which is generated with integers particularly from 0 to 100.
print("File 'numbers.txt' generated with integers from 0 to 100.")

# Now we have to read data from the file and create a list for it with functions and codes below.
with open("numbers.txt", "r") as file:
    mynumbers_str = file.read().splitlines()

# Now we haeve to convert the list of strings to a list of integers to perfrom the task.
mynumbers = [int(num) for num in mynumbers_str]

#Now we have to output the values in integer format at the end in order to get the result.
print("List of Numbers (as integers):", mynumbers)
#In the end as you will run the program you will get the result which the user requires as per the task allocated to him.