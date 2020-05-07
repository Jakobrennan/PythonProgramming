# creating list to hold hero's inventory

inventory = ["sword", "armor", "shield", "toothpick"]
for item in inventory:
    print(item)

print("\nyou have " + str(len(inventory)) + "items")

# using 'in' on a list

if "shield" in inventory:
    print("you are protected")

itemToPick = int(raw_input("pick a number between 1 and " + str(len(inventory))))
print("that item is: " + inventory[itemToPick])

start = raw_input("start of slice (max: "+str(len(inventory))+")")
end = raw_input("end of slice (max: "+str(len(inventory))+")")

print(str(start)+":"+str(end))
print(inventory[int(start):int(end)])

chest = ["gold", "potion"]
print(chest)
inventory += chest
print("inventory now contains : ")
print(inventory)

# what makes lists different to tuples is that they are mutable

print(inventory)
print("swapping sword with crossbow")
inventory[0] = "crossbow"
print(inventory)

# can swab index of list using slicing to

print("you acquire: orb of future \n it costs your armor and shield")
inventory[1:3] = ["orb of future teller"]
print(inventory)

# deleting 
print("losing the toothpick")
del inventory[2]
print(inventory)

print("deleting first 2 items with slicing")
del inventory[:2]
print(inventory)

