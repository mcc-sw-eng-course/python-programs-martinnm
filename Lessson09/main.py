from checkers import *

def main():
    checkers = Checkers()
    checkers.initializeGame()
    checkers.printBoard()
    while(not checkers.checkEndGame()):
        print("Human Turn")
        checkers.movePiece("H")
        checkers.printBoard()
        while(checkers.doubleTurn):
            print("Human Turn")
            checkers.movePiece("H")
            checkers.printBoard()
        print("Computer Turn")
        checkers.movePiece("C")
        checkers.printBoard()
        while (checkers.doubleTurn):
            print("Computer Turn")
            checkers.movePiece("C")
            checkers.printBoard()
    print("Game ended!" + checkers.playerWon + " won!")


if __name__ == '__main__':
   main()