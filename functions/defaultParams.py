# creating functions with default params

def birthday(name, age):
    """prints message with provided params"""
    print("HAPPY BIRTHDAY " + name.upper() + ", you're " + str(age) + " today!")


#has default params
def birthday2(name = "bob", age = 80):
    """prints message with provided params"""
    print("HAPPY BIRTHDAY " + name.upper() + ", you're " + str(age) + " today!")

birthday("name", 30)
birthday2("not bob", 8)
birthday2()
