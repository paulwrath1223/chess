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
                    board_string += P if piece.white else G
                    board_string += piece.figure_kind + " " + W
                else:
                    board_string += ". "
            board_string += "\n"
        board_string += "    a|b|c|d|e|f|g|h"
        return board_string

    def print_board(self):
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

    def find_piece_by_coordinate(self, coordinate: tuple):
        """Finds if coordinate is occupied or if there is a piece
        :param coordinate: (x, y)
        :return: class Piece
        """
        for player in self.players:
            for piece in player.pieces:
                if piece.get_pos() == coordinate:
                    return piece
    def within_grid(self, coords):
        if()

    def find_possible_moves(self, piece):
        possible_move_array = []
        if piece.figure_kind == "P":
            if piece.white:
                y_increment = 1
            else:
                y_increment = -1
            # TODO: Need to add case for en passant
            pawn_take_left_coords = (piece.coordinates[0] - 1, piece.coordinates[1] + y_increment)
            if (self.find_piece_by_coordinate(pawn_take_left_coords) is not None and
                    pawn_take_left_coords[0]<8):
                possible_move_array.append(pawn_take_left_coords)

            pawn_take_right_coords = (piece.coordinates[0] + 1, piece.coordinates[1] + y_increment)
            if (self.find_piece_by_coordinate(pawn_take_right_coords) is not None and
                    self.find_piece_by_coordinate(pawn_take_right_coords) != "Out of bounds"):
                possible_move_array.append(pawn_take_right_coords)

            pawn_advance_one_coords = (piece.coordinates[0], piece.coordinates[1] + y_increment)
            if (self.find_piece_by_coordinate(pawn_advance_one_coords) is None and
                    self.find_piece_by_coordinate(pawn_advance_one_coords) != "Out of bounds"):
                possible_move_array.append(pawn_advance_one_coords)

            pawn_advance_two_coords = (piece.coordinates[0], piece.coordinates[1] + (2 * y_increment))
            if (self.find_piece_by_coordinate(pawn_advance_two_coords) is None and
                    self.find_piece_by_coordinate(pawn_advance_one_coords) is None and not piece.moved):
                possible_move_array.append(pawn_advance_two_coords)
        return possible_move_array
