#Below is the original list.
citylocations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

#Now we have to print the list and length of the list.
print("Original List:", citylocations)
print("Length of the list", len(citylocations))

#Now we have to use the sorted() to print the list in alphabetical order without
#Modyfing the actual results.
sorted_list = sorted(citylocations)
print("Sorted List(Alphabetical Order):",sorted_list)

#Also kindly note the original list is still in its original order
print("Origianl List(Still in Original Order):",citylocations)

#Now we have to use the sorted() to print the list in reverse alphabetical order
#Without changing the order of the original list.
myreverse_sorted_list = sorted(citylocations, reverse=True)
print("Sorted List(Reverse Alphabetical  Order):",citylocations)

#Also kindly note the original list is still in its original order
print("Origianl List(Still in Original Order):",citylocations)

#Now have to use reverse() to change the order of the list
citylocations.reverse()
print("Reversed List:", citylocations)

#Now we have to use the sort() to change the list to alphabetical order.
citylocations.sort()
print("List sorted in Alphabetical Order:",citylocations)

#Now we have to use the sort() to change the list to reverse alphabetical order.
citylocations.sort(reverse=True)
print("List Sorted in Reverse Alphabetical Order:",citylocations)
