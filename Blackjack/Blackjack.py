from itertools import repeat
import random

stdDeck = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "J", "Q", "K", "A"]
playDeck = []
playerHand = []
cpuHand = []
n = 4
playerScore = 0
cpuScore = 0
Busted = False

for x in range(0, 13):
    playDeck.extend(repeat(stdDeck[x], n))  # fill blackjack deck with 51 cards (4 decks)

draw = random.choice(playDeck)  # draw random card from deck for player
playDeck.remove(draw)  # remove that card from playDeck
draw2 = random.choice(playDeck)  # draw random card from deck for cpu
playDeck.remove(draw2)  # remove that card from playDeck

playerHand.append(draw)  # add card to players hand
cpuHand.append(draw2)   # add card to cpu hand


# checking score for player cards
def values(draw):

    global playerScore

    if draw == "c2":
        playerScore += 2
    if draw == "c3":
        playerScore += 3
    if draw == "c4":
        playerScore += 4
    if draw == "c5":
        playerScore += 5
    if draw == "c6":
        playerScore += 6
    if draw == "c7":
        playerScore += 7
    if draw == "c8":
        playerScore += 8
    if draw == "c9":
        playerScore += 9
    if draw == "c10" or draw == "J" or draw == "Q" or draw == "K":
        playerScore += 10
    if draw == "A":
        askPlayer = raw_input("You drawn Ace: 1 or 11 ?")
        if askPlayer == "1":
            playerScore += 1
        else:
            playerScore += 11
    return playerScore


# checking score for cpu cards
def values2(draw2):

    global cpuScore

    if draw2 == "c2":
        cpuScore += 2
    if draw2 == "c3":
        cpuScore += 3
    if draw2 == "c4":
        cpuScore += 4
    if draw2 == "c5":
        cpuScore += 5
    if draw2 == "c6":
        cpuScore += 6
    if draw2 == "c7":
        cpuScore += 7
    if draw2 == "c8":
        cpuScore += 8
    if draw2 == "c9":
        cpuScore += 9
    if draw2 == "c10" or draw2 == "J" or draw2 == "Q" or draw2 == "K":
        cpuScore += 10
    if draw2 == "A":
        if cpuScore < 12:
            cpuScore += 10
        else:
            cpuScore += 1
    return cpuScore


values(draw)
values2(draw2)

print "CPU has", cpuHand, "Score: ", cpuScore
print "Player has", playerHand, "Score: ", playerScore

# Player operations
while True:
    hit = raw_input("HIT or STAND ? ")
    if hit == "HIT":
        draw = random.choice(playDeck)  # draw random card from deck
        playDeck.remove(draw)  # remove that card from playDeck
        playerHand.append(draw)
        values(draw)
        if playerScore > 21:
            print "Player has", playerHand, "Score: ", playerScore
            print"Player BUSTED"
            Busted = True
            break
        else:
            print "Player has", playerHand, "Score: ", playerScore
    elif hit == "STAND":
        break

# Simpliefied AI for CPU to draw cards untill atleast 16 score
if Busted == False:

    while cpuScore <= 16:
        draw2 = random.choice(playDeck)
        playDeck.remove(draw2)
        cpuHand.append(draw2)
        values2(draw2)
    print "CPU has", cpuHand, "Score: ", cpuScore


if playerScore > cpuScore and Busted == False:
    print "Player wins with ", playerScore
if cpuScore > playerScore  and cpuScore <= 21 or Busted == True:
    print "CPU wins with ", cpuScore
if cpuScore > 21:
    print "CPU BUSTED, Player wins with ", playerScore
if cpuScore == playerScore:
    print "It's a TIE"







