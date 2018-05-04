numbers = int(input("How many Fibonacci numbers do you want to see?\n>> "))

def fibo(numbers):
    series=[1,1] # I might as well start my series with the first two elements.
    if numbers == 1:
        print("1")
    elif numbers == 2:
        print("1,1")
    elif numbers > 2:
        while len(series) < numbers:
            sum = series[-2] + series[-1]
            series.append(sum)
        print(series)

fibo(numbers)

