# Inside list, each element is a dictionary, a mapping of keys and values 
# Python has the ability to nest the data structures within one another. We can have lists inside of other lists, or lists inside of dictionaries

# L1 *****
# In this case, we have dictionaries inside of a list.
people =[
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slythrerin"}
]
# ******** 

# L4 *****
# function that takes kyes as input and return kyes and values from inside of the dictionary
# Here We are giving the name keys so the people.sort() can sort according to the name 
def f(person):
    return person["name"]
# ********

# L2 *****
# Sorting the list
people.sort(key=f)
# ********

# L3 *****
# printing the sorted list
print(people)

# Exeption error will occure becouse sort() function cannot compare as it does't know the smallest and the largest value so we are creating the function above to solve this problem 
# ********