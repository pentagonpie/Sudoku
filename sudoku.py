class sudoku: 
    def __init__(self):
        self.grid = self.__createGrid()


    #Create new grid for sudoku class
    #The index tuple for the grid is as follows:
    """
       J       J      J
      i i i 
    k 1 2 3  4 5 6  7 8 9
 Q  k 2 3 4  5 6 7  8 9 1
    k 3 4 5  6 7 8  9 1 2

     4 5 6  7 8 9  1 2 3
 Q   5 6 7  8 9 1  2 3 4
     ...


    (q,k,j,i)

    row:
    a b c d e f

    column:
    a
    b
    c
    d
    e
    f
    """
    def __createGrid(self):
        columns = []
        for _ in range(0,3):
            a_row = []
            for _ in range(0,3):
                square = [[0,0,0] for y in range(0,3)]
                a_row.append(square)
            columns.append(a_row)
        return columns

    def printGrid(self):
        for column in self.grid:
            for row in column:
                strRow = ""

                for square in row:

                    strRow += "|{} {} {}|".format(square[0],square[1],square[2])

                print(strRow)

            print("---------------------")

    #Setting grid with info from puzzle, given as a string of numbers and dots for zero
    def setGrid(self, puzzle):  
        #index of digit in puzzle
        count = 0

        for a in range(0,3):
            for b in range(0,3):
                for c in range(0,3):
                    for d in range(0,3):

                        if puzzle[count] != '.':
                            self.setCell((a,b,c,d), int(puzzle[count]))
                        else:
                            self.setCell((a,b,c,d), 0)
                        count+=1

    #Return single digit from board at position
    def getCell(self, position):
        if position[0] > 2 or position[0] < 0:
            print("first parameter in getCell out of bounds")
        if position[1] > 2 or position[1] < 0:
            print("second parameter in getCell out of bounds")
        if position[2] > 2 or position[2] < 0:
            print("third parameter in getCell out of bounds")
        if position[3] > 2 or position[3] < 0:
            print("fourth parameter in getCell out of bounds")
        return int(self.grid[position[0]][position[1]][position[2]][position[3]])

    #Set a single digit at board at position, value is val
    def setCell(self, position, val):
        if not isinstance(val, int):
            raise("set cell method got value other than int!")
        self.grid[position[0]][position[1]][position[2]][position[3]] = val

    #Checks entire row in grid
    # 2 if full and correct
    # 1 if missing but correct
    # 0 if wrong
    def checkRow(self,loc):
        row = []
        for x in range(0,3):
            for cell in range(0,3):
                aCell = self.getCell( (loc[0],loc[1],x,cell)) 
                if aCell != 0:
                    row.append(aCell)
            
        #Creates a set from the row of numbers, if there are duplicates, the set will be smaller
        reduced = set(row)
        if len(reduced) != len(row):
            return 0

        if len(row) == 9:
            return 2
        else:
            return 1


    #Checks entire column in grid
    # 2 if full and correct
    # 1 if missing but correct
    # 0 if wrong
    def checkColumn(self,loc):
        column = []
        for x in range(0,3):
            for cell in range(0,3):
                if self.getCell( (x,cell,loc[0],loc[1])) != 0:
                    column.append(self.getCell( (x,cell,loc[0],loc[1])))
        
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
    def checkRowsColumns(self, position):

        resultRows = self.checkRow( (position[0],position[1]))
        resultColumn = self.checkColumn( (position[2],position[3]))

        #Both are atleast valid, maybe even full valid
        if resultRows >1 and  resultColumn > 1:
            return True
        
        #Return false because didn't return true in all tests
        return False

    #check entire grid
    #If single error found, return 0
    #If no errors found, return 1
    #If no errors found and grid is full, return 2
    def checkGridValid(self):
        fullGrid = True
        for square in range(0,3):
            for row in range(0,3):
                resultRow = self.checkRow( (row,square))
                if resultRow == 0:
                    return 0

                #Even a single missing value means the grid is not full
                if resultRow != 2:
                    fullGrid = False

        for square in range(0,3):
            for column in range(0,3):
                resultColumn = self.checkColumn( (column,square))
                if resultColumn == 0:

                    return 0

                #Even a single missing value means the grid is not full
                if resultColumn != 2:
                    fullGrid = False
        
        for row in range(0,3):
            for column in range(0,3):
                resultGrid = self.checkSquare( (row,column))
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
    def checkSquare(self, loc):
        nums = []
        fullGrid = True
        for row in range(0,3):
            for column in range(0,3):
                x = self.getCell( (loc[0],row,loc[1],column)) 
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
    def _checkSquare(self, loc):
        nums = []
        fullGrid = True
        for row in range(0,3):
            for column in range(0,3):
                x = self.getCell( (loc[0],row,loc[1],column)) 
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


    #Function to find next empty cell in a grid, if found none, return default (-1,-1,-1,-1) 
    def findEmpty(self):
        for row in range(0,3):
            for column in range(0,3):
                for subRow in range(0,3):
                    for subColumn in range(0,3):
                        if self.getCell( (row,subRow,column,subColumn)) == 0:
                            return  (row,subRow,column,subColumn)
        return (-1,-1,-1,-1)


    #Main method to solve the grid using backtracking
    def solveGrid(self):
        empty = self.findEmpty()
        # Were givin full grid
        if empty[0] == -1:
            if self.checkGridValid() == 2:
                return 
            
        print("calling the function")
        print( self._solveGrid(empty))

        
    #Recursive method used by solveGrid to find the solution for the sudoku puzzle
    def _solveGrid(self,location):

        #Starting function with no spaces left, probably because grid is done, check it
        if location[0] == -1:
            if self.checkGridValid() == 2:
                return True
            else:
                print("returning false")
                return False
        solved = False
        for i in range(1,10):
            self.setCell(location, i)
            result = self.checkGridValid()
            #print("trying ", i, " at location ", location)

            #finishd grid
            if result == 2:
            
                return True

            #wrong input, delete
            if result == 0:
                self.setCell(location,0)
                continue

            #if reached here, last input was not wrong but also didn't complete board, try recursivly all other possible inputs after the current input
            solved = self._solveGrid( self.findEmpty())
            if solved:
                return True
            

        if solved == False:
            #wrong input, delete
            self.setCell(location,0)
            return False

        