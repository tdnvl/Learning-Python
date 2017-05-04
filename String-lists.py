word = raw_input ("Type a word... ")
length = len(word)
lengt = length - 1
print(lengt)
## int(lengt)
for l in word:
    if word[0:1] == word[l:lengt]:
        print("First and last letters are the same")
    else:
        print("First and last letters are different")
