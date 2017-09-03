import random
# List of 62 characters to pull from to generate a password
character_list = ["a","b","c","d","-","=","!","@","#","$","%","&"]
random.seed(None,2)

n = int(input("How many characters in your password?\n>> "))
password = []
number = 1
while number <= n:
    character_index = random.randint(0,11)
    password.append(character_list[character_index])
    number = number + 1

print("This is your password: " + "".join(password))
