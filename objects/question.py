class question:
    # qid : int : Question ID
    # questionText : string : What's the actual question
    # answer : string : The correct answer to the question
    # incorrectChoices : string[] : All the incorrect answers
    # numAsked : int : number of times this question has been asked in the past
    # numCorrect : int : number of times people have got this question correct in the past
    # categories : string[] : which categories it belongs to
    def __init__(self,qid,questionText,answer,incorrectChoices,categories):
        self.qid = qid
        self.questionText = questionText
        self.answer = answer
        self.incorrectChoices = incorrectChoices
        self.numAsked = 0
        self.numCorrect = 0
        self.categories = categories

    def setSaveData(self,numask,numcorr):
        '''parses the save data and sets the number of times asked and the number of times correct'''
        self.numAsked = numask
        self.numCorrect = numcorr
