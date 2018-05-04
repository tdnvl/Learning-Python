# Ex 23. Write a Python program to combine values in python list of dictionaries.
from collections import Counter

dct = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# I can't iterate on dictionaries!
# I want to extract each item in the list and add them to a Counter

C = Counter() # initiate Counter as empty

for l in dct:
    D = Counter()
    item = l['item']
    amount = l['amount']
    D[item] = amount
    C.update(D)
print(C)

# Expected Output: Counter({'item1': 1150, 'item2': 300})
