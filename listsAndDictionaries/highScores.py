scores = []
choice = None

while choice != "0":
    print("""

    high scores

    0   -   exit
    1   -   show scores
    2   -   add a score
    3   -   delete a score
    4   -   sort scores
    """)

    choice = raw_input("choice: ")
    print()

    if choice == "0":
        print("end program")
    elif choice == "1":
        print("high scores")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(raw_input("what was your score: "))
        scores.append(score)
    elif choice == "3":
        score = int(raw_input("what was your score: "))
        if score in scores:
            scores.remove(score)
        else:
            print(str(score)+" isn't in the list")
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("you didn't pick a valid option")

