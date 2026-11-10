
class Flight():
    def __init__(self, capacity):
        # This time the "__init__ method" is going to take a single argument "capacity" other than the "self"
        
        # Every flight needs some sort of capacity to know how many people can fit on the plane. It will store in a value:
        self.capacity = capacity

        # And what other information do we need to store about a Flight, the flight have passengers
        #  list can be used in order to store sequence of values
        self.passengers = []  # Empty list created


    # let's think about what methods/functions we might care about performing when it comes to a flight 
    # creating new method/function a Method that is going to work on an individual Object. The name of the method/function can be anything of your choice
    # We also need to reference the Object itself so "self" keyword used here again
    # The passenger will be add by their name 
    def add_passenger(self, name):
        # How we can acces the empty list mentioned above 
        self.passengers.append(name) # it is an attribute, a list that was initially starts out as an empyt list mentioned above 

        # Our self.add_passenger function should let add if the capacity is already full

# So now If we want to create a flight having the class Flight with the capacity of 3 people. Means only 3 people can go in this flight 
        flight = Flight(3)  # "3" is the "capacity" (an argument) specified inside the __init__ function mentioned above
