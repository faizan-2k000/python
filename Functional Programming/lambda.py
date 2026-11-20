
# L1 *****
people =[
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slythrerin"}
]
# ******** 

# L2 *****
# Sorting the list
people.sort(key=lambda person: person["name"])
# Here people (a list define above) is handing over all of the keys (name and house)from dictionaries to the lambda function where person is taking it as input. Then person is now become list (people[] is now person[]) and it is returning the sorted list by name keys.
# So the after the lambda, person is an an argument(taking input) and person["name"] is the return value  
# ********

# L3 *****
# printing the sorted list
print(people)

# Exeption error will occure becouse sort() function cannot compare as it does't know the smallest and the largest value  
# ********