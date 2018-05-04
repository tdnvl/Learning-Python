# Exercise 6 at https://www.w3resource.com/python-exercises/dictionary/
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
n = int(input("Enter an integer...\n>>> "))
i = 1
A = {}
while i <= n:
    A[i] = i*i
    i = i + 1
print(A)
