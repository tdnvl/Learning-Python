import random
# List of 62 characters to pull from to generate a password
# character_list = ["a","b","c","d","-","=","!","@","#","$","%","&"]
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

# print("Reading from: " + characters.name)
# line = characters.read()
# chain = []
# chain.append(line[0])
# chain.append(line[2])
# print("".join(chain))

