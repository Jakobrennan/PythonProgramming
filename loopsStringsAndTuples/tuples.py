inventory = ()

if not inventory:
    print("you got nothing atm")

print("click anything")

inventory = ("sword", 
             "shield", 
             "gold")
for item in inventory:
    print(item)

print("\n\n\n inventory 2.0 \n\n\n")

print("inventory has " + str(len(inventory)) + " items: ")

for item in inventory:
    print(item)

print("\n\n")

view_index = input("enter index of item you would like to see: (must be less than "+ str(len(inventory)) +") ")
print("item " + str(view_index) + " = " + str(inventory[view_index]))

print("\n\n slicing tuple")

index1 = input("select beginning index for inventory: ")
index2 = input("select end index for inventory: ")
print("inventory between " + str(index1) + " and " + str(index2) + " is : " + str(inventory[index1:index2]))


print("\n\n")

chest = ("gold", "gems")
for item in chest:
    print(item)

print("\n\n")
print("add chest to inventory")
inventory += chest

print("\n\n")
for item in inventory:
    print(item)

