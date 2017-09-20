import random
random.seed(None, 2)
characters = open('characters.txt','r')
n = int(input("How many characters in your password?\n>> "))
password = []
number = 1
selector = characters.read()
while number <= n:
    character_index = random.randint(0, 64)
    new_character = selector[character_index]
    password.append(new_character)
    number = number + 1
    del new_character
characters.close()
print("This is your password: " + "".join(password))

