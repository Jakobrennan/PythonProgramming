# pizza slicing program that slices the word pizza

print("""
        0   1   2   3   4   5
        |   |   |   |   |   |
        ---------------------
        | p | i | z | z | a |
        ---------------------
        |   |   |   |   |   
       -5  -4  -3  -2  -1   
       """)
word="pizza"
pos1 = None
while pos1 != "":
    pos1 = input("\ninput starting position: ")
    if pos1:
        pos1 = int(pos1)
        pos2 = int(input("\ninput finishing position: "))
        print("result: ", word[pos1:pos2])

print("click anything to exit")
