word = str(input("Type a word... "))
length = int(len(word))
print(length)
length = length + 1
test = 0


# Let's define the index of the midpoint in word
if length % 2 == 0:
    midpoint = length / 2
    print ("The midpoint is " + str(midpoint) + "\n")
else:
    midpoint = (length / 2) + 1
    print ("The midpoint is " + str(midpoint) + "\n")


# Let's compare the first and the last characters, and move towards the midpoint
for l in range(1,midpoint):
 last = length - l
 print(word[last])
 if word[l] == word[last]:
    test = test + 1
    print(test)
 else:
        print("Not a palyndrome")

if test == midpoint:
    print("This is a palyndrome")
else:
    print ("This is not a palyndrome")

