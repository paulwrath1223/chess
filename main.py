"""
 Main file
"""
# TODO: pawn transform to queen
# TODO: add coords to the top and right of the board
# TODO: https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
# TODO: game over condition
# TODO: check check not always working - check for king if he moves in check
# TODO: Castling
# TODO: Game History  -https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
# TODO: En Passant
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
    # TODO: add more commands: return move, restart game, end game
    while True:
        inp = input(prompt).lower()
        if inp == "/attack":
            print(board.print_board(board.find_attacked_tiles(board.turn_white)))
        elif inp == "0":
            return 0
        elif check_if_user_input_coords_exists(inp):
            coords = chess_notation_to_code_notation(inp)
            return coords
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
    while True:
        coords = user_input(board, f"{board.get_str_color()} (in form \"a1\") : ")
        piece = board.find_piece_by_coordinate(coords)
        if type(piece) is Piece:
            if piece.white == board.turn_white:
                break
            else:
                print("Please choose piece of your color.")
        else:
            print("There is no piece at the given coordinates. Please try again.")

    possible_moves = board.find_possible_moves(piece)
    print(board.print_board(possible_moves))
    while True:
        coords = user_input(board, f"Move {piece.figure_kind} at {code_notation_to_chess_notation(coords)} to "
                                   f"(in form \"a1\", 0 to deselect) : ")
        if coords == 0:
            print("Piece deselected4444444444444.\n")  # is 44444444444444 on purpose
            return move_piece(board)
        if coords in possible_moves:
            take_piece(board, coords)
            piece.set_pos(coords)
            board.toggle_player()
            return
        else:
            print("This move is not possible. Please try again.\n")


def take_piece(board, coords) -> None:
    piece_to_take = board.find_piece_by_coordinate(coords)
    if type(piece_to_take) is Piece:
        i = 1 if board.turn_white else 0
        board.players[i].pieces.remove(piece_to_take)


def start():
    board: Board = Board()  # not global, will be passed as a param to other functions

    # game loop
    while not board.game_over:
        print(board)
        print("Turn " + str(board.current_move) + ". ")
        move_piece(board)


start()
