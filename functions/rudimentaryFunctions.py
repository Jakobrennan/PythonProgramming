# using functions on 3 ways

#basic function
def printHello(message):
    """simply prints the message when called"""
    if message == "":
        message = "default message"
    print(message)

#return
def returnInt():
    """returns the number 10"""
    value = 10
    return value

#returns value based on input
def askQ(q):
    """provide question and gain response"""
    print(q)
    response = None
    while response not in ("y", "n"):
        response = raw_input("answer (y or n): ")
    return response


printHello("Hello")
printHello("")
print(returnInt())
print("answer: " + str(askQ("is up up?")))
