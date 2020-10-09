import unittest
from sudoku import sudoku

class myTest(unittest.TestCase):

    def test_createGrid(self):
        mySu = sudoku()

        notNone = mySu.grid is not None
        self.assertEqual(notNone, True)

        self.assertEqual(isinstance(mySu.grid, list), True)
        self.assertEqual(len(mySu.grid), 3)


    def test_setCell(self):
        mySu = sudoku()

        mySu.setCell((0,0,1,2), 3)
        self.assertEqual(mySu.getCell((0,0,1,2)), 3)

        mySu.setCell((2,2,2,2), 6)
        self.assertEqual(mySu.getCell((2,2,2,2)), 6)


    def test_checkColumn(self):
    # 2 if full and correct
    # 1 if missing but correct
    # 0 if wrong  
        mySu = sudoku()

        puzzleComplete = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzleComplete)
        self.assertEqual(mySu.checkColumn((0,0)), 2)


        puzzle = '8.4....3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
        mySu.setGrid(puzzle)
        self.assertEqual(mySu.checkColumn((0,0)), 1)

        puzzleWrong = '743589261686412739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzleWrong)
        self.assertEqual(mySu.checkColumn((0,0)), 0)

        puzzleWrong2 = '743589261586432739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzleWrong2)
        self.assertEqual(mySu.checkColumn((1,1)), 0)


    def test_findEmpty(self):
        mySu = sudoku()

        #full
        puzzle = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzle)
        self.assertEqual(mySu.findEmpty()[0],-1)

        puzzle2 = '74.589261586412739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzle2)
        #need 0,0,0,2
        self.assertEqual(mySu.findEmpty()[3],2)
        self.assertEqual(mySu.findEmpty()[0],0)
        

    def test_checkRow(self):
    # 2 if full and correct
    # 1 if missing but correct
    # 0 if wrong
        mySu = sudoku()

        #Check wrong
        puzzle = '8.4.3..3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
        mySu.setGrid(puzzle)
        self.assertEqual(mySu.checkRow((0,0)), 0)

        #check missing
        puzzle2 = '72..491.5..5........3....27.3...........1...4.4......1.62.7..1.....9.5.6.1.5.3.4.'
        mySu.setGrid(puzzle2)
        self.assertEqual(mySu.checkRow((0,0)), 1)

        #check correct
        puzzle3 = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'
        mySu.setGrid(puzzle3)
        self.assertEqual(mySu.checkRow((0,0)), 2)


        puzzle4 = '72..491.5..5...5....3....27.3...........1...4.4......1.62.7..1.....9.5.6.1.5.3.4.'
        mySu.setGrid(puzzle4)
        self.assertEqual(mySu.checkRow((0,1)), 0)

if __name__ == '__main__':
        unittest.main()

       