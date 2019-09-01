# craps roller
# code on www.courseptr.com/downloads

import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("you rolles a ", die1, " and a ", die2, " for a total of ", total)


## basic if
word = raw_input("guess the word: ")

if word == "word":
    print("well done")
else:
    print("you're a fool")

raw_input("press enter to exit")
