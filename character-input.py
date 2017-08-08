import datetime
name = raw_input("What is your name? \n")
age = raw_input("What is your age? \n")
now = datetime.datetime.now()
year = now.year + (100 - int(age))
print(name + ", you will turn 100 in " + str(year))
