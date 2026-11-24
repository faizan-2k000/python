
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