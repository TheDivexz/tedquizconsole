import quizparse as parser
    
def interpretQuestionBlock(inter):
    iid = 0
    iqtext = ""
    ianswer = ""
    iincorrect = []
    icategories = []
    inumasked = 0
    inumcorrect = 0

    # There should be a more efficent way
    for i in inter:
        temp = parser.parseLine(inter)
        if temp[0] == "id":
            iid = int(temp[1])
        elif temp[0] == "num_asked":
            inumasked = int(temp[1])
        elif temp[0] == "num_correct":
            inumcorrect = int(temp[1])
        elif temp[0] = "text":
            iqtext = parser.pStripBrackets(temp[1])
        elif temp[0] == "answer"
            ianswer == parser.pStripBrackets(temp[1])