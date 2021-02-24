import random
# all questions within a category have similar themes.
class category:
    # categoryTitle : string : The Name of the Category
    # questions : int[] : stores the index fo the questions in the master array
    def __init__(self, categoryTitle):
        self.categoryTitle = categoryTitle
        self.questions = []

    def addQuestion(self,q):
        '''Adds a question index to the category list'''
        self.uncategorized.append(q)

    def getQuestion(self):
        '''gets an Uncategorzed question then deletes it from the list'''
        temp = random.randint(0,len(self.questions)-1)
        return self.questions.pop(temp)

