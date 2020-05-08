# improved high scored program using _nested squences_


scores = []
choice = None

while choice != "0":
    print("""

    high scores 2.0

    0   -   exit
    1   -   show scores
    2   -   add a score
    """)

    choice = raw_input("choice: ")
    print()

    if choice == "0":
        print("end program")
    elif choice == "1":
        print("scores")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(str(name) + "\t" + str(score))
    elif choice == "2":
        name = str(raw_input("player's name: "))
        score = int(raw_input("player's score: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("you didn't pick a valid option")

