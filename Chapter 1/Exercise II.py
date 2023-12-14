6
# At first we need to get a number from the user.
thenumber = int(input("Enter a number: "))

#Now we have to initialize a variable in order to store the sum of the digits.
the_sum_of_digits = 0

#Now we have to pass loop through the digits in the number and add it to-
# the_sum_of_digits
while thenumber > 0:
  digit = thenumber % 10
  the_sum_of_digits += digit
  thenumber //= 10

#Now we have to print the result.
print(" The sum of digits in the given number is:", the_sum_of_digits)
