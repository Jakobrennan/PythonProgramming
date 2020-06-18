# trivia game
# reads .txt file with questions and prints them

import sys

def open_file(file_name, mode):
    """simple open file function"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("unable to open file", file_name, " - ending program \n", e)
        input("press key to end")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """reads file, returns next line formatted"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


