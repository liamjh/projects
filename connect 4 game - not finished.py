

blank = 0

def initialiseboard(): # resets board to start.
    gameboard = [[0 for i in range(0,10) ] for j in range(0,9)]
    return gameboard

def setupgame():
    gamefinished = False
    thisplayer = "Z"
    return gamefinished, thisplayer


def outputboard(gameboard):
    maxrow = 6
    maxcolumn = 7
    for row in range(maxrow):
        for column in range(maxcolumn):
            print(gameboard[row][column], end = '')
        print()

def playerchoosescolumn(gameboard): # returns a valid column number
    print(thisplayer, "'s turn.")
    columnvalid = False
    while columnvalid != True:
        columnnumber = int(input("Enter a column number: "))
        if columnnumber >= 0 and columnnumber <= 6:
            if gameboard[5][columnnumber] == blank:
                columnvalid = True
        else:
            print("Enter a valid columnnumber. ")
    return columnnumber

def findfreerow(columnnumber, gameboard): # returns the next free position
    thisrow = 0
    while gameboard[thisrow] [columnnumber] != blank:
        thisrow += 1
    return thisrow


def playermakesmove():
    columnnumber = playerchoosescolumn(gameboard)
    thisrow = findfreerow(columnnumber, gameboard)
    gameboard[thisrow][columnnumber] = thisplayer
    return thisrow, columnnumber


def checkhorizontal(gameboard, thisrow, thisplayer):
    winnerfound = False
    for i in range(1, 4):
        if gameboard[thisrow][i] == thisplayer and gameboard[thisrow][i + 1] == thisplayer and gameboard[thisrow][i + 2] == thisplayer and gameboard[thisrow][i + 3] == thisplayer:
            winnerfound = True
        if gameboard[thisrow][i] == thisplayer and gameboard[thisrow][i - 1] == thisplayer and gameboard[thisrow][i - 2] == thisplayer and gameboard[thisrow][i - 3] == thisplayer:
            winnerfound = True
    return winnerfound
    
def checkvertical(gameboard, columnnumber, thisrow, thisplayer):
    winnerfound = False
    for i in range(1, 4):
        if gameboard[i][columnnumber] == thisplayer and gameboard[i + 1][columnnumber] == thisplayer and gameboard[i + 2][columnnumber] == thisplayer and gameboard[i + 3][columnnumber] == thisplayer:
            winnerfound = True
        if gameboard[i][columnnumber] == thisplayer and gameboard[i - 1][columnnumber] == thisplayer and gameboard[i - 2][columnnumber] == thisplayer and gameboard[i - 3][columnnumber] == thisplayer:
            winnerfound = True
        
    return winnerfound
    
def checkifwon():
    winnerfound = False
    gamefinished = False
    winnerfound = checkhorizontal(gameboard, thisrow, thisplayer)
    if winnerfound == False:
        winnerfound = checkvertical(gameboard, columnnumber, thisrow, thisplayer)
    if winnerfound == True:
        gamefinished = True
    return winnerfound, gamefinished
    
    
def checkboard(gameboard):
    blankfound = False
    gamefinished = False
    thisrow = 0
    thiscolumn = 0
    while thisrow != 7 or blankfound != True:
        thisrow += 1
        while thiscolumn != 7 or blankfound != True:
            thiscolumn += 1
            if gameboard[thisrow][thiscolumn] == blank:
                blankfound = True
    if blankfound == True:
        print("It is a draw.")
        gamefinished = True
    return gamefinished

def swapplayers(thisplayer):
    if thisplayer == "Z":
        thisplayer = "O"
    else:
        thisplayer = "Z"
    return thisplayer
    
    
    


#--------------------MainConsole-------------------------

gameboard = initialiseboard()
gamefinished, thisplayer = setupgame()
outputboard(gameboard)
while gamefinished == False:
    thisrow, columnnumber = playermakesmove()
    outputboard(gameboard)
    winnerfound, gamefinished = checkifwon()
    if winnerfound == False:
        thisplayer = swapplayers(thisplayer)
    elif winnerfound == True:
        print(thisplayer, "has won.")





