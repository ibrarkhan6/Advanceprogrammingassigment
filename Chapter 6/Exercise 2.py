# For the array a = [20,23,82,40,32,15,67,52] print the output of following.
a = [20, 23, 82, 40, 32, 15, 67, 52]

# At first we need to find the indices of even numbers.
myeven_indices = [index for index, value in enumerate(a) if value % 2 == 0]
print("Indices of even numbers:", myeven_indices)

# Now we need to sort the array.
thesorted_array = sorted(a)
print("Sorted array:", thesorted_array)

# Now we need to slice elements from index 3 to the end of the array.
myslice1 = a[3:]
print("Slice from index 3 to the end:", myslice1)

# Now we need to slice elements from index 0 to index 4.
myslice2 = a[:5]
print("Slice from index 0 to index 4:", myslice2)

#  Now we need print  [32, 15, 67] using negative slicing for the user.
mynegative_slice = a[-5:-2]
print("Negative slicing to get [32, 15, 67]:", mynegative_slice)
