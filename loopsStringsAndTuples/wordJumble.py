# word jumble game

import random

WORDS = ("meretricious", "dog", "antinomous", "diagnostic", "epoch")
ran_word = random.choice(WORDS)
correct_word = ran_word
jumble = ""

while ran_word:
    position = random.randrange(len(ran_word))
    jumble += ran_word[position]
    ran_word = ran_word[:position] + ran_word[(position + 1):]

print("""

    the jubled word is:

    """ + jumble)

guess = raw_input("what do you think the word is?\n")
askedForHelp = False
nohelp = 5
while guess != correct_word:
    print("guess again")
    hint = raw_input("do you want a hint?")
    if hint.lower() == "yes":
        askedForHelp = True
        print("first 3 letters are: " + correct_word[0:3])
    guess = raw_input("your guess: ")

if guess == correct_word:
    score = 0
    if askedForHelp:
        score -= 3
    score += 5
    print("well done, score is: " + str(score))
