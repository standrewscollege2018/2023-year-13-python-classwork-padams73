''' Student management system '''

class Student:
    ''' Student objects have attributes like name, phone, address, and a list of
    the classes they are enrolled in. There are also getter functions for each,
    as well as functions to display all of their information. '''

    def __init__(self, name):
        ''' The init function is called automatically when the object is created'''

        print("Hello")

        # Assign name to new student
        self._name = name

        # Add the new student to the students list
        students.append(self)
    
    
    def get_name(self):
        ''' Return the name of the student '''

        return self._name

# list to store all students
students = []

# Create students
Student("John Smith")
Student("Joanna Smith")

# Loop through all students and display names
for s in students:
    print(f"Hi my name is {s.get_name()}")
