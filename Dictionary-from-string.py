# Ex. 24 Write a Python program to create a dictionary from a string
example = 'w3resource'
dic1 = {}
# Access each character individually
for l in example:
  if l in dic1:
    dic1[l] += 1
  else:
    dic1[l] = 1

print(dic1)
