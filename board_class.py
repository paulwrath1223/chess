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

    def __repr__(self, ):
        board_string = ""
        for y in range(7, -1, -1):
            board_string += (str(y + 1) + " | ")
            for x in range(8):
                piece = self.find_piece_by_coordinate([x, y])
                # print(f"{x},{y}: {piece}")
                if type(piece) is Piece:
                    board_string += P if piece.white else G
                    board_string += piece.figure_kind + " " + W
                else:
                    board_string += ". "
            board_string += "\n"
        board_string += "    a|b|c|d|e|f|g|h"
        return board_string

    def find_piece_by_coordinate(self, coordinate: list):
        """Finds if coordinate is occupied or if there is a piece
        :param coordinate: [x, y]
        :return: class Piece or string "out of bounds"
        """
        # TODO: returns two different types, is it needed?
        for player in self.players:
            for piece in player.pieces:
                if piece.get_pos() == coordinate:
                    return piece
        return "Out of bounds"

    def find_possible_moves(self, piece):
        rows, cols = (8, 8)
        possibleMoveArray = [[False] * cols] * rows
        if piece.figure_kind == "P":
            if piece.white:
                yIncrement = 1
            else:
                yIncrement = -1
            # Need to add case for en passant
            pawnTakeLeftCoords = (piece.coordinates[0] - 1, piece.coordinates[1] + yIncrement)
            if (self.find_piece_by_coordinate(pawnTakeLeftCoords) is not None and
                    self.find_piece_by_coordinate(pawnTakeLeftCoords) != "Out of bounds"):
                possibleMoveArray[pawnTakeLeftCoords[0]][pawnTakeLeftCoords[1]] = True

            pawnTakeRightCoords = (piece.coordinates[0] + 1, piece.coordinates[1] + yIncrement)
            if (self.find_piece_by_coordinate(pawnTakeRightCoords) is not None and
                    self.find_piece_by_coordinate(pawnTakeRightCoords) != "Out of bounds"):
                possibleMoveArray[pawnTakeRightCoords[0]][pawnTakeRightCoords[1]] = True

            pawnAdvanceOneCoords = (piece.coordinates[0], piece.coordinates[1] + yIncrement)
            if (self.find_piece_by_coordinate(pawnAdvanceOneCoords) is None and
                    self.find_piece_by_coordinate(pawnAdvanceOneCoords) != "Out of bounds"):
                possibleMoveArray[pawnAdvanceOneCoords[0]][pawnAdvanceOneCoords[1]] = True

            pawnAdvanceTwoCoords = (piece.coordinates[0], piece.coordinates[1] + (2 * yIncrement))
            if (self.find_piece_by_coordinate(pawnAdvanceTwoCoords) is None and
                    self.find_piece_by_coordinate(pawnAdvanceOneCoords) is None and not piece.moved):
                possibleMoveArray[pawnAdvanceTwoCoords[0]][pawnAdvanceTwoCoords[1]] = True
