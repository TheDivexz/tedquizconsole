from random import seed
from random import randint

class question:
    # qid : int : Question ID
    # questionText : string : What's the actual question
    # answer : string : The correct answer to the question
    # incorrectChoices : string[] : All the incorrect answers
    # numAsked : int : number of times this question has been asked in the past
    # numCorrect : int : number of times people have got this question correct in the past
    def __init__(self,qid,questionText,answer,incorrectChoices,numAsked,numCorrect):
        self.qid = qid
        self.questionText = questionText
        self.answer = answer
        self.incorrectChoices = incorrectChoices
        self.numAsked = numAsked
        self.numCorrect = numCorrect
