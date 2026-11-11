
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

        # if seats are not available
        if not self.open_seats(): # The pythonic way to say if self.open_seats() == 0:
            return False

        # How we can acces the empty list mentioned above 
        self.passengers.append(name) # it is an attribute, a list that was initially starts out as an empyt list mentioned above 
        return True # If seats available
    
    # Our self.add_passenger function should not let add if the capacity is already full
    # This function will going to return number of open seats that are on the plane
    def open_seats(self):
        # Other then "self" there are no any inputs that we need to calculate about the seats
        # The other information we need to know is the "capacity minus how many passengers are there" and we are putting passengers information in len() function to find the number of passengers
        return self.capacity - len(self.passengers)




# So now If we want to create a flight having the class Flight with the capacity of 3 people. Means only 3 people can go in this flight 
flight = Flight(3)  # "3" is the "capacity" (an argument) specified inside the __init__ function mentioned above

# We have 3 functions,
#     __init__() that creates a new flight
#     add_passenger() that adds the new passenger in that flight
#     an open_seats() for total number of seats available

# lets use those function to actually add some passengers to this flight 
people = ["Harry", "Bob", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for that {person}")



