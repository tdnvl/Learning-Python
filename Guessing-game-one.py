import random
a = random.randint(1, 9)
game = True
i = 0
while game == True:
    guess = raw_input("Guess a number between 1 an 9...\n>> ")
    i = i + 1

    # First check for exit, while it's a string, to break

    if guess == "exit":
        break

    # Once the exit has been checked, the other conditional tests will be with integers. Let's force the type for the rest of the script.

    guess = int(guess)

    if guess == a:
        print ("Yay! You guessed it in " + str(i) + " guess(es)!")
        game = False
    elif guess > a:
        print ("Too big.")
    elif guess < a:
        print ("Too small.")

