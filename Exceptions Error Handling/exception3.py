
#                       **** Exception Error Handeling ****

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))

# ValueError expression, if input is text instead of integer 
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

result = x / y  

print(f"{x} / {y} = {result}")

# Error if type text into an int type variable: 
# $ python exception3.py
# x: hello
# Traceback (most recent call last):
#   File "D:\pyyy\python\Exceptions Error Handling\exception3.py", line 6, in <module>
#     x = int(input("x: "))
# ValueError: invalid literal for int() with base 10: 'hello'


# This error line 
#        ValueError: invalid literal for int() with base 10: 'hello'
# says:
#        You can't take text that is not a number and turn it into an integer
