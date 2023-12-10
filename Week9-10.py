import re

#Only letters and spaces 
class Validator:
    @staticmethod 
    def validate_name(name):
        return bool(re.match("^[a-zA-Z ]+$", name))

#Basic email patter and validation
    @staticmethod 
    def validate_email(email):
        return bool(re.match("^\w+@\w+\.\w+$", email))
    
class Person: 
    def __init__(self, name, email):
       self.name = name 
       self.email = email 
    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
class Student(Person):
    def __init__(self, name, email, student_id, program_of_study):
        super ().__init__(name, email)
        self.Student_id = student_id
        self.Program_Of_Study =program_of_study
    def display_information(self):
        super().display_information()
        print(f"Student id: {self.student_id}")
        print(f"program of study: {self.program_of_study}")
class Instructor(Person):
    def __init__(self, name, email, instructor_id, last_institution, highest_degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.last_institution = last_institution
        self.highest_degree = highest_degree
    def display_information(self):
        super().display_information()
        print(f"instructor_id:{self.instructor_id}")
        print(f"last_institution:{self.last_institution}")
        print(f"highest_degree:{self.highest_degree}")

College_records = []
#Gathering Information Loop 
while True: 
    individual_type = input("Enter the type of individual (instructor/student) or 'done'to finish: ").lower()
    if individual_type == 'done':
        break
    if individual_type not in ['intructor', 'student']:
        print("invalid input. please enter 'instructor', 'student', or 'done'.")
        continue 
name = input("enter name:")
while not Validator.validate_name(name):
    print("invalid name format. only letters and spaces allowed.")
    name = input("re-enter name:")
email = input("enter email address")
while not Validator.validate_email(email):
    print("invalid email format.")
    email = input("re-enter email address:")
#Validation for instructor ID length and type can be added here
if individual_type == 'instructor':
    instructor_id = input ("enter instructor id: ")
    last_institution = input("enter last institution graduated from: ")
    highest_degree = input("enter highest degree earned: ")
    intructor = Instructor(name, email, instructor_id, last_institution, highest_degree)
    College_records.append(Instructor)
#Validationfor student ID length and type can be added here 
else: 
    student_id= input("enter student id: ")
    program_of_study=input("enter program of study: ")
    student = Student(name, email, student_id, program_of_study)
    College_records.append(student)
#Displaying collected information 
for record in College_records:
    record.display_information()
    print()