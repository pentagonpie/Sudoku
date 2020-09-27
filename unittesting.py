import unittest
import sudoku

class myTest(unittest.TestCase):

    def test_createGrid(self):
        mySu = sudoku()
        grid = mySu.createGrid()

        notNone = grid is not None
        self.assertEqual(notNone, True)

        self.assertEqual(isinstance(grid, list), True)



if __name__ == '__main__':
        unittest.main()

       