# Ex 17. Write a Python program to remove duplicate values from Dictionary
dic1 = {1: "bob", (1,2): 123, (1,2,3): 456, "joe": 456}

# It is dangerous to modify a dictionary inside of a loop
# Let's construct a new dictionary and add non-duplicate values

# Contains the new dictionary
dic2 = {}

# Maintains a set of the values we have already encountered
values = set([])

# For each key,value pair
for (key,value) in dic1.items():
    # If we have not seen the value before, add this key and value
    # to the new dictionary
    if value not in values:
        dic2[key] = value

        # Make sure we add the value in the set so we can check
        # if it exists for the rest of the loop
        values.add(value)

print(dic1)
print(dic2)
