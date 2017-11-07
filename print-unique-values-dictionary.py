# Ex 20. Write a Python program to print all unique values in a dictionary.

dct = {"IV":"S001", "XI": "S002", "VI": "S001", "VII": "S005", "VIII":"S005", "V":"S009","X":"S007"}
# Initialize an empty set. Curly braces are reserved for empty dictionary!
unique_values = set()
for i in dct:
  unique_values.add(dct[i])

#for i in dct.values():
#  unique_values.add(i)
print(unique_values)
