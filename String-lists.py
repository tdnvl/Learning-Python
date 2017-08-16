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
for l in range(0,midpoint):
    if word[l] == word[last-1-l]:
        test = test + 1

if test == midpoint:
    print("This is a palyndrome")

if test == 1:
    print ("This is not a palyndrome")
