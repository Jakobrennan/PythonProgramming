import random

# primitive use of loop

intake = input("enter your word:\n")

for letter in intake:
    print(letter)

input("press enter to exit")

# using loop with range()

for i in range(1, 100):
    print(i, end=" ")
print("\n")
# in 5's

for i in range(0, 100, 5):
    print(i, end=" ")
print("\n")
# backwards in 2's

for i in range(100, 0, -2):
    print(i, end=" ")
print("\n")

# 'message analyzer'

message = input("input a message")

print("message length: ", len(message))

print("\nthe letter 'e'\n")
if "e" in message:
    print("is in your message")
else:
    print("is not in your message")

input("press enter to exit")

# random access

word = "onomatopoeia"
print("word ", word)
high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

print("press something to exit")
