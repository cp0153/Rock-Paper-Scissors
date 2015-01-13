import time
import random

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

Possible_Choices = enum('ROCK', 'PAPER', 'SCISSORS')

def user_wants_to_continue():
    "asks the user if they want to continue"
    while True:
        answer = raw_input('Do you wish to continue? (y/n):')[0].lower()
        if answer == "n":
            return False
        if answer == "y":
            return True
    
def player_choice():
    "This function asks the user to pick rock paper or scissors"
    while True:
        choice = raw_input('Please enter your choice (p)aper, (r)ock, or (s)cissors: ')[0].lower()
        if choice == "p":
            return Possible_Choices.PAPER
        elif choice == "r":
            return Possible_Choices.ROCK
        elif choice == "s":
            return Possible_Choices.SCISSORS

        print "invalid\n Please enter your choice (p)aper, (r)ock, or (s)cissors:"

while True:
    print "Player-1, its your turn!"
    player_1_turn = player_choice()
    print "Player 1 picked", Possible_Choices.reverse_mapping[player_1_turn].lower(), "\n"

    print "Player-2, it's your turn!"
    player_2_turn = random.randint(0, 2)
    time.sleep(2)
    print "Player 2 picked", Possible_Choices.reverse_mapping[player_2_turn].lower(), "\n"

    winner = (player_1_turn, player_2_turn)
    
    result = { winner == (0, 0) or winner == (1, 1) or winner == (2, 2): 'Draw! Nobody wins',
               winner == (0, 2) or winner == (1, 0) or winner == (2, 1): 'You win',
               winner == (0, 1) or winner == (1, 2) or winner == (2, 0): 'You lose, player 2 wins'}[1]
    print result

    if user_wants_to_continue() == False:
        break
