while True:
    choice1 = str(raw_input("Player one, what's your move?\nType R for Rock, P for Paper, and S for Scissors\n>> "))
    if choice1.lower() not in ('r', 'p', 's'):
        print ("Not a valid choice.")
    else:
        break
while True:
    choice2 = str(raw_input("Player two, what's your move?\nType R for Rock, P for Paper, and S for Scissors\n>> "))
    if choice2.lower() not in ('r', 'p', 's'):
        print ("Not a valid choice.")
    else:
        break

# I'm trying to have the name of the player in an array. That might or might not be useful, but I'm trying.
p1 = ["Player 1",choice1.lower()]
p2 = ["Player 2", choice2.lower()]

# first case: Same choice!
if p1[1] == p2[1]:
    print ("Draw! Play again.")
elif p1[1] == 'r' and p2[1] == 's':
    print (p1[0] + " wins! Rock beats scissors.")
elif p1[1] == 'r' and p2[1] == 'p':
    print (p2[0] + " wins! Paper beats rock.")
elif p1[1] == 'p' and p2[1] == 's':
    print (p2[0] + " wins! Scissors beats paper.")
elif p1[1] == 'p' and p2[1] == 's':
    print (p2[0] + " wins! Scissors beats paper.")


