#################################################
# Deck.py
#
# Created by Darren Lee=
#################################################


import random
from Card import *
class Deck(object):
    def __init__(self, name = None, cards = None, copyDeck = None):
        if (copyDeck != None):
            self.name = copyDeck.name
            copyCards = []
            for eachCard in copyDeck.cards:
                copyCards.append(Card(None, None, eachCard))
            self.cards = copyCards
            return
        if (type(cards) != list):
            print("AGE TYPE IS NOT LIST:" + str(cards))
            assert(False)
        elif (type(name) != str):
            print("AGE TYPE IS NOT STRING:" + str(name))
            assert(False)
        self.name = name
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card)

    def __repr__(self):
        allCards = self.name + "\n"
        for eachCard in self.cards:
            allCards += str(eachCard) + "\n"
        return allCards[:-1]
    def randomize(self):
        random.shuffle(self.cards)