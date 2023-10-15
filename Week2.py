# Step 1: Store your first name as a variable. Use all lowercase letters when you declare it.
first_name = "marissa"
#Step 2: Store your last name as a variable. Use all uppercase letters when you declare it.
last_name = "BOMMARITO"
#Step 3: Print out, "Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.
print(f"Hello, {first_name.upper()} {last_name.lower()}")
#Step 4: Print out two newlines 
print("/n/n")
#Step 5: Create a new variable that stores your first and last name together with a space between both parts.
full_name = f"{first_name} {last_name}" 
#Step 6: Slice your last name from the variable you created in step 5 and prints it out. This must take place on one line. 
print(full_name.split()[-1])
#Step 7: Replace your last name in the variable you created in step 5 with "<your last name>, Walsh College Student"; print out the new value of this variable
full_name = full_name.replace(last_name, "Bommarito>, Walsh College Student") 
print(full_name)
#Step 8: Print out the following: "Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi"
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')
#Step 9: Store 2 decimal numbers as variables.
num1 = 10.5 
num2 = 3.5 
#Step 10: Store one addition, one subtraction, one multiplication, and one division operation of these variables as variables.
add_result = num1 + num2
sub_result = num1 - num2 
mul_result = num1 * num2 
div_result = num1 / num2 
#Step 11: Print out each of the four results as:
print(f"{num1} plus {num2} equals {add_result}")
print("{} minus {} equals {}" .format(num1,num2,sub_result))
print("%s times %s equals %.2f" % (num1, num2, mul_result))
print(num1, "divided by" , num2, "equals", div_result)
#Step 12: Create a new variable called sq_root that stores the square root of the variable that holds the result of the multiplication operation you performed in step 10 to two decimal places. Print out this value as:
import math 
sq_root = round(math.sqrt(mul_result), 2)
print(f"The square root of {mul_result} equals {sq_root}")
#Step 13: Store the current month as a string variable (e.g. March, June, etc.) and day of the month as a numeric variable.
current_month = "October" 
day_of_month = 16 
#Step 14: Output "Today is day <day of month> of the month of <month variable>."
print(f"\tToday is day {day_of_month} of the month of {current_month}.")