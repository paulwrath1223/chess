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
            print(board.print_board_2(board.find_attacked_tiles(board.turn_white)))
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
    print(board.print_board_2(possible_moves))
    while True:
        coords = user_input(board, f"Move {piece.figure_kind} at {code_notation_to_chess_notation(coords)} to "
                                   f"(in form \"a1\", 0 to deselect) : ")
        if coords == 0:
            print("Piece deselected.\n")
            return move_piece(board)
        if coords in possible_moves:
            take_piece(board, coords)
            piece.set_pos(coords)
            check_for_checkmate(board)
            board.increase_current_move()
            board.toggle_player()
            return
        else:
            print("This move is not possible. Please try again.\n")


def take_piece(board, coords) -> None:
    piece_to_take = board.find_piece_by_coordinate(coords)
    if type(piece_to_take) is Piece:
        i = 1 if board.turn_white else 0
        board.players[i].pieces.remove(piece_to_take)


# TODO: Not working, Vojta is working on it
def check_for_checkmate(board: Board):
    i = 1 if board.turn_white else 0
    all_possible_moves = []
    for piece in board.players[i].pieces:
        all_possible_moves += board.find_possible_moves(piece)
    if len(all_possible_moves) == 0:
        if board.players[i].pieces[0].coordinates in board.find_attacked_tiles(board.turn_white):
            print("Check Mate")
        else:
            print("Stale Mate")

def start():
    board: Board = Board()  # not global, will be passed as a param to other functions
    print(board.an_game_to_an_move_list("17 1999.11.20 1-0 2851 None 51 date_false result_false welo_false belo_true edate_false setup_false fen_false result2_false oyrange_false blen_false ### W1.e4 B1.c6 W2.d4 B2.d5 W3.exd5 B3.cxd5 W4.Bd3 B4.Nc6 W5.c3 B5.Nf6 W6.Bf4 B6.Bg4 W7.Qb3 B7.Qd7 W8.Nd2 B8.e6 W9.Ngf3 B9.Bd6 W10.Ne5 B10.Bxe5 W11.dxe5 B11.Nh5 W12.Be3 B12.a6 W13.h3 B13.Nxe5 W14.Bf1 B14.Bf5 W15.g4 B15.Nd3+ W16.Bxd3 B16.Bxd3 W17.gxh5 B17.Rc8 W18.Rg1 B18.f6 W19.h6 B19.g6 W20.O-O-O B20.d4 W21.Bxd4 B21.Ke7 W22.Nf3 B22.e5 W23.Rxd3 B23.exd4 W24.Re1+ B24.Kf8 W25.Rxd4 B25.Qc6 W26.Qb4+ "))
    # game loop
    while not board.game_over:
        print(board.print_board_2())
        print("Turn " + str(board.current_move) + ". ")
        move_piece(board)


start()
