number = int(input("Enter a number: "))

divisors = range(2, number + 1)

check = []

for i in divisors:
    if number % i == 0:
        check.append(i)
    else:
        continue
print("This is the list of divisors: " + str(check))

if check != [number]:
    print("This is not a prime number.")
elif check == [number]:
    print("This is a prime number.")
