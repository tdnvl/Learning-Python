number = input("Give me a number... ")

my_list = range(1, number + 1)

divisors = []

for i in my_list:
    if number % i == 0:
        divisors.append(i)
    else:
        continue

print ("The list of divisors is " + str(divisors))
