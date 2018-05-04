# Exercise 3 at https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/lists/exercises_list_and_dictionaries.html
groceries = ["banana", "orange", "apple"]
stock = {}
prices = {}
stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3
def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            total = total + prices[i]
            stock[i] = stock[i] - 1
    print("The total is: " + str(total))
    print(stock)

compute_bill(groceries)
