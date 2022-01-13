"""
 Main file
"""

# imports
from board_class import Board

# global variables
_board: Board = Board()


def code_notation_to_chess_notation(a):
    b1 = a[1] + 1
    b2 = chr(a[0] + 97)
    b = (b2, b1)
    return b


def chess_notation_to_code_notation(a):
    b1 = int(a[1]) - 1
    b2 = ord(a[0]) - 97
    b = (b2, b1)
    return b


print(_board)

gameOver = False   # checkmate has occurred?
currentMove = 1
whitesTurn = True   # true means that it is currently white's move
while not gameOver:
    print("Turn " + str(currentMove) + ". ")
    if whitesTurn:
        pieceToBeMoved = input("enter the coordinates of the piece you would like to move: (in form \"a1\") : ").lower()
        coordPieceToBeMoved = chess_notation_to_code_notation(
            (pieceToBeMoved[0],pieceToBeMoved[1]))
        print(coordPieceToBeMoved)