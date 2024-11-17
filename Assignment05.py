# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   A. Martinez,11/13/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
from typing import TextIO
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file:TextIO = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
parts:list[str] = []
start_scratch: str = '' #Answer if the user wanted to start from scratch after index error

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    # Read from the JSON file
    file = open(FILE_NAME, "r")
    students = json.load(file)
    # file = open(FILE_NAME, "r")
    # for row in file.readlines():
    #     # Transform the data from the file
    #     parts = row.strip().split(',')
    #     student_first_name = parts[0]
    #     student_last_name = parts[1]
    #     course_name = parts[2]
    #     student_data={'first_name':student_first_name,'last_name':student_last_name,'course_name':course_name}
    #     # Load it into our collection (list of lists)
    #     students.append(student_data)
    file.close()
except FileNotFoundError:
    print('File not found. Creating a new file...')
    open(FILE_NAME,'w')
except IndexError:
    print('The input data does not contain the expected 3 columns for FirstName, LastName, Course')
    # Start loop to check for user input
    valid_answer = False
    while not valid_answer:
        # Ask user what to do
        start_scratch = input("Would you like to erase changes and start from scratch. If yes, this will erase local "
                              "changes (yes/no): ")
        # If user says yes, overwrite changes with a blank file.
        # If no, raise error, and let the user fix it themselves.
        if start_scratch == 'yes':
            print('Creating new file...')
            open(FILE_NAME, 'w')
            valid_answer = True
        elif start_scratch == 'no':
            raise IndexError("The input data does not contain the expected 3 columns for FirstName, LastName, Course")
        else:
            print('Unknown input')
except Exception as e:
        print('Unknown Exception', e)
finally:
    if file and not file.closed:
        file.close()
print(students)

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First name should be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Last name should be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print (e)

    # Present the current data in the JSON file by sorting the data by dictionaries
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please enter a valid response (Options 1,2,or 3")

print("Program Ended")
