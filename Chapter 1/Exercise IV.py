#Now we have the given list.
Staffnames = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol",
              "Zainab","Iftikhar", "Arshiya","Rafia","Jake"]
#At first we need to initialize an empty dictionary to store item counts.
count_items = {}

#Now we need to iterate through the list and count the occurrences of each item.
for item in Staffnames:
#Also kindly note if the item is already in the dictionary, increment its count.
    if item in count_items:
      count_items[item] +=1
# Also kindly note if the item is not in the dictionary,add it with a count of 1
    else:
      count_items[item] = 1
#Now we have to print counts item
for item, count in count_items.items():
  print(f"{item}: {count} times")
