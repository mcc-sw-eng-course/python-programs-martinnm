import unittest
from checkers import *
from unittest import mock

class testCheckers(unittest.TestCase):

    def test_correctBoundaries(self):
        checkers = Checkers()
        self.assertTrue(checkers.checkBoundaries(1, 1))

    def test_incorrectBoundaries(self):
        checkers = Checkers()
        self.assertFalse(checkers.checkBoundaries(1, 10))

    def test_freePiece(self):
        checkers = Checkers()
        self.assertTrue(checkers.isPieceFree(1, 4))

    def test_freePieceEdgeY0(self):
        checkers = Checkers()
        self.assertTrue(checkers.isPieceFree(1, 0))

    def test_freePieceEdgeY7(self):
        checkers = Checkers()
        self.assertTrue(checkers.isPieceFree(1, 7))

    def test_freePieceEdgeX0(self):
        checkers = Checkers()
        self.assertTrue(checkers.isPieceFree(0, 3))

    def test_freePieceEdgeX7(self):
        checkers = Checkers()
        self.assertTrue(checkers.isPieceFree(7, 3))

    def test_InvalidMove(self):
        checkers = Checkers()
        self.assertFalse(checkers.checkValidSimpleMove(7, 2, 1, 1))

    def test_validMove(self):
        checkers = Checkers()
        self.assertTrue(checkers.checkValidSimpleMove(1, 1, 2, 2))

    def test_validMoveReverse(self):
        checkers = Checkers()
        self.assertTrue(checkers.checkValidSimpleMove(2, 2, 1, 1))

    def test_checkValidJumpMoveXY(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidJumpMove(1, 1, 3, 3, 'H'))

    def test_checkValidJumpMoveXplusYplus(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidJumpMove(3, 3, 1, 1, 'H'))

    def test_checkValidJumpMoveXYplus(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidJumpMove(3, 3, 1, 5, 'H'))

    def test_checkValidJumpMoveXplusY(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidJumpMove(3, 3, 5, 5, 'H'))

    def test_checkValidJumpMoveXYHuman(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(1, 1, 3, 3, 'H'))

    def test_checkValidJumpMoveXplusYplusHuman(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertTrue(checkers.checkValidEatMove(3, 3, 1, 1, 'H'))

    def test_checkValidJumpMoveXYplusHuman(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertTrue(checkers.checkValidEatMove(3, 3, 1, 5, 'H'))

    def test_checkValidJumpMoveXplusYHuman(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(3, 3, 5, 5, 'H'))

    def test_checkValidJumpMoveXYComp(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(1, 1, 3, 3, 'C'))

    def test_checkValidJumpMoveXplusYplusComp(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(3, 3, 1, 1, 'C'))

    def test_checkValidJumpMoveXYplusComp(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(3, 3, 1, 5, 'C'))

    def test_checkValidJumpMoveXplusYComp(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidEatMove(3, 3, 5, 5, 'C'))

    def test_checkValidPieceHuman(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertTrue(checkers.checkValidPiece(5, 1, 'H'))

    def test_checkInvalidPieceComputer(self):
        checkers = Checkers()
        checkers.initializeGame()
        self.assertFalse(checkers.checkValidPiece(1, 1, 'C'))

    def test_checkInvalidPieceIncorrectUserComputer(self):
        checkers = Checkers()
        checkers.initializeGame()
        checkers.printBoard()
        self.assertFalse(checkers.checkValidPiece(1, 1, 'H'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCheckers)
    unittest.TextTestRunner(verbosity=0).run(suite)