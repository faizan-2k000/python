
# Create empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
# s.add(5)

print(s)

# if you add another duplicate element like s.add(5), sets will consider it and print it only one

s.remove(2)
print(s)

print(f"Set has {len(s)} number of elements")
