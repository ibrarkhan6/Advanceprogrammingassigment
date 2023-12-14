# At first we need to initialize a counter for the number of loop iterations.
count = 0

# Secondly we need to use aa while loop keep asking the user if they
# want to continue.
while True:
  user_input = input("Do you want to continue? (Y/N): ").upper()
  count += 1
  # We also need to increment the loop iteration counter.

  #We also need to check if the user input is not 'Y', then we need
  # to break the loop.
  if user_input !='Y':
    break

print(f"The loop was executed {count} times.")
#The results are shown below.