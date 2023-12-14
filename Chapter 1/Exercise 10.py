# In this task we need to create a dictionary for a film details.
Myfilm_details = {
    "Title": "Jaawan",
    "Director": "Atlee",
    "Genre": "Politics",
    "Main Character": "Shahrukh Khan",
    "Movie Language ": "Hindi",
}
# We also need to display film details using a loop ti get the results.
print("Film Details:")
for key, value in Myfilm_details.items():
    print(f"{key}: {value}")