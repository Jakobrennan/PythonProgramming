# fortune cookie with 5 messages
import random
num = random.randrange(5) + 1

if num == 1:
    print("lookout for busses")
elif num == 2:
    print("lovers looking at you")
elif num == 3:
    print("you're lucky, just don't know it yet")
elif num == 4:
    print("chin up chuck")
else:
    print("you're stressed and a bath is needed")

# flipping a coin 100 times and telling you the stats

heads = 0
tails = 0
count = 0
while count < 100:
    tossedCoin = random.randint(1, 2)
    if tossedCoin == 1:
        heads += 1
    else:
        tails += 1
    count += 1
print("heads: " + str(heads) + " - tails: " + str(tails))

# number guessing game but computer guesses

# accept player number that computer needs to guess
# declare variable for computers number
# declare count variable
# while computersGuess isn't equal to humans
#     computersGuess randomly generates
#     + 1 to count variable
# when complete, print number of attempts

player = int(raw_input("pick a number between 1 and 10,000 for computer to guess: "))
computer = 0
attempts = 0
while computer != player:
    computer = random.randint(1, 10000)
    attempts += 1
print("well that took " + str(attempts) + " for the computer")
