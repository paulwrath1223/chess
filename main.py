"""
 Main file
"""

# imports
from board_class import Board


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


def user_input(prompt: str) -> []:
    """
    Loop which asks user for input until it provides valid input
    :param prompt:
    :return: returns valid input,
    """
    """TODO
    - add more commands: help, deselect... return move, restart game, end game
    - 
    """
    while True:
        if not check_if_user_input_coords_exists(input(prompt).lower()):
            print("We couldn't read that, please try again. \n")


def check_if_user_input_coords_exists(coords: str):
    if len(coords) == 2:
        if 96 < ord(coords[0]) < 105:
            try:
                y_coord = int(coords[1])
                if 0 < y_coord < 9:
                    return coords
            except:
                pass

def start():
    board: Board = Board()  # not global, will be passed as a param to other functions

    # game loop
    while not board.game_over:
        print(board)
        print("Turn " + str(board.current_move) + ". ")
        if board.turn_white:
            on_turn_color =  "White" if board.turn_white else "Black"
            piece_to_be_moved = user_input(f"{on_turn_color} (in form \"a1\") : ")
            coord_piece_to_be_moved = chess_notation_to_code_notation((piece_to_be_moved[0], piece_to_be_moved[1]))
            piece = board.find_piece_by_coordinate(coord_piece_to_be_moved)
            for coord in board.find_possible_moves(piece):
                print(coord)


start()
