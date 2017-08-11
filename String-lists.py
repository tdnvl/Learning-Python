word = str(raw_input ("Type a word... "))
print(word)
length = int(len(word))
lengt = length - 1
print(lengt)
int(lengt)

if length % 2 == 0:
    midpoint = length / 2
else:
    midpoint = (length / 2) +1


for l in range(1,midpoint):
    # the end of the range should be the rounded-up length / 2 so it stops when it reaches the middle letter
    test = 0
    if word[l] == word[lengt-l]:
        test = test + 1
    else:
        print("Not a palyndrome")
    if test == midpoint:
        print("This is a palyndrome")
    else:
        break

