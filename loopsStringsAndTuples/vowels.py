# learnig about immutable strings, you cannot change a string you have already
# assigned to a variable name
# proof below loops through a given string and prints the product of your string
# (with no vowels) 
# the new string has been assigned to a new variable, but it is printed
# everytime, so it has been reassigned to the new variable, the old varaible
# still existed, you can't go back an change it during the process of the
# program

message = raw_input("enter your string: ")
new_string = ""
vowels = "aeiou"

for letter in message:
    if letter.lower() not in vowels:
        new_string+= letter
        print("new message: ", new_string)

print("\n\n click enter to exit")


