
# When the conditional statement appears like if, elif, else or other conditional statement, then the boolean expressional (True/False)/action code will be intended in the next line of conditional statement type of code. Also the code inside the functions will be intended.

# In Python, indentation is not just for readability, but it is also a requirement for the code to run correctly.

# In python, elseif is written a elif
# ***** Programm: Conditions *****
# Topic: ***** Ecxeption Error/Debugging Exception Error *****
# Debugg Method:
# Type error / exception
# When bug appears, start reading from very bottom of the error message and read upwards. The last line of the error message is usually the most important one, as it tells you what type of error occurred and where it occurred in your code.

# Buggy Program:

print("****** Buggy Program: ******")

num = input("number:")
if num > 0:                         # Conditional statement ends with the colon (:)
    print("Number is positive")
elif num < 0:
    print("Number is negetive")
else:
    print("Number is zero")    

# Debugged Program:

print("****** Debugged Program: ******")

num = int(input("Number: "))   # input() is a builtin function to take input from the user 
if num > 0:                    # Conditional statement ends with the colon (:)
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")