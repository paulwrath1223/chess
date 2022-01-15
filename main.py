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
    # b = (b2, b1)
    b = str(b2) + str(b1)
    return b


def chess_notation_to_code_notation(a):
    b1 = int(a[1]) - 1
    b2 = ord(a[0]) - 97
    b = (b2, b1)
    return b


def user_input(board: Board, prompt: str) -> []:
    """
    Loop which asks user for input until it provides valid input
    :param board: board
    :param prompt: ask user question
    :return: returns valid input,
    """
    """ TODO: 
    - add more commands: help, deselect... return move, restart game, end game
    - 
    """
    while True:
        inp = input(prompt).lower()
        if check_if_user_input_coords_exists(inp):
            coords = chess_notation_to_code_notation(inp)
            return board.find_piece_by_coordinate(coords)
        else:
            print("We couldn't read that, please try again. \n")


def check_if_user_input_coords_exists(coords: str):
    if len(coords) == 2 and 96 < ord(coords[0]) < 105:
        try:
            y_coord = int(coords[1])
            if 0 < y_coord < 9:
                return coords
        except:
            pass


def select_move(maximum):
    while True:
        selected_move_str = input("which move would you like to execute? (0 to deselect current piece) : \n")
        try:
            selected_move_int = int(selected_move_str)
            if 0 <= selected_move_int <= maximum:
                return selected_move_int
            else:
                print("Not valid interval.")
        except:
            print("Must be a number.")
        print('If the selected piece is not the piece you wish to move, enter \'0\' to select a new piece.')


def move_piece(board):
    on_turn_color = "White" if board.turn_white else "Black"
    piece = user_input(board, f"{on_turn_color} (in form \"a1\") : ")
    while type(piece) is not Piece:
        print("there is no piece at the given coordinates, please try again.")
        piece = user_input(board, f"{on_turn_color} (in form \"a1\") : ")
        # todo check if the piece is of current player

    possible_moves = board.find_possible_moves(piece)
    for i, coord in enumerate(possible_moves):
        print(str(i + 1) + ": " + str(code_notation_to_chess_notation(coord)).replace("\'", ""))
    selected_move = select_move(len(possible_moves))
    if selected_move == 0:
        print("select a new piece")
        return move_piece(board)
    else:
        piece.set_pos(possible_moves[selected_move - 1])
        board.toggle_player()


def start():
    board: Board = Board()  # not global, will be passed as a param to other functions

    # game loop
    while not board.game_over:
        print(board)
        print("Turn " + str(board.current_move) + ". ")
        move_piece(board)


start()
