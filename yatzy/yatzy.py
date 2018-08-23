from random import randint
players = input("How many players: ")
numLista=[0]* 5
playerNum = 1

scores = []
for player in range(players):
    scores.append([0] * 75)

# One-Six=0-5; pair=6, TP=7, Toak=8, Foak=9, ss=10, bs=11, fh= 12, chans=13, yatzy= 14
locations = ["ones", "twos", "threes", "fours", "fives", "sixes", "pair", "two pair", "three of a kind", "four of a kind", "small straight", "big straight", "full house", "chance", "yatzy"]

def rethrow():
    dieSelection = raw_input("Which die would you like to throw again: ").split()
    for i in dieSelection:
        numLista[int(i) - 1] = randint(1, 6)


    print numLista
while True:
    print "Player %i:s turn!" % playerNum
    for i in range(0,5):
        numLista[i] = randint(1,6)
    print numLista
    for x in range(0,2):
        if raw_input("Would you like to rethrow (y/n): ") == ("y"):
            rethrow()
        else: break
    index = locations.index(raw_input("Where would you like to save your die: ")) * 5
    print index
    for i in range(0,5):
        scores[playerNum - 1][i + index] = numLista[i]
    print scores

    playerNum = (playerNum + 1) % players