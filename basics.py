# This file will just cover the basic syntax of the Python language

print("the 'print' method is very intersting " + " because you can not a lot of \n\n \t things on compile" * 2)

name = raw_input("type name : ")

print("Your just typed " + name)
print("Your just typed ", name)
print('quote manipulation')

# Thomas watson, chairman of IBM in 1943
quote = "I thINk tHEre is a wORLd marKET FOr maybe five coMPUTers"

print("Orignial: ")
print(quote)

print(quote.lower())
print(quote.title())
print(quote.upper())
print(quote.swapcase())
print(quote.strip())
print(quote.replace("five", "millions and millions"))
print(quote.replace("e", "", 2))

print("After applying numberous methods to the original quote ('"+quote+"'), the 'quote' remains unharmed")

a = raw_input("enter a number : ")
b = raw_input("enter a number : ")
c = raw_input("enter a number : ")

print('total = ', a + b + c)

print("now the actual total = ", int(a) + int(b) + int(c))

# using some augmented assignment operators

x = 10
print(x)

x  *= 5
print(x)

x /= 5
print(x)

x %= 5
print(x)

x += 5
print(x)

x -= 5
print(x)

age = int(raw_input("type your age to find out how many seconds you've been alive : "))
seconds = age * 364 * 24 * 60 * 60
print(seconds)

moon_weight = int(raw_input("input your weight in pounds: "))
moon_weight = moon_weight / 6
print("on the moon you'd weigh ", moon_weight, " pounds or something like that ")

raw_input("press enter to continue")
