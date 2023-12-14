# We need to create a tubles with values in this task.
useryears = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

# We also need to access the value at index -3.
print("Value at index-3", useryears[-3])

# We also need to reverse the tuple and print the original tuble and also
# reversed tuple.
reversed_year = tuple(reversed(useryears))
print("Original Tuple:", useryears)
print("Reversed Tuple:", reversed_year)

# We also need to count the number of times 2009 is in the tuple.
usercount_2009 = useryears.count (2009)
print("Number of times 2009 appears in the tuble:", usercount_2009)

#  We also need to get the index value of 2018.
userindex_2018 = useryears.count(2009)
print("Index of 2018:", userindex_2018)

# We also need to find the length of the given tuble.
usertuple_length = len(useryears)
print("Length of the tuple:", usertuple_length)