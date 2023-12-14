import json

# I am using the def function in order to create or update the JSON file for the user.
def update_json_file(myfile_path, data):
    # I am using below the with function.
    with open(myfile_path, 'w') as json_file:
        json.dump(data, json_file, indent=2) # The indent is 2.

# I am once again using the def function in order to read and display individual values from the JSON file.
def read_and_display_json(myfile_path):
    with open(myfile_path, 'r') as myjson_file:
        mystudent_data = json.load(myjson_file)
      # Using the print below.
        print("\nDetails of the Student are")# By this we will print "Details of the Student are". 
        print(f"\tName: {mystudent_data['Name']}")
        print(f"\tID: {mystudent_data['ID']}")
        print(f"\tcourse: {mystudent_data['course']}")
        # Using the if function below.
        if 'CourseDetails' in mystudent_data:
            print("\tGroup:", mystudent_data['CourseDetails']['Group'])
            print("\tYear:", mystudent_data['CourseDetails']['Year'])

#  Now I need to get user input.
mystudent_name = input("Enter the student name: ")
mystudent_id = int(input("Enter the student ID: "))
mystudent_course = input("Enter the student course: ")

# Now I also need to create initial student dictionary which I am going to do below. 
student_details = {
    "Name": mystudent_name,
    "ID": mystudent_id,
    "course": mystudent_course
}

# Now I also need to create or update the JSON file with the initial student details.
update_json_file('StudentJson.json', student_details)

# Now I also need to read  and display individual values from the JSON file for the user.
read_and_display_json('StudentJson.json')

# Now I also need to  append coursedetails to the existing student dictionary for the user.
course_details = {
    "Group": "A",
    "Year": 2
}
student_details["CourseDetails"] = course_details

#  Now I also need to update the JSON file with the modified student details for the user.
update_json_file('StudentJson.json', student_details)

# Now at need I need to make sure to read and display individual values from the updated JSON file for the user.
read_and_display_json('StudentJson.json')
