

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
        self.moved = False  # has this piece moved before
        self.value = value  # value of the figure kind, pawn is 1, rook is 5...

    def __repr__(self):
        color = "white" if self.white else "black"
        return f"({self.figure_kind}, {self.coordinates}, {color})"

    def set_pos(self, coordinates):
        self.coordinates = coordinates
        self.moved = True

    def get_pos(self):
        return self.coordinates

    def get_symbol(self):
        pieces = ''.join(chr(9812 + x) for x in range(12))
        start_index = 0 if self.white else 6
        if self.figure_kind == "K":
            return pieces[start_index]
        if self.figure_kind == "Q":
            return pieces[start_index + 1]
        if self.figure_kind == "R":
            return pieces[start_index + 2]
        if self.figure_kind == "B":
            return pieces[start_index + 3]
        if self.figure_kind == "N":
            return pieces[start_index + 4]
        if self.figure_kind == "P":
            return pieces[start_index + 5]


