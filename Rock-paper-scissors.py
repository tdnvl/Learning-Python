while True:
    player1 = str(raw_input("Player one, what's your move?\nType R for Rock, P for Paper, and S for Scissors\n>> "))
    if player1.lower() not in ('r', 'p', 's'):
        print ("Not a valid choice.")
    else:
        break
while True:
    player2 = str(raw_input("Player two, what's your move?\nType R for Rock, P for Paper, and S for Scissors\n>> "))
    if player1.lower() not in ('r', 'p', 's'):
        print ("Not a valid choice.")
    else:
        break
