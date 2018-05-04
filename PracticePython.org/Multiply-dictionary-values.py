# Ex 11 at https://www.w3resource.com/python-exercises/dictionary
# Write a Python program to multiply all the items in a dictionary
dic1 = {1: 12, 2: 45, 3: -12, 9: 22, 102: 11}
dic_product = 1
for i in dic1.values():
    dic_product = dic_product * i
print(dic_product)
