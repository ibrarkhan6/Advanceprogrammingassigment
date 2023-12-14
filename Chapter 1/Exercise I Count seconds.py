# At very first we need to ask the user to write the number of days.

goodays = int(input("Enter the number of days: "))

# Now we have to convert days to hours, hours to minutes and as well as minutes
# to seconds.

hours = goodays * 24
minutes = hours * 60
seconds = minutes * 60

# Now at last we need to print the result.
print("Number of seconds in", goodays, "days is:", seconds)