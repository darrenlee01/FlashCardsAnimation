Twizlet!!
By Chloe Chan (chloec) and Darren Lee (darrenl)

File to run: MasterAnimationFile.py
################################################################################

INTRODUCTION:

Our program is basically Quizlet, with a twist! It takes a text file of
vocabulary words and definitions, which we called 'decks'. The user can choose
the deck to study from, whether they want the word or definition to appear 
first, as well as if they want to study in Standard mode or Waterfall mode 
(see description below). 

Standard Mode: Runs through all cards once

Waterfall Mode: 
- If you get the card right, press 'c'
- If you get the word wrong, press 'i'
- A corresponding green check or red X appears in the bottom right corner of 
  the flashcard. All the incorrect cards are reshuffled into a new list, and 
  you have to keep doing those cards until you get all of them right. 
- You can find more info here: 
  https://blog.prepscholar.com/the-best-way-to-study-sat-vocab-words 
  (scroll down to 'How to Study SAT Vocab the Right Way: The Waterfall Method')

################################################################################

IMPORTANT INPUTS:

Initial Start Screen:
- Click on the arrows in the top corners to go to the next/previous pages of 
  decks
- Click on the deck you want to study

Options Mid Screen:
- Click on the top box to toggle whether or not you want the word or definition 
  to appear first
- Click on the bottom box to toggle Standard/Waterfall Mode
- Click on 'Go!' to start studying!

Flashcard Screen:
- 'Space' or clicking on the card flips it over to the other side
- 'Left' moves on to the  next card
- 'Right' moves back to the previous card
- For Waterfall Mode, see above for more inputs ('i' and 'c')

Finished Screen:
- 'r' brings you back to the main page to choose a deck

################################################################################
INPUT TEXT FILE FORMAT (for the words/definitions):

Naming Decks:
- Must name Deck first, then have cards, then separating decks (do not end with
  the dashes)
- For example:
    Spanish Vocab
	10. hola como estas?: hello, how are you doing?
	--------
	ACT Vocab
	1. Unprecedented: never done or known before

New flashcard format:
- Number. Word Word Word: Definition Definition Def Definition
- For example:
    10. hola como estas?: hello, how are you doing?

Separating Decks:
- Put any number of dashes as long as the first index is a dash
- For example:
    ------------------------

################################################################################
MODULES USED:

- 112 Animation Module (cmu_112_graphics)
- Card.py: our own Card class that consists of: 
    - str word
    - str definition
    - bool isCorrect
- Deck.py: our own Deck class that consists of:
    - str name
    - Card[] cards

Thanks for reading! :)