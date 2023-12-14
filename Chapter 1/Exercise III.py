# At first we need to get the number of rows for the pattern from the user.
rows = int(input("Now enter the number of rows for the pattern: "))

#Now we need to use outer loop in order to handle number of rows.
for a in range(0, rows):
  #Now we need to use inner loop to handle spaces before asterisks.
    for b in range(0, rows - a -1):
        print(" ", end= ' ')
    for c in range(0, 2 * a +1):
        print("*", end= ' ')
      # Now we have to move to the next line after each row is printed
    print()