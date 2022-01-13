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
        print(self.players)
        self.turn_white = True

    def __repr__(self):
        board_string = ""
        for y in range(7, -1, -1):
            for x in range(8):
                piece = self.find_piece_by_coordinate([x, y])
                # print(f"{x},{y}: {piece}")
                if piece is not None:
                    board_string += P if piece.white else G
                    board_string += piece.figure_kind + " " + W
                else:
                    board_string += ". "
            board_string += "\n"
        return board_string

    def find_piece_by_coordinate(self, coordinate: list) -> Piece:
        """Finds if coordinate is occupied or if there is a piece
        :param coordinate: [x, y]
        :return: class Piece
        """
        for player in self.players:
            for piece in player.pieces:
                if piece.get_pos() == coordinate:
                    return piece
