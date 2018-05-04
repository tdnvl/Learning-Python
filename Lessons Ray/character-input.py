import datetime
name = raw_input("What is your name? \n")
age = raw_input("What is your age? \n")
times = int(raw_input("How many times do you want to print this message? \n"))
now = datetime.datetime.now()
year = now.year + (100 - int(age))
print(times * (name + ", you will turn 100 in " + str(year) + "\n"))
