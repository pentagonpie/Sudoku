import numpy as np

def createGrid():


    columns = []
    for _ in range(0,3):
        a_row = []
        for _ in range(0,3):
            square = [[0,0,0] for y in range(0,3)]
            a_row.append(square)
        columns.append(a_row)
    return columns

def printGrid(grid):

    for column in grid:
        for row in column:
            strRow = ""

            for square in row:

                strRow += "|{} {} {}|".format(square[0],square[1],square[2])

            print(strRow)

        print("---------------------")

def setGrid(grid, puzzle):  
    count = 0
    for x, column in enumerate(grid):
        
        for y,row in enumerate(column):
            for z,square in enumerate(row):
                for q, cell in enumerate(square):
                    if puzzle[count] != '.':
                        grid[x][y][z][q] = puzzle[count]
                    count+=1

def getCell(grid, position):
    return grid[position[0]][position[1]][position[2]][position[3]]


def checkRow(grid,loc):
    row = []
    for x in range(0,3):
        for cell in range(0,3):
            row.append(grid[loc[0]][loc[1]][x][cell])
        

    #Creates a set from the row of numbers, if there are duplicates, the set will be smaller
    reduced = set(row)
    if len(reduced) != len(row):
        return 0

    if len(row) == 9:
        return 2
    else:
        return 1



def checkColumn(grid,loc):
    column = []
    for x in range(0,3):
        for cell in range(0,3):
            column.append(grid[x][cell][loc[0]][loc[1]])
    
    #Creates a set from the column of numbers, if there are duplicates, the set will be smaller
    reduced2 = set(column)
    if len(reduced2) != len(column):
        return 0

    if len(column) == 9:
        return 2
    else:
        return 1



#Function to check if current state of grid, more specifically the rows and columns of the current new add cell, are valid.
#They might still be missing values, but check if current values are valid
def checkRowsColumns(grid, position):

    resultRows = checkRow(grid, (position[0],position[1]))
    resultColumn = checkColumn(grid, (position[2],position[3]))

    #Both are atleast valid, maybe even full valid
    if resultRows >1 and  resultColumn > 1:
        return True
    
    #Return true because didn't return false in all tests
    return False

#check entire grid
#If single error found, return 0
#If no errors found, return 1
#If no errors found and grid is full, return 2
def checkGridValid(grid):
    pass





grid = createGrid()

puzzle = '8.4....3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
puzzleComplete = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'

################5 instead of 4
puzzleWrong = '753589261586412739219376458425937186967128345138645927894763512352891674671254893'
setGrid(grid,puzzleWrong)

print("after setting board:")

printGrid(grid)
aPosition = (0,0,0,1)
print("the cell is ", getCell(grid, aPosition))

print("new")


print("The grid in this cell is ", checkRowsColumns(grid,aPosition))
print("\n")
