#Pass a loop through numbers from 1 to 100.
for usernum in range(1,101):
  # We also need to check and make sure that the number is odd.
  if usernum % 2 != 0:
    # If the number is odd then we need to skip to the next iteration without
    #printing
    continue
  # If even number than print the number.
  print(usernum)

#The results are shown below.