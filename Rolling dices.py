from random import *
total = 0
counter = 0
diceList = []
diceNumber = 1


while True:
    userInput = raw_input("Would you like to roll a dice? YES/NO ")
    if userInput == "YES":
        break
    elif not userInput == "NO":
        print("Only YES/NO answers")

while True:
    diceCount = int(raw_input("How many dices? "))
    break
for x in range(diceCount):
    diceSize = int(raw_input("What size of dice " + str(diceNumber) + " number? "))
    diceList.append(diceSize)
    diceNumber = diceNumber + 1


while True:
    for y in diceList:
        number = randint(1, y)
        print"You rolled: ", number
        total = total + number
        counter = counter + 1
    userInput2 = raw_input("Would you like to roll again? ")
    if userInput2 == "NO":
        print "Total dice numbers equals: ", total
        print "You rolled dices", counter, "times"
        exit()





