# illustrating an infinite loop

health = 10
damage = 3
trolls = 0

print("""
    surrounded and afraid, you take your sword and swing
""")

while health != 0: # fix by placing '>' operator
    trolls += 1
    health -= damage
    print("your health is " + str(health) + ", there are " + str(trolls) + " trolls attacking, there's no hope")
