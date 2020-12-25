#################################################
# Card.py
#
# Created by Darren Lee
# Your andrew id: darrenl
#################################################


class Card(object):
    def __init__(self, word = None, definition = None, copyCard = None):
        if (copyCard != None):
            self.word = copyCard.word
            self.definition = copyCard.definition
            self.isCorrect = None
            return
        if (type(word) != str):
            print("NAME TYPE IS NOT STRING: " + str(word))
            assert(False)
        elif (type(definition) != str):
            print("AGE TYPE IS NOT STRING:" + str(definition))
            assert(False)

        self.word = word
        self.definition = definition
        self.isCorrect = None
    
    def __repr__(self):
        return (self.word + ": " + str(self.definition) + " (" + 
                        str(self.isCorrect) + ")")
