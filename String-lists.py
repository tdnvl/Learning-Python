word = str(raw_input ("Type a word... "))
print(word)
length = int(len(word))
lengt = length - 1
print(lengt)
int(lengt)
for l in range(0,lengt):
    # the end of the range should be the rounded-up length / 2 so it stops when it reaches the middle letter
    test = 0
    if word[l] == word[lengt-l]:
        test = test + 1
    else:
        print("Not a palyndrome")
    if test == length:
        print("This is a palyndrome")
    else:
        break

