

class Piece:
    def __init__(self, coordinates, white):
        """
        :param coordinates: (0,0) is bottom left white rook, (1,0) is white knight
        :param white: on white team? boolean. true = white, false = black
        """
        self.coordinates = coordinates
        self.white = white   # creates a new empty list for each dog

    def set_pos(self, coordinates):
        self.coordinates = coordinates

    def get_pos(self):
        return self.coordinates
