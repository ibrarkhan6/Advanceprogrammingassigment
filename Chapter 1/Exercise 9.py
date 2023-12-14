# Firstly we need to create an integer list with 10 values.
userinteger_list = [2,5,7,1,9,3,4,6,8,10]

# Secondly we need to output the list using a for loop.
print("Original list:")
for num in userinteger_list:
  print(num, end=" ")
print()

# Thirdly we need to output the highest and lowest value.
print("Highest value:", max(userinteger_list))
print("Lowest value:", min(userinteger_list))

# Fourtly we need to sort the elements in ascending order.
userinteger_list.sort()
print("Sorted in ascending order:", userinteger_list)

# We also need to sort the elements in descending order.
userinteger_list.sort(reverse=True)
print("Sorted in descending order:", userinteger_list)

# We also need to append the elements.
userinteger_list.append(11)
userinteger_list.append(12)

# At list we need to  print the list after the appending.
print("List after appending elements:", userinteger_list)
#The results are shown below.