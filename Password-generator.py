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
characters = open('characters.txt','rb+')
print("Reading from: " + characters.name)
line = characters.read()
chain = []
chain.append(line[0])
chain.append(line[1])
chain.append(line[25])
print(chain)

