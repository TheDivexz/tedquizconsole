from . import quizparse as parser
from objects import question
    
def interpretQuestionBlock(inter):
    '''Interprets the code inside of a Question = { } block.
        returns [QUESTION OBJECT, LIST OF CATEGORIES]'''
    iid = 0
    iqtext = ""
    ianswer = ""
    iincorrect = []
    icategories = []

    # There should be a more efficent way
    for i in inter:
        temp = parser.parseLine(i)
        if temp[0] == "id":
            iid = int(temp[1])
        elif temp[0] == "text":
            iqtext = parser.pStripBrackets(temp[1])
        elif temp[0] == "answer":
            ianswer = parser.pStripBrackets(temp[1])
        elif temp[0] == "incorrect":
            iincorrect = parser.pList(temp[1])
        elif temp[0] == "category":
            icategories = parser.pList(temp[1])

    return question(iid,iqtext,ianswer,iincorrect,icategories)

def isQuestionBlock(inter):
    '''checks to see if paramater is start of a question block'''
    if not inter:
        return False
    if inter[0] == "question" and inter[1] == "{":
        return True
    return False