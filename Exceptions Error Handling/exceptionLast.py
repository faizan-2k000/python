
#                       **** Exception Error Handeling ****

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
 
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x / y  
except ZeroDivisionError:
    print("Error: Can't divide by 0.")
    sys.exit(1)
print(f"{x} / {y} = {result}")

# In Web application, if something goes wrong, we want to handle the error nicely by displaying a nice error message to the user, by telling what was wrong instead of having the program entirely crash      

# Are called query strings
# field1=value1&field2=value2&field3=value3...

# for example:
# https://www.google.com/search?q=harvard&sxsrf=AKL5yDj4-4t35eKCe0AdnR_KSK_78_gy-Q%3A1795501830306&atvm=2

# where an = separates the name of the parameter from its value, and the & symbol separates parameters from one another. 

# its the way form submits information to web server, by encoding the form data in the URL.

q=Harvard
q is the name, short for “query” and Harward is the value, pair of both are called