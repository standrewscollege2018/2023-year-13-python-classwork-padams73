''' This file demonstrates how to combine object orientation 
and GUI
We will import students from a csv, create them as objects, 
then display them in the GUI '''

# Import Tkinter libraries
from tkinter import *
from tkinter import messagebox

########### Define the Student class and its functions ##############

class Student:
    ''' Student objects have attributes like name, phone, address, and a list of
    the classes they are enrolled in. There are also getter functions for each,
    as well as functions to display all of their information. '''

    def __init__(self, name, age, phone, classes):
        ''' The init function is called automatically when the object is created'''

         # Assign properties to new student
        # All properties have an underscore in front
        # This means the property is private to the object
        # and they can only be referenced by calling a getter
        # function from the object (encapsulation)
        self._name = name
        self._phone = phone
        self._age = age
        self._classes = classes

        # Student is automatically enrolled
        self._enrolled = True

        # Add the new student to the students list and their name to a list too
        students.append(self)
        student_names.append(name)
    
    
    def get_name(self):
        ''' Return the name of the student '''

        return self._name
    
    def get_phone(self):
        ''' Return the phone number '''

        return self._phone

    def get_age(self):
        ''' Return their age '''

        return self._age
    
    def get_classes(self):
        ''' Return list of classes they are enrolled in '''

        return self._classes
    
    def get_enrolled(self):
        ''' Return enrolment status '''

        return self._enrolled

    def unenrol(self):
        ''' This is a setter function that changes the value of a property '''

        self._enrolled = False

############ Lists  #########

# List of student objects
students = []
# List of student comments
student_names = []
# List of class codes
classes = ['MAT', 'GRA', 'ENG', 'BIO', 'DTC', 'PHY']


############# Functions ############################
def generate_students():
    ''' Function imports students from csv file '''

    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes = []
            i = 3
            while i in range(3,8):
                classes.append(line[i])
                i += 1
            Student(line[0], int(line[1]), line[2], classes)


def populate_listbox():
    ''' reload and repopulate the listbox '''

    # Clear listbox first
    student_listbox.delete(0,END)
    # Then repopulate
    for name in student_names:
        student_listbox.insert(END, name)


def filter_students(c):
    ''' This function will display all students in the selected class '''

    

################### GUI ####################

# Create and configure main window
root = Tk()
root.title("Demo of OO and Tkinter")
root.geometry('400x400')

# Option Menu containing list of names
selected_class = StringVar()
# Set the initial selection to the first item in the names list
selected_class.set(classes[0])
class_menu = OptionMenu(root, selected_class, *classes, command=filter_students)
class_menu.config(width=20,bg='#123456', fg='white')
class_menu.grid(row=0, column=0)


student_listbox = Listbox(root)
student_listbox.grid(row=0, column=1)

# Import students and populate the listbox
generate_students()
populate_listbox()

# Start the program runnning
root.mainloop()