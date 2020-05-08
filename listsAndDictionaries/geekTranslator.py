# first use of dictionaries

words = {"error":"A wandering; a roving or irregular course.",
        "perpetual":"A body of law, sanctioned by legislation",
        "king":"A chief ruler; a sovereign; one invested with supreme...",
        "game":"Sport of any kind; jest, frolic.",
        "math":"a science (or group of related sciences) dealing with the..."}

words["king"]

choice = None
while choice != "0":
    print("""
    GEEK TRANSLATOR

    0   -   exit
    1   -   look up geek term
    2   -   add geek term
    3   -   redefine term
    4   -   delete term
    """)

    choice = raw_input("select your option: ")

    if choice == "0":
        print("end program")
    elif choice == "1":
        word = str(raw_input("input word your looking for: "))
#        if word in words:
#            print(words[word])
#        else:
#            print("that word isn't in your dictionary")
        print(words.get(word, "that word doesn't exist"))
    elif choice == "2":
        term = raw_input("input new word: ")
        if term not in words:
            definition = raw_input("input definition:\n")
            words[term] = definition
            print("\n" + term + " has been added")
    elif choice == "3":
        term = raw_input("word you want to rededine: ")
        if term not in words:
            print("that word does not exist")
        else:
            definition = raw_input("write new definition:\n")
            words[term] = definition
    elif choice == "4":
        term = raw_input("term you want tot delete: ")
        if term not in words:
            print("cannot delete " + term + " as it doesn't exist")
        else:
            del words[term]
            print(term + " has been deleted")
    else:
        print("not an option")

