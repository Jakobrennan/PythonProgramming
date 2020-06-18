# using try statements and `exceptions` to handle errors

try:
    num = float(input("input a number: "))
except:
    print("error occured - possibly not a number")

#sprcifying an error
try:
    num = float(input("input a number: "))
except ValueError:
    print("not a number")

print()

# handling multiple exceptions

for value in (None, "string"):
    try:
        print("attempting to convert", value, end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("error occured")

for value in (None, "string"):
    try:
        print("attempting to convert", value, end=" ")
        print(float(value))
    except TypeError: 
        print("can only handle string or number types")
    except ValueError:
        print("only handle string of digits")

# getting an exceptions argument

try:
    num = float(input("input a number: "))
except ValueError as e:
    print("error occured - argument is: ")
    print(e)

# adding 'else' clauses
try:
    num = float(input("input a number: "))
except ValueError as e:
    print("error occured - argument is: ")
    print(e)
else:
    print("number is", num)
