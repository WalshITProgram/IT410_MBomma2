#This is a case of basic form variable establishment 
#Using Basic Form is a common and simple way of storing user data within a program as a stored variable for future reference in code. 
yourname=input("Hi, What is your name? ") 
print( "Thanks, "+ yourname + "! "  "Nice to meet you! ")
#Unpacking values from a tuple into variables
#Using a tuple will allow for subdata to be inputted as support for primary data.
person_info = ("Marissa", 24, "Manager")
name, age, profession = person_info 
print(f"Name: {name}, Age: {age}, Profession: {profession}")
#Extracting values from a list into variables 
#Extracting data in a list increases code clarity and avoids data repitition to keep process time low
grades = [99, 96]
Networking, programmingI = grades
print(f"Networking: {Networking}, ProgrammingI: {programmingI}")
#Assigning values using sequence assignment
#Will help with code clarity by allowing for short and concise code
first_name, last_name = "Marissa", "Bommarito" 
print(f"First Name: {first_name}, Last Name: {last_name}")
#Extending sequence assignment to unpack multiple values
#This structure allows for the ability to take a group of strings and to assign each of them unique variability 
first, *rest = 1, 2, 3, 4, 5
print(f"First: {first}, Rest: {rest}")