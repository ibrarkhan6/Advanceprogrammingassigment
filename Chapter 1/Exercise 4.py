# At first we need to promote the user for three numbers.
usernum1 = float(input("Enter the first number: "))
usernum2 = float(input("Enter the second number: "))
usernum3 = float(input("Enter the third number: "))

#Secondly we need to compare the numbers to find the largest.
if usernum1 >= usernum2 and usernum1 >= usernum3:
  the_largest = usernum1

# Using elif statement
elif usernum2 >= usernum1 and usernum2 >= usernum3:
  the_largest = usernum2
  #Using the else statement
else:
 the_largest = usernum3

# At last we need to print the largest number
print(f"The largest number is: {the_largest}")
#The results are shown below.