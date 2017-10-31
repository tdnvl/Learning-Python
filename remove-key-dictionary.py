# Ex 12 at https://www.w3resource.com/python-exercises/dictionary
# Write a Python program to remove a key from a dictionary.
dic1 = {1: 123, 2: "adf", 3: "hello", 4: (1,2,3), 5: "bob", 6: 987, 7: 765, 8: 653, 9: 234}
print(dic1)
clef = int(input("Enter the key you want to remove... \n >> "))
del dic1[clef]
if clef in dic1.keys():
    print("You removed key # " + str(clef) + " from your dictionary.")
    print(dic1)
else:
    print("The key is not in the dictionary.")


