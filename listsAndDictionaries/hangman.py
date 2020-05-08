# hangman game

import random

# constants
HANGMAN = (
"""
---------
|       |
|    
|
|
|
|\ 
| \ 
|\ \ 
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|
|
|
|\ 
| \ 
|\ \ 
| \ \  
-----------
""",
"""
---------
|       |
|      ( )
|      -+-
|
|
|\ 
| \ 
|\ \ 
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|     --+-
|    /
|
|\ 
| \ 
|\ \ 
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|     --+--
|    /     \ 
|
|\ 
| \ 
|\ \ 
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|     --+--
|    /  |  \ 
|
|\ 
| \ 
|\ \ 
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|     --+--
|    /  |  \ 
|       |
|\      -
| \    /
|\ \ _/
| \ \ 
-----------
""",
"""
---------
|       |
|      ( )
|     --+--
|    /  |  \ 
|       |
|\      -
| \    / \ 
|\ \ _/   \_
| \ \ 
-----------
""",
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# initalize vars
word = random.choice(WORDS)
tracker = "-"*len(word)
wrong = 0
guessed = []

# game logic
print("""
        ____      ____         ___         ___        __   _______
       |    |    |    |       /   \       |    \     |  | /       \ 
       |    |    |    |      /     \      |     \    |  ||   ___   |      ( )
       |    |____|    |     /       \     |   \  \   |  ||  |   |  |      -+-
       |              |    /   /_\   \    |   |\  \  |  ||  |   |__|     / | \ 
       |     ____     |   /    ___    \   |   | \  \ |  ||  |  _____    /  |  \ 
       |    |    |    |  /    /   \    \  |   |  \  \|  ||  | |_   _|     / \ 
       |    |    |    | /    /     \    \ |   |   \  |  |\  \___| |      /   \ 
       |____|    |____|/____/       \____\|___|    \____| \_______|    _/     \_
       """)

while wrong < MAX_WRONG and tracker != word:
    print(HANGMAN[wrong])
    print("\tletter's used\n")
    for letter in guessed:
        print("\t" + str(letter)+"\n")

    guess = raw_input("guess: ")
    guess = guess.upper()

    while guess in guessed:
       print("you've already used that letter")
       guess = raw_input("guess: ")
       guess = guess.upper()
    guessed.append(guess)

    if guess in word:
        print("yes, " + str(guess) + " is in the word")
        # create new tracker to include in game
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += tracker[i]
        tracker = new
    else:
        print(str(guess) + " is not in the word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("END OF GAME")
else:
    print("you guessed it, well done")

