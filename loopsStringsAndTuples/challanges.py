# simple method that counts between 2 numbers with the displacement you set

#start = int(raw_input("starting number: "))
#end = int(raw_input("ending number: "))
#displacement = int(raw_input("displacement number: "))
#
#while start <= end:
#    print(start)
#    start += displacement

# print message backwords

mess = raw_input("enter message: ")
back = ""

for i in range(len(mess), 0, -1):
    back += mess[i-1:i]

print(back)

# simple
