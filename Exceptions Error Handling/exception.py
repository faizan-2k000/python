

                # **** Exception Error Understanding ****

# We will learn how to handle Exception messy errors gracefully so the program remained running and do not crash
 

x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")

# Run the program and type value of x = 5 and value of y, the program will run succesfully as shown below:

# IT@DESKTOP-MR9OLKB MINGW64 /d/pyyy/python (main)
# $ python exception.py 
# x: 5
# y: 10
# 5 / 10 = 0.5

# Now try value of x = 5 and value of 0 = 10, the Exception error will appear as shown below:

# IT@DESKTOP-MR9OLKB MINGW64 /d/pyyy/python (main)
# $ python exception.py 
# x: 5
# y: 0
# Traceback (most recent call last):
#   File "D:\pyyy\python\exception.py", line 4, in <module>
#     result = x / y
#              ~~^~~
# ZeroDivisionError: division by zero
