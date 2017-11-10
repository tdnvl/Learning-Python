# Ex 23. Write a Python program to combine values in python list of dictionaries.
from collections import Counter

dct = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


D = Counter()
E = Counter() # Do I need three counters to do this?

# I can't iterate on dictionaries!
# I want to extract each item in the list and add them to a Counter

for i in range(0,len(dct),1):
    C = Counter() # initiate Counter as empty
    C = Counter(dct[i]) # create counter from each dictionary in the list
    E = C + D # add Counter C to Counter D
    D = E # Before looping,

print(E)





# Expected Output: Counter({'item1': 1150, 'item2': 300})
