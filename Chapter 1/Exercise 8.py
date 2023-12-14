# The number of rows that are present in this pattern are 5.
rows = 5

# Secondly we have to outer loop to iterate through rows.
for y in range(1, rows +1):

  # Use inner  loop to iterate through numbers in each row.
  for z in range(1, y +1):
    # Print
    print(z, end=" ")
  # We also need to print the current number followed by a space.
  print()
  # We also need to  move to the next line after each row.

#The results are shown below.