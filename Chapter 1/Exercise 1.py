# At very first we need to promote the user for the name and age.
 # This is the personal details of the user.
username = input("Hello, user!\nWhat is your name?\n").title()
userage = int(input("What is your age?\n"))

# Secondly we need to calcuate the length of the name and age after one year.
# This part involves the calculation of alphabets such the name and age.
username_length = len(username)
userfuture_age = userage + 1

# Thirdly we need to print the formatted output at the end.
# In order to get the final result over a period of time.
print(f"It is good to  meet you,{username}")
print("The length of your name is:")
print(username_length)
print(f"You will be {userfuture_age} in a year.")
#The results are shown below.