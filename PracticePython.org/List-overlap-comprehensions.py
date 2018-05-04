a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# List comprehensions take the form: [EXPRESSION FOR_LOOPS CONDITIONALS]
c = [element for element in a if element not in c and element in b]
# Using a set removes duplicates. It has to be typed as a list, though.
d = list(set(c))
print(d)
