from random import randint

#Define variables
players = input("How many players: ")
numLista=[0]* 5
playerNum = 0
scores = []
for player in range(players):
    scores.append([0] * 75)
# One-Six=0-5; pair=6, TP=7, Toak=8, Foak=9, ss=10, bs=11, fh= 12, chans=13, yatzy= 14
locations = ["ones", "twos", "threes", "fours", "fives", "sixes", "pair", "two pair", "three of a kind", "four of a kind", "small straight", "big straight", "full house", "chance", "yatzy"]

#Rethrow function
def rethrow():
    dieSelection = raw_input("Which die would you like to throw again: ").split()
    for i in dieSelection:
        numLista[int(i) - 1] = randint(1, 6)


    print numLista

#Main game loop
while True:
    print "Player {}:s turn!".format(playerNum + 1)

    #Generate die
    for i in range(0,5):
        numLista[i] = randint(1,6)
    print numLista

    #Give player two rethrows, if they want them
    for x in range(0,2):
        if raw_input("Would you like to rethrow (y/n): ") == ("y"):
            rethrow()
        else: break

    #Save your score, break loop when correctly saved
    while True:

        #Exception handling of input
        while True:
            try:
                index = locations.index(raw_input("Where would you like to save your die: ")) * 5
                break

            except ValueError:
                print ("That's not a valid spot")

        #test if spot is empty in scoretable
        if scores[playerNum][index] == 0:
            for i in range(0,5):
                scores[playerNum][i + index] = numLista[i]
            break
        else:
            print ("You've already saved something there!")

    #Print scoretable for the current player
    print ("player {}:s score").format(playerNum + 1)
    for i in range(0,15):
        print "{}:\t{}".format(locations[i], scores[playerNum][i*5:i*5+5])
    print "\n\n"

    #Next player
    playerNum = (playerNum + 1) % players
