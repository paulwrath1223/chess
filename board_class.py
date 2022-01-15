"""
Board class
"""
# imports
import board_class
from piece_class import Piece
from player_class import Player

# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


class Board:

    def __init__(self):
        """ Constructor
        """
        self.players = []
        self.players.append(Player(True))
        self.players.append(Player(False))
        self.turn_white = True
        self.game_over = False  # checkmate has occurred?
        self.current_move = 1

    def __repr__(self):
        board_string = ""
        for y in range(7, -1, -1):
            board_string += (str(y + 1) + " | ")
            for x in range(8):
                piece = self.find_piece_by_coordinate((x, y))
                # print(f"{x},{y}: {piece}")
                if type(piece) is Piece:
                    if (x + y) % 2 == 0:
                        checkered = "█"
                    else:
                        checkered = " "

                    board_string += R if piece.white else B
                    board_string += piece.figure_kind + W + checkered
                else:
                    # board_string += ". "

                    if (x + y) % 2 == 0:
                        board_string += " █"
                    else:
                        board_string += "  "

            board_string += "\n"
        board_string += "    a|b|c|d|e|f|g|h"
        return board_string

    def toggle_player(self):
        self.turn_white = not self.turn_white

    def print_board(self):
        # TODO: highlight possible moves
        board_string = ""
        for y in range(7, -1, -1):
            board_string += (str(y + 1) + " | ")
            for x in range(8):
                piece = self.find_piece_by_coordinate((x, y))
                # print(f"{x},{y}: {piece}")
                if type(piece) is Piece:
                    board_string += P if piece.white else G
                    board_string += piece.figure_kind + " " + W
                else:
                    if x + y % 2 == 0:
                        board_string += "\219\219"
                    else:
                        board_string += "  "
            board_string += "\n"
        board_string += "    a|b|c|d|e|f|g|h"
        return board_string

    def find_piece_by_coordinate(self, coordinate: ()):
        """Finds if coordinate is occupied or if there is a piece
        :param coordinate: (x, y)
        :return: class Piece if occupied or None if not
        """
        for player in self.players:
            for piece in player.pieces:
                if piece.get_pos() == coordinate:
                    return piece

    def within_grid(self, coords: ()) -> bool:
        return 0 <= coords[0] <= 8 and 0 <= coords[1] <= 8

    def find_possible_moves(self, piece: Piece) -> []:
        print(piece)
        possible_move_array = []
        if piece.figure_kind == "P":
            self.pawn_possible_moves(piece, possible_move_array)
        elif piece.figure_kind == "N":
            self.knight_possible_moves(piece, possible_move_array)
        return possible_move_array

    def figure_take_or_move_check(self, possible_move_array: [], coords: []) -> None:
        if self.within_grid(coords):
            piece_to_take = self.find_piece_by_coordinate(coords)
            if piece_to_take is None or piece_to_take.get_color is self.turn_white:
                possible_move_array.append(coords)

    def pawn_possible_moves(self, piece: Piece, possible_move_array) -> None:
        y_increment = 1 if piece.white else -1

        """TODO:
        - need to add case for en passant
        - check if by moving King gets in check
        - 
        """
        self.pawn_take_check(possible_move_array, (piece.coordinates[0] - 1, piece.coordinates[1] + y_increment))
        self.pawn_take_check(possible_move_array, (piece.coordinates[0] + 1, piece.coordinates[1] + y_increment))
        if self.pawn_move_check(possible_move_array,
                                (piece.coordinates[0], piece.coordinates[1] + y_increment)) and not piece.moved:
            self.pawn_move_check(possible_move_array, (piece.coordinates[0], piece.coordinates[1] + 2 * y_increment))
            #return possible_move_array not neccesary

    def pawn_move_check(self, possible_move_array: [], coords: []) -> bool:
        if self.within_grid(coords) and self.find_piece_by_coordinate(coords) is None:
            possible_move_array.append(coords)
            return True

    def pawn_take_check(self, possible_move_array: [], coords: []) -> None:
        if self.within_grid(coords):
            piece = self.find_piece_by_coordinate(coords)
            if type(piece) is Piece and piece.get_color() is not self.turn_white: # I cannot read what the fuck this line means
                possible_move_array.append(coords)

    def knight_possible_moves(self, piece:Piece, possible_move_array: []) -> None:
        for x in (-2, -1, 1, 2):
            for i in (-1, 1):
                y = (3 - abs(x))*i
                self.figure_take_or_move_check(possible_move_array, (piece.coordinates[0] + x, piece.coordinates[1]+y))

