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

    def __init__(self) -> None:
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
                    board_string += R if piece.white else B
                    board_string += piece.figure_kind + " " + W
                else:
                    board_string += ". "
            board_string += "\n"
        board_string += "    a|b|c|d|e|f|g|h"
        return board_string

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
                    board_string += ". "
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
        if 0 <= coords[0] <= 8 and 0 <= coords[1] <= 8:
            return True

    def find_possible_moves(self, piece: Piece):
        if piece.figure_kind == "P":
            return self.pawn_possible_moves(piece)
        return []

    def pawn_possible_moves(self, piece: Piece):
        possible_move_array = []
        y_increment = 1 if piece.white else -1

        """TODO:
        - need to add case for en passant
        - check if by moving King gets in check
        - 
        """
        self.pawn_take_check(possible_move_array, (piece.coordinates[0] - 1, piece.coordinates[1] + y_increment))
        self.pawn_take_check(possible_move_array, (piece.coordinates[0] + 1, piece.coordinates[1] + y_increment))
        if self.pawn_move_check(possible_move_array, (piece.coordinates[0], piece.coordinates[1] + y_increment)) and not piece.moved:
            self.pawn_move_check(possible_move_array, (piece.coordinates[0], piece.coordinates[1] + 2 * y_increment))
        return possible_move_array

    def pawn_take_check(self, possible_move_array: [], coords: []) -> None:
        if self.within_grid(coords):
            piece = self.find_piece_by_coordinate(coords)
            if type(piece) is Piece and piece.get_color() is not self.turn_white:
                possible_move_array.append(coords)

    def pawn_move_check(self, possible_move_array: [], coords: []) -> bool:
        if self.within_grid(coords) and self.find_piece_by_coordinate(coords) is None:
            possible_move_array.append(coords)
            return True

