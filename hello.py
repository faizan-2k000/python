print("Hello, world!")



name = input ("Name: ")
print("Hi, " + name)    
# + sign is used to concatenate
#  In python, the + operator can be used to add numbers or concatenate strings and lists.
# ************************

# Formatting Strings
print(f"Hello, {input("Name: ")}")
# Formated String:
    # we simply add an f before the quotation marks.

# num = input("number: ")
# if num > 0:
#     print("is greater then 0")

num = int(input("Number: "))
if num > 0:                    # Conditional statement ends with the colon (:)
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")