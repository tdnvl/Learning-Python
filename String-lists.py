word = str(raw_input("Type a word... "))
length = int(len(word))
# print("The length of this word is " + str(length))
test = 0


# Let's define the index of the midpoint (for the symmetry) in word
if length % 2 == 0:
    midpoint = length / 2
    # print ("The midpoint is " + str(midpoint) + "\n")
else:
    midpoint = (length / 2) + 1
    # print ("The midpoint is " + str(midpoint) + "\n")

# Two checks to see if my indexing was correct
# print("First is " + word[0])
# print("Last is " + word[last-1])

# Let's compare the first and the last characters, and move towards the midpoint
for l in range(0,midpoint):
    if word[l] == word[length-1-l]:
        test = test + 1

# If the test was positive for all letters from the first to the midpoint, then it is a palyndrome
if test == midpoint:
    print("This is a palindrome.")

# Even if a word is not a palyndrome, the middle letter will match against itself and test will be, at a minimum, 1.
if test == 1:
    print ("This is not a palindrome.")
