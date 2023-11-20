import json

#Function to validate Employee ID 
def validate_employee_id(employee_id): 
    return employee_id.isdigit() and len(employee_id) <= 7
#Function to validate Employee Name 
def validate_employee_name(name):
    return all(c.isalpha() or c in " -'" for c in name)
#Function to validate Employee Email 
def validate_employee_email(email) :
    return all(c.isalnum() or c in ".@" and c not in '!\"#$%^&*()=+,<>/?;:[]{}\\' for c in email)
#Function to validate Employee Address 
def validate_employee_address(address) :
    return all(c.isalnum() or c in " -" and c not in '!\"@$%^&*_=+<>?;:[ ]{}' for c in address)
#Function to validate Employee Salary 
def validate_employee_salary(salary) :
    return 18 <= salary <= 27
#Function to gather employee information
def gather_employee_info(): 
    employee = {}

    employee_id = input("Enter employee ID: ")
    while not validate_employee_id(employee_id):
        employee_id = input("Enter a valid Employee ID (7 or fewer digits): ")
    employee['Employee ID'] = int(employee_id)

    employee_name = input("Enter employee name: ")
    while not validate_employee_name(employee_name):
        employee_name = input("Enter a valid Employee Name: ")
    employee['Employee name'] = employee_name + " - IT Department"

    employee_email = input("Enter employee email: ")
    while not validate_employee_email(employee_email):
        employee_name = input("Enter a valid Employee Email: ")
    employee['Employee name'] = employee_email

    employee_address = input("Enter employee address (optional): ")
    if employee_address: 
        while not validate_employee_address(employee_address):
            employee_address = input("Enter a valid Employee Address: ")
        employee['Employee Address'] = employee_address

    employee_salary = float(input("Enter employee salary (between 18 and 27): "))
    while not validate_employee_salary(employee_salary):
        employee_salary = float(input("Enter a valid salary (between 18 and 27): "))
    employee['Employee Salary'] = employee_salary * 1.3 #30% increase

    return employee

#Function to write employee data to JSON file 
def write_to_json(data):
    with open('employee_data.json', 'w') as file:
        json.dump(data, file, indent=4)

#Main function to execute the purpose 
def main():
    employee_list = []

    while True:
        employee = gather_employee_info()
        employee_list.append(employee)

        add_more = input("Do you want to enter more employees? (yes/no): ")
        if add_more.lower() != 'yes':
            break

    print("List of Updated Employee Information: ")
    print(employee_list)

    write_to_json(employee_list)

#Execute the program 
if __name__== "__main__":
    main()