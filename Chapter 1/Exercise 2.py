# At first we need to promote the user for two integers.
# We will  try and get two integers to promote the user.
usernum1 = int(input("Enter the first integer: "))
usernum2 = int(input("Enter the second integer: "))

# Secondly we need to perform the calculation which
# very important part.
usersum_result = usernum1 + usernum2
userdiff_result = usernum1 - usernum2
userproduct_result = usernum1 * usernum2

# We also need to check that if the second number is zero to avoid division
# By zero
if usernum2 != 0:
  userquotient_result = usernum1 / usernum2
  userremainder_result = usernum1 % usernum2

else:
  userquotient_result = "Undefined (division by zero)"
  userremainder_result = "Undefined (division by zero)"
# At last we need to print the results.
print(f"Sum: {usersum_result}")
print(f"Difference: {userdiff_result}")
print(f"Product: {userproduct_result}")
print(f"Quotient: {userquotient_result}")
print(f"Remainder: {userremainder_result}")
#The results are shown below.