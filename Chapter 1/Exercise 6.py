#Pass a loop through numbers from 1 to 100.
for usernum in range(1, 101):
  #We also need to check for the multiples of both 3 and 5 first
  if usernum % 3 == 0 and usernum % 5 ==0:
    print("FizzBuzz")
 #  To Check for multiples of 3 I am using elif statement
  elif usernum % 3 == 0:
      print("Fizz")

# To check for multiples of 5 I am using elif statement again
  elif usernum % 5 == 0:
      print("Buzz")

  # Print the number if it's not a multiple of 3 or 5
  else:
        print(usernum)
  # The results are shown below.
