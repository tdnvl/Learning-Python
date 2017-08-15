word = str(raw_input("Type a word... "))
length = int(len(word))
print("The length of this word is " + str(length))
# length = length + 1
test = 0


# Let's define the index of the midpoint in word
if length % 2 == 0:
    midpoint = length / 2
    print ("The midpoint is " + str(midpoint) + "\n")
else:
    midpoint = (length / 2) + 1
    print ("The midpoint is " + str(midpoint) + "\n")

last = length
print("First is " + word[0])
print("Last is " + word[last-1])

# Let's compare the first and the last characters, and move towards the midpoint
for l in range(0,midpoint-1):
    while test != midpoint:
        if word[last-1-l] == word[l]:
            test = test + 1
            print(test)
        else:
            print("Not a palyndrome")

if test == midpoint:
    print("This is a palyndrome")
else:
    print ("This is not a palyndrome")

