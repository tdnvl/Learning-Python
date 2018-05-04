# Ex 30 Write a Python program to get the top three items in a shop.
dic1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

# We're going to use the function called sorted
# sorted takes in an iterable and it returns the same iterable
# sorted.
# There is an additional input parameter called key that takes in
# an anonymous function that specifies how you would like the values
# to be ordered
# If you don't specify the key, the Python will automatically figure this out

# First convert the dictionary into a list of tuples
# Creates a list such that each element is a two element tuple where
# the key is the first element and the value is the second element
t = [(k, v) for (k, v) in dic1.items()]

# t is the list we are sorting
# key you specify an anonymous function where the input
# of the function is an element from the input t
# The input t is a list of tuples, so therefore
# if we specify lambda x: ... this means x is a tuple
# from the input t
# Specify x[1] as the value or the price and this guides
# the sorting so that we sort based on the second element of the tuple
# Specify sorting in reverse order
out = sorted(t, key=lambda x: x[1], reverse=True)

# Print off the top 3 items
# Because we have sorted, and specified the order to be reversed
# the top 3 items appear at the beginning
for i in range(3):
    # Get the item
    item = out[i]

    # Access the key and value for the item and print it out
    print(item[0], item[1])
