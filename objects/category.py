import question
# all questions within a category have similar themes.
class category:
    # categoryTitle : string : The Name of the Category
    # questions : question[] : All the questions within a category
    def __init__(self, categoryTitle,qid):
        self.categoryTitle = categoryTitle
        self.qid = qid
        self.questions = []

    def addQuestion(self,q):
        '''Adds a question to the category'''
        self.uncategorized.append(q)

    def getQuestion(self):
        '''gets an Uncategorzed question then deletes it from the list'''
        temp = randint(0,len(self.questions)-1)
        return self.questions.pop(temp)

