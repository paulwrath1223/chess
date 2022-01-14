"""
Player class
"""

# imports
from piece_class import Piece


class Player:

    def __init__(self, white: bool, time_left: float = -1):
        """
        constructor
        :param white: true if player is white, false if player is black
        :param time_left: time in milliseconds, default -1, not every game timed
        """
        self.pieces = []  # list of pieces king is on index 0
        self.is_in_check = False
        self.white = white
        self.time_left = time_left  # float in milliseconds
        self.pieces_init()

    def pieces_init(self) -> None:
        """ Generetes pieces for white, if the player is black, moves the pieces.
        :return: None
        """
        self.pieces.append(Piece("K", (4, 0), self.white, 0))
        self.pieces.append(Piece("Q", (3, 0), self.white, 9))
        self.pieces.append(Piece("R", (0, 0), self.white, 5))
        self.pieces.append(Piece("R", (7, 0), self.white, 5))
        self.pieces.append(Piece("B", (2, 0), self.white, 3))
        self.pieces.append(Piece("B", (5, 0), self.white, 3))
        self.pieces.append(Piece("N", (1, 0), self.white, 3))
        self.pieces.append(Piece("N", (6, 0), self.white, 3))
        for i in range(8):
            self.pieces.append(Piece("P", (i, 1), self.white, 1))

        if not self.white:
            for piece in self.pieces:
                piece.coordinates = (piece.coordinates[0], 7 - piece.coordinates[1])

