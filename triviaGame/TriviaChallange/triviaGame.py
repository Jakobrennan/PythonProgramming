# trivia game
# reads .txt file with questions and prints them

import sys, pickle, shelve

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

def next_block(the_file):
    """reads next block in template trivia file"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """welcomes player"""
    print("\t\tWelcome to trivia challenge\n")
    print("\t\t", title, "\n")
    name = input("what's your name: ")
    return name

def write_leaderboard(score, name):
    LB = open("leaderboard.dat", "ab+")
    user = [name, score]
    pickle.dump(user, LB)
    LB.close()

def read_leaderboard():
    LB = open("leaderboard.dat", "ab+")
    board = pickle.load(LB)
    print(board)
    LB.close()

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    name = welcome(title)
    score = 0
    
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask questions
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, " - ", answers[i])

        #getting answer
        answer = input("what's your answer: ")
 
        #check answer
        if answer == correct:
            print("\ncorrect", end=" ")
            score += 1
        else:
            print("\nincorrect\n", end=" ")
        print(correct)
        print(explanation)
        print("score: ", score, "\n")
 
        # getting next question
        category, question, answers, correct, explanation = next_block(trivia_file)
    
    trivia_file.close()
    print("that was the last question")
    print("you're final score: ", score)
    write_leaderboard(score, name)

main()
read_leaderboard()
input("press enter to exit")
