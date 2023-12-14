#Below is given the list of the tuples
overallmarks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),
 ("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
#Now we need to sort the list of the tuples based  on marks in ascending order-
#For example (low to high)
now_sorted_low_to_high = sorted(overallmarks, key=lambda x: x[1])
#Now we need to sort the list of the tuples based  on marks in descending order-
#For example (high to low)
now_sorted_high_to_low = sorted(overallmarks, key=lambda x: x[1], reverse=True)

#Now we need to print the sorted list in order to get the final results for the
#- overallmarks
print("Sorted by marks(low to high):", now_sorted_low_to_high)
print("Sorted by marks(low to high):", now_sorted_high_to_low)