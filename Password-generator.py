import random
random.seed(None, 2)
characters = open('characters.txt','r')
n = int(input("How many characters in your password?\n>> "))
password = []
number = 1
while number <= n:
    character_index = random.randint(0, 64)
    print("Character index: " + str(character_index))
    selector = characters.read()
    new_character = selector[character_index]
    print("New character: " + str(new_character))
    password.append(new_character)
    print("Password: " + str(password))
    number = number + 1
    print("Number: " + str(number))
    del new_character
characters.close()
print("This is your password: " + "".join(password))

