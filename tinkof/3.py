def getSequence():
    blocksSequence = input()
    if len(blocksSequence) >= 1 and len(blocksSequence) <= 1000:
        checkSequence(blocksSequence)
    else:
        print("invalid value")

def checkSequence(blocksSequence):
    sequenceCorrect = True
    for value in blocksSequence:
        if int(value) == 0 or int(value) == 1:
            continue
        else:
            print("invalid value")
            sequenceCorrect = False
            break
    if sequenceCorrect == True:
        getBlocksPositionsArray(blocksSequence)
    
def getBlocksPositionsArray(blocksSequence):
    blocksPositionsArray = []
    for value in blocksSequence:
        blocksPositionsArray.append(int(value))
    field = createField()
    fillField(blocksPositionsArray, field)

def createField():
    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return field

def fillField(blocksPositionsArray, field):
    for block in blocksPositionsArray:
        if block == 0:
            searchVerticalBlockParckingSpace(field)
        elif block == 1:
            searchHorizontalBlockParckingSpace(field)
        checkColumns(field)
        checkRows(field)
    showField(field)

def searchHorizontalBlockParckingSpace(field):
    stopIteration = False
    for row in range(0, 4):
        if stopIteration == False:
            for column in range(0, 4):
                if column + 1 <= 3:
                    if field[row][column] == 0 and field[row][column + 1] == 0:
                        field[row][column] = 1
                        field[row][column + 1] = 1
                        print(row + 1, column + 1)
                        stopIteration = True
                        break
                    else:
                        continue
        else:
            break

def searchVerticalBlockParckingSpace(field):
    stopIteration = False
    for row in range(0, 4):
        if stopIteration == False:
            for column in range(0, 4):
                if row + 1 <= 3:
                    if field[row + 1][column] == 0 and field[row][column] == 0:
                        field[row][column] = 1
                        field[row + 1][column] = 1
                        print(row + 1, column + 1)
                        stopIteration = True
                        break
                    else:
                        continue
        else:
            break

def checkRows(field):
    rowFullnes = 0
    for row in range(0, 4):
        for column in range(0, 4):
            if field[row][column] == 1:
                rowFullnes += 1
        if rowFullnes == 4:
            clearRow(field, row)
        rowFullnes = 0
        
def checkColumns(field):
    columnFullnes = 0
    for column in range(0, 4):
        for row in range(0, 4):
            if field[column][row] == 1:
                columnFullnes += 1
        if columnFullnes == 4:
            clearRow(field, column)
        columnFullnes = 0

def clearRow(field, row):
    for x in range(0, 4):
        field[row][x] = 0

def clearColumn(field, column):
    for y in range(0, 4):
        field[y][column] = 0

def showField(field):
    for row in field:
        print(*row)

getSequence()