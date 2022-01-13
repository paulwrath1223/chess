"""
 Main file
"""

# imports
from board_class import Board

# global variables
_board: Board = Board()


def code_notation_to_chess_notation(a):
    b1 = a[1] + 1
    b2 = chr(a[1] + 97)
    b = (b1, b2)
    return b


def chess_notation_to_code_notation(a):
    b1 = a[1] - 1
    b2 = ord(a[1]) - 97
    b = (b1, b2)
    return b


print(_board)
