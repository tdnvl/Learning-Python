# Ask for a phrase to revert
phrase = str(input("Type a phrase to revert:\n>> "))

# Split phrase into words
def split_phrase(phrase):
    words = phrase.split()
    print(words)

words = split_phrase(phrase)
print(words)

# Revert the sequence of words
inverted_phrase = []

for i in range(3):
    inverted_phrase.append(words[:-i])

print(inverted_phrase)
