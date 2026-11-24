
#                       **** Exception Error Handeling ****

import sys

x = int(input("x: "))
y = int(input("y: "))

# $$$ try-except Expression: $$$

# Try to do something, like here, try to x / y
try:
    result = x / y

# And then print the custom made Error message if above mentioned try does not work, and then exit the program. 
except ZeroDivisionError:
    print("Error: Can't divide by 0.")
    
    # To exit the program, python has a module called sys. it will exit the program with status code of 1
    sys.exit(1)

print(f"{x} / {y} = {result}")

# Output:
# IT@DESKTOP-MR9OLKB MINGW64 /d/pyyy/python/Exceptions Error Handling (main)
# $ python exception2.py 
# x: 5
# y: 0
# Error: Can't divide by 0.