# Exercise 2 at https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/lists/exercises_list_and_dictionaries.html
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
inventory = {"banana": 10, "apple": 8, "orange": 3, "pear": 5}
for i in prices:
    print(i)
    print("price: ", prices[i])
    print("inventory: ", inventory[i])
    print("__________\n")

total = 0
for i in prices:
    print(prices[i]*inventory[i])
    total = total + (prices[i]*inventory[i])
print("The total is " + str(total))
