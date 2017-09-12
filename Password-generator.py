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
    print(character_index)
    selector = characters.read()
    new_character = selector[character_index]
    password.append(new_character)
    print(password)
    number = number + 1
characters.close()
print("This is your password: " + "".join(password))

# print("Reading from: " + characters.name)
# line = characters.read()
# chain = []
# chain.append(line[0])
# chain.append(line[2])
# print("".join(chain))

