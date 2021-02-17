import os
import sys
from random import seed
from random import randint

# The Question Object
class question:

    def __init__(self,questionText,answer,dud1,dud2,dud3):
        self.questionText = questionText
        self.answer = answer
        self.dud1 = dud1
        self.dud2 = dud2
        self.dud3 = dud3

# Stores all the questions in each category
class category:

    def __init__(self,categoryTitle):
        self.categoryTitle = categoryTitle
        self.questions = []

    def addToQuestions(self,questionToAdd):
        self.questions.append(questionToAdd)

def main():
    # Gets all the files with a .txt extension
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.txt')]
    categories = []

    for filename in file_list:

        f = open(filename)
        fname = f.readline()
        categories.append(category(fname))
        fquestion = f.readline()

        while fquestion:
            a1 = f.readline()
            a2 = f.readline()
            a3 = f.readline()
            a4 = f.readline()
            categories[len(categories)-1].addToQuestions(question(fquestion,a1,a2,a3,a4))
            fquestion = f.readline()
    
    # Main User Loop
    while True:
        print("Enter category number to recieve a question\ntype -1 to get a list of all the categories")
        userInput = int(input(">> "))
        if userInput == -1:
            for index, cat in enumerate(categories):
                # None is the equivalent of null in python because Python likes to be special
                if cat != None:
                    print(index,"-",cat.categoryTitle)
        
        else:
            catnumber = userInput
            qnum = randint(0,len(categories[catnumber].questions))
            print(categories[catnumber].questions[qnum].questionText)
            print(categories[catnumber].questions[qnum].answer)
            print(categories[catnumber].questions[qnum].dud1)
            print(categories[catnumber].questions[qnum].dud2)
            print(categories[catnumber].questions[qnum].dud3)
            categories[catnumber].questions.pop(qnum)  

if __name__ == "__main__":
    main()
