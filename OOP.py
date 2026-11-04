
# In OOP, we think about the world in terms of Objects where Objects might store information/data inside of them, and also support the ability to perform types of operations, some sort of actions, or method, or functions that can operate on those Objects 

# Python has number of built in types. It has types for lists, sets and so on

# Creating a new type in python
class Point():

    # We will create other Points, points to store x and y values
    
        # Think when we create a point so what should happen
        def __init__(self, input1, input2): 
        # Creating Method or Function, 2 times underscore (_) and init, that is going to automatically be called every time and this function takes couple of arguments
        # All functions/Methods operates on Objects themselves, 
        # "self" is a "first Argument" which represents the "Object" in "question"
        # If there ar two points, so each have both different x and y values/coordinates and we want these values will able to store separatly inside the Object and the "self" variable referencing the "Object" and this self vriable might change depending on which point we want to interacting with at any given time 
        # Now, What other inputs does a Point() need?, well x and y, so add x and y Object also in __init__()     
        # "self" Object representing the point itself

        # Storing data to Object "self (which is representing Point())" 
            self.x = input1
            self.y = input2
            # we store argument x and y to object self properties (.x and .y) = input1 and input2 whatever values inside it as an argument happen to be 

# Creating another/new Point()
p = Point(2, 4) 
# And then the "self" argument is going to provided automatically so do not need to mention self again as it is mentioned above in the __init__(). But need to provide input 1 and 2 (x and y) 
