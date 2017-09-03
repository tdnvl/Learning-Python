# Split phrase, reverse, and concatenate
def reverse_phrase(phrase):
    split_phrase = phrase.split()
    split_phrase.reverse()
    reversed_phrase = " ".join(split_phrase)
    print("The inverted phrase is: " + reversed_phrase)

# Ask for a phrase to revert
user_phrase = str(input("Type a phrase to revert:\n>> "))

reverse_phrase(user_phrase)
