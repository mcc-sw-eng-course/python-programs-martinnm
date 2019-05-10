import random

class Checkers:

    def __init__(self):
        self.COLS = 8
        self.ROWS = 8
        self.human = "W"
        self.computer = "B"
        self.eatenPiecesH = []
        self.eatenPiecesC = []
        self.board = [["-" for i in range(self.COLS)] for j in range(self.ROWS)]
        self.doubleTurn = False
        self.playerWon = ""

    def initializeGame(self):
        for i in range(0, 3):
            for j in range(len(self.board[i])):
                if i%2 == 0 and j%2 == 0:
                    self.board[i][j] = self.computer
                elif i%2 != 0 and j%2 != 0:
                    self.board[i][j] = self.computer
        for i in range(5, 8):
            for j in range(len(self.board[i])):
                if i%2 == 0 and j%2 == 0:
                    self.board[i][j] = self.human
                elif i%2 != 0 and j%2 != 0:
                    self.board[i][j] = self.human

    def printBoard(self):
        print("   ", end= '')
        for k in range(len(self.board)):
            print(str(k) + " ", end='')
        print()
        for i in range(len(self.board)):
            print(str(i) + ": ", end='')
            for j in range(len(self.board[i])):
                print(self.board[i][j] + " ", end='')
            print()

    def movePiece(self, player):
        isPieceValid = False
        while not isPieceValid:
            if player == 'H':
                coordiantesSelectPieceInput = input("Type coordinates of the piece you want to move: example (x, y): ")
                coordiantesSelectPieceX = int(coordiantesSelectPieceInput.split(",")[0])
                coordiantesSelectPieceY = int(coordiantesSelectPieceInput.split(",")[1])
                print("Coordinates Piece: " + str(coordiantesSelectPieceX) + ", " + str(coordiantesSelectPieceY))
            else:
                coordinates = self.computerTurn()
                coordiantesSelectPieceX = coordinates[0]
                coordiantesSelectPieceY = coordinates[1]
                print("Coordinates Piece: " + str(coordiantesSelectPieceX) + ", " + str(coordiantesSelectPieceY))
            isPieceValid = self.checkValidPiece(coordiantesSelectPieceX, coordiantesSelectPieceY, player)
            print(isPieceValid)
        isMoveValidEat = False
        isMoveValidJump = False
        isMoveValidSimple = False
        while not isMoveValidEat and not isMoveValidJump and not isMoveValidSimple:
            if player == 'H':
                coordiantesSelectPlaceInput = input("Type coordinates of the place you want to move: example (x, y): ")
                coordiantesSelectPlaceX = int(coordiantesSelectPlaceInput.split(",")[0])
                coordiantesSelectPlaceY = int(coordiantesSelectPlaceInput.split(",")[1])
                print("Coordinates Place: " + str(coordiantesSelectPlaceX) + ", " + str(coordiantesSelectPlaceY))
            else:
                coordinates = self.computerTurn()
                coordiantesSelectPlaceX = coordinates[0]
                coordiantesSelectPlaceY = coordinates[1]
                print("Coordinates Place: " + str(coordiantesSelectPlaceX) + ", " + str(coordiantesSelectPlaceY))
            isMoveValidEat = self.checkValidEatMove(coordiantesSelectPlaceX, coordiantesSelectPlaceY,
                                                    coordiantesSelectPieceX, coordiantesSelectPieceY, player)
            print("Eat Move: " + str(isMoveValidEat))
            isMoveValidJump = self.checkValidJumpMove(coordiantesSelectPlaceX, coordiantesSelectPlaceY,
                                                    coordiantesSelectPieceX, coordiantesSelectPieceY, player)
            print("Jump Move: " + str(isMoveValidJump))
            isMoveValidSimple = self.checkValidSimpleMove(coordiantesSelectPlaceX, coordiantesSelectPlaceY,
                                                    coordiantesSelectPieceX, coordiantesSelectPieceY)
            print("Simple Move: " + str(isMoveValidSimple))
            if(isMoveValidEat):
                self.redrawBoard(coordiantesSelectPlaceX, coordiantesSelectPlaceY, coordiantesSelectPieceX,
                                 coordiantesSelectPieceY, player, "eat")
                self.doubleTurn = True
            elif (isMoveValidJump):
                self.redrawBoard(coordiantesSelectPlaceX, coordiantesSelectPlaceY, coordiantesSelectPieceX,
                                 coordiantesSelectPieceY, player, "jump")
                self.doubleTurn = False
            elif(isMoveValidSimple):
                self.redrawBoard(coordiantesSelectPlaceX, coordiantesSelectPlaceY, coordiantesSelectPieceX,
                                 coordiantesSelectPieceY, player, "simple")
                self.doubleTurn = False

    def checkValidPiece(self, x, y, player):
        if self.checkBoundaries(x, y):
            if((player == "C" and self.board[x][y] == 'B') or (player == "H" and self.board[x][y] == 'W')):
                if self.isPieceFree(x, y):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def savePieceToEat(self, x, y, player):
        if player == 'C':
            self.eatenPiecesC.append([x,y])
        else:
            self.eatenPiecesH.append([x,y])

    def checkValidEatMove(self, xPlace, yPlace, xPiece, yPiece, player):
        if self.checkBoundaries(xPlace, yPlace):
            if(self.board[xPlace][yPlace] == '-'):
                if(xPiece + 2 == xPlace and yPiece + 2 == yPlace):
                    if(player == 'H' and self.board[xPiece + 1][yPiece + 1] == self.computer):
                        self.savePieceToEat(xPiece + 1, yPiece + 1, 'C')
                        return True
                    elif (player == 'C' and self.board[xPiece + 1][yPiece + 1] == self.human):
                        self.savePieceToEat(xPiece + 1, yPiece + 1, 'H')
                        return True
                    else:
                        return False
                elif(xPiece - 2 == xPlace and yPiece + 2 == yPlace):
                    if (player == 'H' and self.board[xPiece - 1][yPiece + 1] == self.computer):
                        self.savePieceToEat(xPiece - 1, yPiece + 1, 'C')
                        return True
                    elif (player == 'C' and self.board[xPiece - 1][yPiece + 1] == self.human):
                        self.savePieceToEat(xPiece - 1, yPiece + 1, 'H')
                        return True
                    else:
                        return False
                elif(xPiece + 2 == xPlace and yPiece - 2 == yPlace):
                    if (player == 'H' and self.board[xPiece + 1][yPiece - 1] == self.computer):
                        self.savePieceToEat(xPiece + 1, yPiece - 1, 'C')
                        return True
                    elif (player == 'C' and self.board[xPiece + 1][yPiece - 1] == self.human):
                        self.savePieceToEat(xPiece + 1, yPiece - 1, 'H')
                        return True
                    else:
                        return False
                elif (xPiece - 2 == xPlace and yPiece - 2 == yPlace):
                    if (player == 'H' and self.board[xPiece - 1][yPiece - 1] == self.computer):
                        self.savePieceToEat(xPiece - 1, yPiece - 1, 'C')
                        return True
                    elif (player == 'C' and self.board[xPiece - 1][yPiece - 1] == self.human):
                        self.savePieceToEat(xPiece - 1, yPiece - 1, 'H')
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def checkValidJumpMove(self, xPlace, yPlace, xPiece, yPiece, player):
            if self.checkBoundaries(xPlace, yPlace):
                if(self.board[xPlace][yPlace] == '-'):
                    if(xPiece + 2 == xPlace and yPiece + 2 == yPlace):
                        if(player == 'H' and self.board[xPiece + 1][yPiece + 1] == self.human):
                            return True
                        elif (player == 'C' and self.board[xPiece + 1][yPiece + 1] == self.computer):
                            return True
                        else:
                            return False
                    elif(xPiece - 2 == xPlace and yPiece + 2 == yPlace):
                        if (player == 'H' and self.board[xPiece - 1][yPiece + 1] == self.human):
                            return True
                        elif (player == 'C' and self.board[xPiece - 1][yPiece + 1] == self.computer):
                            return True
                        else:
                            return False
                    elif(xPiece + 2 == xPlace and yPiece - 2 == yPlace):
                        if (player == 'H' and self.board[xPiece + 1][yPiece - 1] == self.human):
                            return True
                        elif (player == 'C' and self.board[xPiece + 1][yPiece - 1] == self.computer):
                            return True
                        else:
                            return False
                    elif (xPiece - 2 == xPlace and yPiece - 2 == yPlace):
                        if (player == 'H' and self.board[xPiece - 1][yPiece - 1] == self.human):
                            return True
                        elif (player == 'C' and self.board[xPiece - 1][yPiece - 1] == self.computer):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def checkValidSimpleMove(self, xPlace, yPlace, xPiece, yPiece):
        if self.checkBoundaries(xPlace, yPlace):
            if(self.board[xPlace][yPlace] == '-'):
                if(xPiece + 1 == xPlace and yPiece + 1 == yPlace):
                    return True
                elif(xPiece - 1 == xPlace and yPiece + 1 == yPlace):
                    return True
                elif(xPiece + 1 == xPlace and yPiece - 1 == yPlace):
                    return True
                elif (xPiece - 1 == xPlace and yPiece - 1 == yPlace):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def redrawBoard(self, xPlace, yPlace, xPiece, yPiece, player, move):
        if move == "simple":
            self.board[xPiece][yPiece] = '-'
            if player == "H":
                self.board[xPlace][yPlace] = self.human
            else:
                self.board[xPlace][yPlace] = self.computer
        elif move == "jump":
            self.board[xPiece][yPiece] = '-'
            if player == "H":
                self.board[xPlace][yPlace] = self.human
            else:
                self.board[xPlace][yPlace] = self.computer
        else:
            self.board[xPiece][yPiece] = '-'
            if player == "H":
                lastIndexC = len(self.eatenPiecesC) - 1
                x = self.eatenPiecesC[lastIndexC][0]
                y = self.eatenPiecesC[lastIndexC][1]
                self.board[xPlace][yPlace] = self.human
                self.board[x][y] = "-"
            else:
                lastIndexH = len(self.eatenPiecesH) - 1
                x = self.eatenPiecesH[lastIndexH][0]
                y = self.eatenPiecesH[lastIndexH][1]
                self.board[xPlace][yPlace] = self.computer
                self.board[x][y] = "-"

    def checkEndGame(self):
        print(len(self.eatenPiecesH))
        if(len(self.eatenPiecesC) == 12):
            self.playerWon = "Human"
            return True
        elif(len(self.eatenPiecesH) == 12):
            self.playerWon = "Computer"
            return True
        else:
            return False

    def computerTurn(self):
        coordinates = [0, 0]
        coordinates[0] = random.randint(0, 7)
        coordinates[1] = random.randint(0, 7)
        return coordinates

    def checkBoundaries(self, xPlace, yPlace):
        if xPlace >= 0 and xPlace < len(self.board):
            if yPlace >= 0 and yPlace < len(self.board):
                return True
            else:
                return False
        else:
            return False

    def isPieceFree(self, xPiece, yPiece):
        if yPiece == 0:
            if (self.board[xPiece + 1][yPiece + 1] != '-'):
                if (self.board[xPiece - 1][yPiece + 1] != '-'):
                    return False
                else:
                    return True
            else:
                return True
        elif yPiece == 7:
            if (self.board[xPiece + 1][yPiece - 1] != '-'):
                if (self.board[xPiece - 1][yPiece - 1] != '-'):
                    return False
                else:
                    return True
            else:
                return True
        elif xPiece == 0:
            if (self.board[xPiece + 1][yPiece + 1] != '-'):
                if (self.board[xPiece + 1][yPiece - 1] != '-'):
                    return False
                else:
                    return True
            else:
                return True

        elif xPiece == 7:
            if (self.board[xPiece - 1][yPiece + 1] != '-'):
                if (self.board[xPiece - 1][yPiece - 1] != '-'):
                    return False
                else:
                    return True
            else:
                return True

        else:
            if (self.board[xPiece + 1][yPiece + 1] != '-'):
                if (self.board[xPiece - 1][yPiece + 1] != '-'):
                    if (self.board[xPiece + 1][yPiece - 1] != '-'):
                        if (self.board[xPiece - 1][yPiece - 1] != '-'):
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
            else:
                return True


