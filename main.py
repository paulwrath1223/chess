"""
 Main file
"""
# TODO: Delete pieces after they have been taken
# imports
from board_class import Board
from piece_class import Piece


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
    """ TODO: 
    - add more commands: help, deselect... return move, restart game, end game
    - 
    """
    while True:
        inp = input(prompt).lower()
        if not check_if_user_input_coords_exists(inp):
            print("We couldn't read that, please try again. \n")
        else:
            return inp


def check_if_user_input_coords_exists(coords: str):
    if len(coords) == 2 and 96 < ord(coords[0]) < 105:
        try:
            y_coord = int(coords[1])
            if 0 < y_coord < 9:
                return coords
        except:
            pass


def select_move(maximum):
    selected_move_str = input("which move would you like to execute? (0 to deselect current piece) : \n")
    try:
        selected_move_int = int(selected_move_str)

    except:
        selected_move_int = -1
        print("Must be a number")
    if 0 <= selected_move_int <= maximum:
        return selected_move_int
    else:
        print('\nPlease enter a number representing which move you would like to execute. \n'
              'If the selected piece is not the piece you wish to move, enter \'0\' to select a new piece.')
        return select_move(maximum)


def move_piece(board):
    on_turn_color = "White" if board.turn_white else "Black"
    piece_to_be_moved = user_input(f"{on_turn_color} (in form \"a1\") : ")
    coord_piece_to_be_moved = chess_notation_to_code_notation((piece_to_be_moved[0], piece_to_be_moved[1]))
    piece = board.find_piece_by_coordinate(coord_piece_to_be_moved)
    while piece is None:
        print("there is no piece at the given coordinates, please try again.")
        piece_to_be_moved = user_input(f"{on_turn_color} (in form \"a1\") : ")
        coord_piece_to_be_moved = chess_notation_to_code_notation((piece_to_be_moved[0], piece_to_be_moved[1]))
        piece = board.find_piece_by_coordinate(coord_piece_to_be_moved)

    counter = 0
    possible_moves = board.find_possible_moves(piece)
    for coord in possible_moves:
        counter += 1
        print(str(counter) + ": " + str(code_notation_to_chess_notation(coord)).replace("\'", ""))
    selected_move = select_move(counter)
    if selected_move == 0:
        print("select a new piece")
        return move_piece(board)
    else:
        piece.set_pos(possible_moves[selected_move - 1])


def start():
    board: Board = Board()  # not global, will be passed as a param to other functions

    # game loop
    while not board.game_over:
        print(board)
        print("Turn " + str(board.current_move) + ". ")
        move_piece(board)



start()
