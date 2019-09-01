import random

# Steps of program
#
# welcome player
# give instructions of game
# set random number
# set guesses to 1
#     while players guesses does not equal ranom number:
#         if the guess is greater:
#             print guess lower
#         else //if the guess isnt equal or higher at this point, it can only be lower
#             print guess higher
#         get new guess from player
#         increase guesses by 1
# congratulate player on passing
# tell player how many guesses it took
#
# later : added a limited number of guesses for the player

print("""
    ########### Number Guessing ###############

    instructions: there is a number, you will be allowed to guess it,
    see how long it takes to find the right number, but...



    you only have 7 guesses
""")

number = random.randint(1, 100)
guess = int(raw_input("guess the number: "))
attempts = 0
while (guess != number):
    if attempts == 7:
        print("well that proves it, you don't know your algo's mate!!!!")
        break;
    elif guess > number:
        print("you're too high")
    elif guess < number:
        print("you're too low")
    elif guess == number:
        print("well done! that took you " + str(attempts) + " attempts")
        break;
    guess = int(raw_input("guess the number again: "))
    attempts += 1
