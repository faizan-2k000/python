
# L1 *****
people =[
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slythrerin"}
]
# ******** 

# L4 *****
# Here We are giving the house keys so the people.sort() can sort according to the house 
def f(person):
    return person["house"]
# ********

# L2 *****
# Sorting the list
people.sort(key=f)
# ********

# L3 *****
# printing the sorted list
print(people)
# ********