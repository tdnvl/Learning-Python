# Ex 10 at https://www.w3resource.com/python-exercises/dictionary/
# Write a Python program to sum all the items in a dictionary.
dic1 = {1: 12, 2: 45, 3: -12, 9: 22, 102: 11}
dic_sum = 0
for i in dic1.values():
    dic_sum = dic_sum + i
print(dic_sum)
