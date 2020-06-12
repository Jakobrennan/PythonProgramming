# demonstrating reading from a file

print("opening and closing file")
text_file = open("read_it.txt", "r")
text_file.close()

print("reading from file")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("read entire thing at once")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("reading from line")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("read line at a time")
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("reading file into list")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("looping through file, line by line")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()
