#################################################
# FlashCards.py
#
# Created by: Darren Lee, Chloe Chan
#################################################

from cmu_112_graphics import *
from Deck import *
from Card import *
import math

def appStarted(app):
    inputHandling(app)
    app.currDeck = app.allDecks[0]
    startScreenObjects(app)
    midpageObjects(app)
    standardModeObjects(app)
    waterfallObjects(app)

    app.startWithWord = False
    app.showWord = app.startWithWord
    app.gameOver = False

    app.selection = (-1,-1)
    app.startScreen = True
    app.midpage = False
    app.flipPage = False

    app.deckColorDict = {0: "cyan", 1: "lime", 2: "yellow", 3: "pink"}

def inputHandling(app):
    file1 = open("allWords.txt","r")
    app.allDecks = []
    currDeck = []
    currName = ""

    for fileLine in file1.readlines():
        line = fileLine.strip()
        if (line[0].isdigit()):
            wordStartInd = line.index(" ") + 1
            colonInd = line.index(":")
            wordEndInd = colonInd
            defStartInd = colonInd + 2
            defEndInd = len(line)

            word = line[wordStartInd: wordEndInd]
            definition = line[defStartInd: defEndInd]
            currCard = Card(word, definition)
            currDeck.append(currCard)
        elif (line[0] == "-"):
            if (currName == "" or currDeck == []):
                print("SOMETHING WRONG")
                assert(False)
            d = Deck(currName, currDeck)
            app.allDecks.append(d)
            currDeck = []
            currName = ""
        else:
            currName = line
    d = Deck(currName, currDeck)
    app.allDecks.append(d)
    file1.close()
def waterfallObjects(app):
    
    app.iterationNum = 1
    app.startIteration = False

    app.isWaterfall = False
    app.iterationNum = 1
    app.startIteration = False
    
    initializeWaterfall(app)


def startScreenObjects(app):
    app.startTopMargin = 150
    app.startMargin = 20

    app.startCellWidth = (app.width - 3*app.startMargin)//2
    app.startCellHeight = (app.height - app.startTopMargin - 2*app.startMargin)//2
    boxCenters(app)
    app.currDeckNames = [] # insert the name of the deck
    app.currDeckColor = [] # color based on subject 

    app.arrowCoords1 = (app.width - 25, app.startTopMargin//2)
    app.arrowCoords2 = (25, app.startTopMargin//2)
    app.pageNum = 0
    app.pages = len(app.allDecks) // 4
    app.currDeckSelected = None

def boxCenters(app):
    # box1
    x1 = app.startMargin + app.startCellWidth//2
    y1 = app.startTopMargin + app.startCellHeight//2

    # box2
    x2 = app.width - app.startMargin - app.startCellWidth//2
    y2 = y1

    # box3
    x3 = x1
    y3 = app.height - app.startMargin - app.startCellHeight//2

    # box4
    x4 = x2
    y4 = y3

    app.boxes = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

def midpageObjects(app):
    app.wordMode = True

    app.midTopMargin = 130
    app.midMargin = 35

    app.goWidth = (app.width - 3*app.midMargin)//6
    app.midCellWidth = app.width - 3*app.midMargin - app.goWidth
    app.midCellHeight = (app.height - app.midTopMargin - 2*app.midMargin)//2

def standardModeObjects(app):
    app.cardNum = 0
    app.currDeck.randomize()
    app.flipMargin = 40

def initializeWaterfall(app):
    app.iterationOver = False
    app.incorrectDeck = Deck("Incorrect Words", [])
    app.currDeck.randomize()
    app.cardNum = 0


############## mouse pressed / key pressed stuff
def dist(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5

def mousePressed(app, event):
    if app.startScreen:
        startScreenMousePressed(app, event)
    elif app.midpage:
        midpageMousePressed(app, event)
    elif app.isWaterfall:
        waterFallMousePressed(app, event)
    else:
        standardMousePressed(app, event)

def waterFallMousePressed(app, event):
    x0 = app.flipMargin
    y0 = app.flipMargin
    x1 = app.width - app.flipMargin
    y1 = app.height - app.flipMargin

    if (x0 <= event.x <= x1) and (y0 <= event.y <= y1):
        app.showWord = not app.showWord

def startScreenMousePressed(app, event):
    for i in range(4):
        cx, cy = app.boxes[i]
        i += app.pageNum*4
        if (cx-app.startCellWidth//2 <= event.x <= cx+app.startCellWidth//2) and\
            (cy-app.startCellHeight//2 <= event.y <= cy+app.startCellHeight//2):
            app.selection = (cx,cy)
            if (i < len(app.allDecks)):
                app.currDeckSelected = i
                app.startScreen = False
                app.midpage = True
                app.currDeck = Deck(copyDeck = app.allDecks[app.currDeckSelected])
                waterfallObjects(app)
                standardModeObjects(app)
    # arrows
    r = 10
    if dist(app.arrowCoords1[0], app.arrowCoords1[1], event.x, event.y) < r:
        if app.pageNum < app.pages:
            app.pageNum += 1
    elif dist(app.arrowCoords2[0], app.arrowCoords2[1], event.x, event.y) < r:
        if app.pageNum >0:
            app.pageNum -= 1

def midpageMousePressed(app, event):
    xr = app.midCellWidth//2
    yr = app.midCellHeight//2

    x1 = (app.width - app.goWidth - app.midMargin)//2
    y1 = app.midTopMargin + app.midCellHeight//2
    if (x1-xr <= event.x <= x1+xr) and (y1-yr <= event.y <= y1+yr):
        app.startWithWord = not app.startWithWord
    
    x2 = x1
    y2 = app.midTopMargin + app.midCellHeight + app.midMargin + app.midCellHeight//2
    if (x2-xr <= event.x <= x2+xr) and (y2-yr <= event.y <= y2+yr):
        app.isWaterfall = not app.isWaterfall

    # go part
    gx = app.width - app.midMargin - app.goWidth//2
    gy = app.midTopMargin + (app.height - app.midTopMargin - app.midMargin)//2 
    gxr = app.goWidth//2
    gyr = gxr*0.6
    if (gx-gxr <= event.x <= gx+gxr) and (gy-gyr <= event.y <= gy+gyr):
        app.midpage = False
        app.flipPage = True
        app.showWord = app.startWithWord

def standardMousePressed(app, event):
    x0 = app.flipMargin
    y0 = app.flipMargin
    x1 = app.width - app.flipMargin
    y1 = app.height - app.flipMargin

    if (x0 <= event.x <= x1) and (y0 <= event.y <= y1):
        app.showWord = not app.showWord

def keyPressed(app, event):
    
    if app.flipPage:
        if (app.isWaterfall):
            waterFallKeyPressed(app, event)
        else:
            standardKeyPressed(app, event)
    if (event.key == "r" and app.gameOver):
        appStarted(app)

def standardKeyPressed(app, event):

    if event.key == "Space":
        app.showWord = not app.showWord
    elif (event.key == "Right") and (app.cardNum < len(app.currDeck.cards)-1):
        app.cardNum += 1
        app.showWord = app.startWithWord
    elif (event.key == "Left") and (app.cardNum > 0):
        app.cardNum -= 1
        app.showWord = app.startWithWord
    elif (event.key == "Right") and (app.cardNum >= len(app.currDeck.cards)-1):
        app.gameOver = True
        
def waterFallKeyPressed(app, event):
    if event.key == "Space" and not app.gameOver:
        if (app.startIteration):
            app.showWord = not app.showWord
        app.startIteration = True
    elif (event.key == "Right") and (app.cardNum < len(app.currDeck.cards)-1):
        app.showWord = app.startWithWord
        app.cardNum += 1
    elif (event.key == "Left") and (app.cardNum > 0):
        app.showWord = app.startWithWord
        app.cardNum -= 1
    elif (event.key == "Right") and (app.cardNum >= len(app.currDeck.cards)-1):
        app.showWord = app.startWithWord
        app.iterationOver = True

    elif (event.key == "i"):
        app.currDeck.cards[app.cardNum].isCorrect = False
    elif (event.key == "c"):
        app.currDeck.cards[app.cardNum].isCorrect = True
    if (not app.gameOver):
        playWaterfall(app)

def playWaterfall(app):
    if (app.iterationOver):
        
        for card in app.currDeck.cards:
            if (card.isCorrect == False):
                toAdd = Card(card.word, card.definition)
                app.incorrectDeck.addCard(toAdd)
        app.iterationNum += 1
        app.currDeck = Deck(copyDeck = app.incorrectDeck)
        app.startIteration = False
        if (len(app.currDeck.cards) == 0):
            
            app.gameOver = True
            return
        initializeWaterfall(app)



########### start screen drawing stuff
def startScreenDrawings(app, canvas):
    canvas.create_text(app.width//2, app.startTopMargin//2, 
                            text = "Choose a Deck!", font = "Arial 60 bold")
    drawBoxes(app, canvas)
    drawArrow(app, canvas)
    
def drawDeck(app, canvas, leftEdge, topEdge, width, height, deckInd, color):
    margin = 4
    numCards = 7
    cardWidth = width - margin * (numCards - 1)
    cardHeight = height - margin * (numCards - 1)
    
    for i in range(numCards - 1):
        rightEdge = leftEdge + width - margin * i
        bottomEdge = topEdge + height - margin * i
        canvas.create_rectangle(rightEdge - cardWidth, bottomEdge - cardHeight,
            rightEdge, bottomEdge, fill = "white")

    canvas.create_rectangle(leftEdge, topEdge, leftEdge + cardWidth, 
                            topEdge + cardHeight, fill = color)
    cx = (2 * leftEdge + cardWidth) / 2
    cy = (2 * topEdge + cardHeight) / 2
    deckName = app.allDecks[deckInd].name
    canvas.create_text(cx, cy, text = deckName, font = "Arial 40 bold", width = int(cardWidth * 0.8))
def drawBoxes(app, canvas):
    for i in range(4):
        cx, cy = app.boxes[i]
        i += app.pageNum*4
        if i < len(app.allDecks):
            deckColor = app.deckColorDict[i % 4]
            drawDeck(app, canvas, cx-app.startCellWidth//2, cy-app.startCellHeight//2,
                            app.startCellWidth, app.startCellHeight,i, deckColor)
            
        
def drawArrow(app, canvas):
    r = 10
    if app.pageNum < app.pages:
        cx, cy = app.arrowCoords1
        canvas.create_line(cx-r, cy, cx+r, cy, width = 5) # middle
        canvas.create_line(cx, cy-r, cx+r, cy, width = 5) # top
        canvas.create_line(cx, cy+r, cx+r, cy, width = 5) # bottom

    if app.pageNum > 0:
        cx, cy = app.arrowCoords2
        canvas.create_line(cx-r, cy, cx+r, cy, width = 5) # middle
        canvas.create_line(cx-r, cy, cx, cy-r, width = 5) # top
        canvas.create_line(cx-r, cy, cx, cy+r, width = 5) # bottom
       

############ mid page drawing stuff
def midPageDrawings(app, canvas):
    canvas.create_text(app.width//2, app.midTopMargin//2, 
                        text = "Choose Your Options!", font = "Arial 60 bold")
    drawOptions(app, canvas)
    drawGo(app, canvas)

def drawGo(app, canvas):
    gx = app.width - app.midMargin - app.goWidth//2
    gy = app.midTopMargin + (app.height - app.midTopMargin - app.midMargin)//2 
    gxr = app.goWidth//2
    gyr = gxr*0.6

    canvas.create_rectangle(gx-gxr, gy-gyr, gx+gxr, gy+gyr, fill = "lime")
    canvas.create_text(gx, gy, text = "Go!", font = "Arial 30 bold")

def drawOptions(app, canvas):
    xr = app.midCellWidth//2
    yr = app.midCellHeight//2
    
    x1 = (app.width - app.goWidth - app.midMargin)//2
    y1 = app.midTopMargin + app.midCellHeight//2

    if app.startWithWord:
        text = "Word"
    else:
        text = "Definition"
    canvas.create_rectangle(x1-xr, y1-yr, x1+xr, y1+yr, fill = "light blue")
    canvas.create_text(x1, y1, text = text, font = "Arial 60 bold")
    
    x2 = x1
    y2 = app.midTopMargin + app.midCellHeight + app.midMargin + app.midCellHeight//2
    if not app.isWaterfall:
        text = "Standard Mode"
    else:
        text = "Waterfall Mode"
    canvas.create_rectangle(x2-xr, y2-yr, x2+xr, y2+yr, fill = "light yellow")
    canvas.create_text(x2, y2, text = text, font = "Arial 60 bold")

########## flip page drawing stuff
def drawStandard(app, canvas):
    drawCard(app, canvas, app.currDeck)

def drawCorrect(app, canvas):
    cx = app.width - app.flipMargin - 150
    cy = app.height - app.flipMargin - 125
    r = 40

    if app.currDeck.cards[app.cardNum].isCorrect == None:
        return
    elif app.currDeck.cards[app.cardNum].isCorrect == True:
        canvas.create_line(cx-r*(3/2), cy, cx, cy+r, fill = "lime", width = 15)
        canvas.create_line(cx, cy+r, cx+r*(3/2), cy-r*(3/2), fill = "lime", width = 15)
    elif app.currDeck.cards[app.cardNum].isCorrect == False:
        dist = r*math.sqrt(2)
        canvas.create_line(cx-dist, cy-dist, cx+dist, cy+dist, fill = "red", width = 15)
        canvas.create_line(cx-dist, cy+dist, cx+dist, cy-dist, fill = "red", width = 15)

def drawCard(app, canvas, deck):

    x0 = app.flipMargin
    y0 = app.flipMargin
    x1 = app.width - app.flipMargin
    y1 = app.height - app.flipMargin
    cardWidth = x1 - x0
    canvas.create_rectangle(x0, y0, x1, y1) 

    if app.showWord:
        canvas.create_text(app.width//2, app.height//2, 
                        text = deck.cards[app.cardNum].word,
                        font = "Arial 60 bold", width = int(cardWidth * 0.7))
    else:
        canvas.create_text(app.width//2, app.height//2, 
                        text = deck.cards[app.cardNum].definition,
                        font = "Arial 50", width = int(cardWidth * 0.75))

def drawNewIteration(app, canvas):
    x0 = app.flipMargin
    y0 = app.flipMargin
    x1 = app.width - app.flipMargin
    y1 = app.height - app.flipMargin
    iterationColor = app.deckColorDict[app.currDeckSelected % 4]
    canvas.create_rectangle(x0, y0, x1, y1, fill = iterationColor)
    canvas.create_text(app.width//2, app.height//2, 
                            text = "Iteration " + str(app.iterationNum),
                            font = "Arial 60 bold")
    canvas.create_text(app.width//2, app.height//2 + 70, 
                            text = "Press Space to Start!",
                            font = "Arial 30 bold")

def drawGameOver(app, canvas):
    x0 = app.flipMargin
    y0 = app.flipMargin
    x1 = app.width - app.flipMargin
    y1 = app.height - app.flipMargin
    canvas.create_rectangle(x0, y0, x1, y1, fill = "cyan")
    canvas.create_text(app.width//2, app.height//2, 
                            text = "Finished!",
                            font = "Arial 60 bold")
    canvas.create_text(app.width//2, app.height//2 + 70, 
                            text = "Press 'r' go back to main page!",
                            font = "Arial 30 bold")

######## redraw all
def redrawAll(app, canvas):
    # start screen
    if app.startScreen:
        startScreenDrawings(app, canvas)

    # midpage
    if app.midpage:
        midPageDrawings(app, canvas)

    
    # flipcard
    if app.flipPage:
        if (app.isWaterfall):
            if (app.startIteration):
                drawCard(app, canvas, app.currDeck)
                drawCorrect(app, canvas)
            else:
                if (app.gameOver):
                    drawGameOver(app, canvas)
                else:
                    drawNewIteration(app, canvas)
        else:
            if (app.gameOver):
                drawGameOver(app, canvas)
            else:
                drawStandard(app, canvas)

runApp(width = 1200, height = 900)
