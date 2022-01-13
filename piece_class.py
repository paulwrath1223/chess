

class Piece:
    def __init__(self, figure_kind, coordinates, white, value):
        """
        :param figure_kind: King = K, Queen = Q, Bishop = B, Knight = N, Rook = R, Pawn = P
        :param coordinates: (0,0) is bottom left white rook, (1,0) is white knight
        :param white: on white team? boolean. true = white, false = black
        """
        self.figure_kind = figure_kind
        self.coordinates = coordinates
        self.white = white
        self.value = value # value of the figure kind, pawn is 1, rook is 5...

    def __repr__(self):
        return f"({self.figure_kind}, {self.coordinates}, {self.white}, {self.value})"

    # TODO: is setter and getter necessary?
    def set_pos(self, coordinates):
        self.coordinates = coordinates

    def get_pos(self):
        return self.coordinates