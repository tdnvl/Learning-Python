# Ask for a phrase to revert
user_phrase = str(input("Type a phrase to revert:\n>> "))

# Split phrase into words
def split_phrase(phrase):
    return phrase.split()

# Split the phrase typed by the user
all_the_words = split_phrase(user_phrase)
# Reverse the phrase
all_the_words.reverse()
# And now conctenate
inverter_user_phrase = " ".join(all_the_words)

print("The inverted phrase is: " + inverter_user_phrase)
