#Provide data
data = [1121, "Jackie Grainger", 22.22,
        1122, "Jignesh Thrakker", 25.25,
        1127, "Dion Green", 28.75, False,
        24.32, 1132, "Jacob Gerber",
        "Sarah Sanderson", 23.45, 1137, True,
        "Brandon Heck", 1138, 25.84, True,
        1152, "David Toma", 22.65,
        23.75, 1157, "Charles King", False,
        "Jackie Grainger", 1121, 22.22, False,
        22.65, 1152, "David Toma"]
#Initalize lists for dictionaries
employee_data = []
underpaid_salaries = []
company_raises = []
#Process the provided data 
i = 0
while i < len(data):
    employee_id =data[i]
    employee_name =data[i + 1]
    hourly_wage = data[i + 2]
#Calculate total hourly rate (including benefits)
total_hourly_rate = hourly_wage * 1.3 
#Create a dictionary for the employee
employee_dict = {
    "employee ID": employee_id, 
    "employee name": employee_name, 
    "hourly wage": hourly_wage, 
    "total hourly rate": total_hourly_rate
}
#Check if total hourly rate is between 28.15 and 30.65
if 22 <= hourly_wage < 24:
    raise_percent = 5 
elif 24 <= hourly_wage < 26:
    raise_percent = 4
elif 26 <= hourly_wage < 28:
    raise_percent = 3
else:
    raise_percent = 2
#Calculate raise in dollars 
raise_amount = hourly_wage * (raise_percent / 100)
#Create a dictionary for raise information
raise_dict = {
    "employee name": employee_name,
    "raise_amount": raise_amount
}
#Append dictionaries to the respective lists 
employee_data.append(employee_dict)
company_raises.append(raise_dict)
i += 3
#Print the results 
print("employee data:")
for employee_dict in employee_data:
    print(employee_dict)
print("\nunderpaid salaries:")
for underpaid_employee in underpaid_salaries:
    print(underpaid_employee)
print("\ncompany raises:")
for raise_info in company_raises:
    print(raise_info)
      
