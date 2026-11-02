# This Second method is to import entire fucntions module (functions.py) and then use dot (.) notation to access the square function as mentioned in the code below 

import functions

for i in range(10):
    print(f"Square of {i} is {functions.square(i)}")
