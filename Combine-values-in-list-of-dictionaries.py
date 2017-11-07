# Ex 23. Write a Python program to combine values in python list of dictionaries.
from collections import Counter

items = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
counted_items = Counter(items)
print(counted_items)

for i in items:



A = [1, 2, 3, 3, 4, -1, 0, 2, 2, 2, 3]
C = Counter(A) # Creates a Counter object that counts how many times
               # you have seen each value
print(C)

# Expected Output: Counter({'item1': 1150, 'item2': 300})

E = 'aaabbbccdefadsfsvas'
F = Counter(E)
print(F)
