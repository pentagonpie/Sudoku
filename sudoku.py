
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
    return int(grid[position[0]][position[1]][position[2]][position[3]])

def setCell(grid, position, val):
    if not isinstance(val, int):
        print("got bad value for set cell!")
        exit(0)
    grid[position[0]][position[1]][position[2]][position[3]] = val

def checkRow(grid,loc):
    row = []
    for x in range(0,3):
        for cell in range(0,3):
            if getCell(grid, (loc[0],loc[1],x,cell)) != 0:
                row.append(getCell(grid, (loc[0],loc[1],x,cell)))
        

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
            if getCell(grid, (x,cell,loc[0],loc[1])) != 0:
                column.append(getCell(grid, (x,cell,loc[0],loc[1])))
    
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
    fullGrid = True
    for square in range(0,3):
        for row in range(0,3):
            resultRow = checkRow(grid, (row,square))
            if resultRow == 0:
                return 0

            #Even a single missing value means the grid is not full
            if resultRow != 2:
                fullGrid = False

    for square in range(0,3):
        for column in range(0,3):
            resultColumn = checkColumn(grid, (column,square))
            if resultColumn == 0:

                return 0

            #Even a single missing value means the grid is not full
            if resultColumn != 2:
                fullGrid = False
    
    for row in range(0,3):
        for column in range(0,3):
            resultGrid = checkSquare(grid, (row,column))
            if resultGrid == 0:

                return 0
            if resultGrid == 1:
                fullGrid = False

    if fullGrid:
        return 2

    return 1
            

#check square of numbers 3x3
#If single error found, return 0
#If no errors found, return 1
#If no errors found and square is full, return 2
def checkSquare(grid, loc):
    nums = []
    fullGrid = True
    for row in range(0,3):
        for column in range(0,3):
            x = getCell(grid, (loc[0],row,loc[1],column)) 
            if x != 0:
                nums.append(x)

            else:
                fullGrid = False

    unique = set(nums)
    if len(unique) != len(nums):
        return 0
    if fullGrid:
        return 2
    return 1

#DELETE this
def _checkSquare(grid, loc):
    nums = []
    fullGrid = True
    for row in range(0,3):
        for column in range(0,3):
            x = getCell(grid, (loc[0],row,loc[1],column)) 
            if x != 0:
                nums.append(x)

            else:
                fullGrid = False
    print("This is nums inside checksquare function")
    print(nums)
    unique = set(nums)
    if len(unique) != len(nums):
        return 0
    if fullGrid:
        return 2
    return 1


def findEmpty(grid):
    for row in range(0,3):
        for column in range(0,3):
            for subRow in range(0,3):
                for subColumn in range(0,3):
                    if getCell(grid, (row,subRow,column,subColumn)) == 0:
                        return  (row,subRow,column,subColumn)
    return (-1,-1,-1,-1)


def solveGrid(grid):
    empty = findEmpty(grid)
    # Were givin full grid
    if empty[0] == -1:
        if checkGridValid(grid) == 2:
            return 
        
    print("calling the function")
    print( _solveGrid(grid,empty))

    
def _solveGrid(grid,location):

    #Starting function with no spaces left, probably because grid is done, check it
    if location[0] == -1:
        if checkGridValid(grid) == 2:
            return True
        else:
            print("returning false")
            return False

    for i in range(1,10):
        setCell(grid,location, i)
        result = checkGridValid(grid)

        #finishd grid
        if result == 2:
            print("finished solving grid inside function, it is:")
            printGrid(grid)
            print("this is the real value inside function: ", checkGridValid(grid))
            print("this is square checking inside function",  _checkSquare(grid, (0,0)))
            return True


        if result == 0:
            setCell(grid,location,0)
            continue

        solved = _solveGrid(grid, findEmpty(grid))
        if solved:
            print("solved is true")
            return True


print("Starting program")
grid = createGrid()

puzzle = '8.4....3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
puzzle2 = '72..491.5..5........3....27.3...........1...4.4......1.62.7..1.....9.5.6.1.5.3.4.'

puzzleProblem = '814234536233156478545476112112345665379661243458728341543411923621553784734878915'

puzzleComplete = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'

################5 instead of 4
puzzleWrong = '753589261586412739219376458425937186967128345138645927894763512352891674671254893'
puzzleMissing = '7.3589261586412739219376458425937186967128345138645927894763512352891674671254893'
setGrid(grid,puzzle)

print("after setting board:")

printGrid(grid)
aPosition = (0,0,0,1)
#print("the cell is ", getCell(grid, aPosition)
#print("The grid in this cell is ", checkRowsColumns(grid,aPosition))
#print("check grid valid is ", checkGridValid(grid))


solveGrid(grid)
print("after solving with backtracking")
printGrid(grid)

#print("printing puzzle with problem:")
#grid2 = createGrid()
#setGrid(grid2, puzzleProblem)
#printGrid(grid2)
#print("value is ", checkGridValid(grid2))
