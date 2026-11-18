
# Decorators are going to be a function that takes a function of input and returns a modified version of that function as output
# In other Programming languages they can not be passed in as input or output to other functions 

# let's create a function() that modifies another function() by announcing that the function is about to run, and that the function() has completed run
# This announce() function will take function f() as input and will return a new function, and wrape up function f() with having some additional behavior (modification), often called a wrapper function

def announce(f):
    def wrapper():
        print("About to run the function")

        # let's actually run the function
        f()
        # Then print "Done with the function"
        print("Done with the function")
    return wrapper

@announce   # It will add announce decorator to this function
def hello():
    print("Hello World")

# Now run the function hello()
hello()

# The announce(f) Decorator is taking the function f(), and then it's creating a new function that just announcing via print("") statment  

# Rea Life Usage:
# the decorators can be used to make sure user loged in status on web
# the decorators is very usefull for web application framework like Django (Python's framework)