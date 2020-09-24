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




grid = createGrid()

puzzle = '8.4....3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
puzzleComplete = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'

setGrid(grid,puzzleComplete)

print("after setting board:")

printGrid(grid)