from objects.question import question
from objects.category import category
import os
from quizscript import quizparse as parser
from quizscript import quizinter as interpreter
from objects import *
from algorithims import questionsort as qsort
import random

def main():
    # Gets all the .txt files
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.txt')]
    # Master list of all the questions
    questions = []
    # All the question categories
    categories = []
    # Information from the save file
    savedata = []

    print("Reading questions...")
    # reads the question data
    for filename in file_list:
        f = open(filename)

        # Emulating a do while loop
        # Reads and Interprets all the Question blocks
        line = f.readline()
        while line:
            parsedLine = parser.parseLine(line)

            if interpreter.isQuestionBlock(parsedLine):
                qblocklines = []

                while line != "}":
                    qblocklines.append(parsedLine)
                    line = f.readline()

                qblockinterpreted = interpreter.interpretQuestionBlock(qblocklines)
                questions.append(qblockinterpreted)
            line = f.readline()
        qsort.sort(questions)

    print("Reading Save Data...")
    # CSV format is id;timesAsked;timesCorrect
    # Parses save file
    if os.path.exists("savedata.csv"):
        savefile = open("savedata.csv")
        saveinfo = savefile.readline()
        while saveinfo:
            savedata.append(saveinfo.split(";"))
            saveinfo = savefile.readline()
        savefile.close()

    # assign questions to categories and updates question difficulty if any
    saveindex = 0
    # So there is at least 1 category to avoid errors
    print("Assigning Questions...")
    categories.append(questions[0].categories[0])
    for index, q in enumerate(questions):
        for cat in q.categories:
            catExists = False
            for c in categories:
                if c.categoryTitle == cat:
                    c.addQuestion(index)
                    catExists = True
                    break
            if not catExists:
                categories.append(categories(cat))
                categories[len(categories)-1].addQuestion(index)
        if savedata and (saveindex <= len(savedata)-1) and (savedata[saveindex][0] == q.qid):
            q.numAsked = savedata[saveindex][1]
            q.numCorrect = savedata[saveindex][2]
            saveindex += 1
    # No need to hog up space
    savedata = []

    # Main User Loop
    while True:
        print("Enter the name of a category to get a question.\ntype !help to get help")
        userInput = input(">> ")
        if userInput[0] == '!':
            if userInput == "!help":
                print("type !c for the list of categories\nType !save to save your data and quit")
            elif userInput == "!c":
                print(categories)
            elif userInput == "!save":
                wr = open("savedata.csv","w")
                for q in questions:
                    if q.numAsked != 0:
                        strToWrite = str(q.qid) + ";" + str(q.numAsked) + ";" + str(q.numCorrect)
                        wr.write(strToWrite)
                wr.close()
                break
        else:
            for cat in categories:
                if cat.categoryTitle == userInput:
                    randqindex = cat.questions[random.randint(0,len(cat.questions)-1)]
                    questions[randqindex].numAsked += 1
                    print(questions[randqindex].questionText)
                    choices = questions[randqindex].incorrectChoices
                    choices.append(questions[randqindex].answer)
                    for _ in range(len(choices)):
                        randomABCD = choices.pop(random.randint(0,len(choices)-1))
                        if randomABCD == questions[randqindex].answer:
                            print(randomABCD, " (CORRECT ANSWER)")
                        else:
                            print(randomABCD)
                    didGetRight = userInput("Did they get the question right? (y/n) ")
                    if didGetRight == "y":
                        questions[randqindex].numCorrect += 1
                    for ct in questions[randqindex].categories:
                        for c in categories:
                            if ct == c.categoryTitle:
                                tempi = 0
                                for _ in range(len(c.questions)):
                                    if c.questions[tempi] == randqindex:
                                        break
                                    tempi += 1
                                c.questions.pop(tempi)
                                break
                    break

if __name__ == "__main__":
    main()