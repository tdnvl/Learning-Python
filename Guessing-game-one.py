import random
a = random.randint(1, 9)
game = True
i = 0
while game == True:
    guess = int(raw_input("Guess a number between 1 an 9...\n>> "))
    i = i + 1
    if guess == a:
        print ("Yay! You guessed it in " + str(i) + " guess(es)!")
        game = False
    elif guess > a:
        print ("Too big.")
    elif guess < a:
        print ("Too small.")

