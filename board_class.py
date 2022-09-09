"""
Board class
"""
# imports
from piece_class import Piece
from player_class import Player

# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
ORANGE = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
BOLD = '\033[1m'
END_BOLD = '\033[0m'
UNDERLINE = "\033[4m"
END_UNDERLINE = "\033[0m"


class Board:

    def __init__(self):
        self.players = []
        self.players.append(Player(True))
        self.players.append(Player(False))
        self.turn_white = True
        self.score = 0
        self.game_over = False  # checkmate has occurred?
        self.current_move = 1
        self.move_history = []

    def __repr__(self):
        board_string = ""
        for y in range(7, -1, -1):
            board_string += (str(y + 1) + " |")
            for x in range(8):
                piece = self.find_piece_by_coordinate((x, y))
                # print(f"{x},{y}: {piece}")
                if type(piece) is Piece:
                    checkered = "█" if (x + y) % 2 == 0 else " "
                    board_string += checkered
                    board_string += R if piece.white else B
                    board_string += piece.get_symbol() + W + checkered
                else:
                    # board_string += ". "

                    board_string += "███" if (x + y) % 2 == 0 else "   "

            board_string += "\n"
        board_string += "    a |b |c |d |e |f |g |h"
        return board_string

    def toggle_player(self):
        self.turn_white = not self.turn_white

    def increase_current_move(self):
        if not self.turn_white:
            self.current_move += 1

    def get_str_color(self):
        return self.color_text("White" if self.turn_white else "Black", self.turn_white)

    def print_board(self, possible_moves=[]) -> str:
        """
        Prints board while displaying possible moves
        :param possible_moves:
        :return: str board to print
        """
        if possible_moves is None:
            possible_moves = []
        board_string = ""
        for y in range(7, -1, -1):
            board_string += (str(y + 1) + " |")
            for x in range(8):
                piece = self.find_piece_by_coordinate((x, y))
                possible_move = (x, y) in possible_moves
                # print(f"{x},{y}: {piece}")
                checkered = "█" if (x + y) % 2 == 0 else " "
                if type(piece) is Piece:
                    board_string += checkered
                    board_string += R if piece.white else B
                    if possible_move:
                        board_string += BOLD + UNDERLINE + piece.get_symbol() + END_UNDERLINE + END_BOLD
                    else:
                        board_string += piece.get_symbol()
                    board_string += W + checkered
                else:
                    # board_string += ". "
                    if possible_move:
                        board_string += checkered
                        board_string += R if self.turn_white else B
                        board_string += "." + W + checkered
                    else:
                        board_string += "███" if (x + y) % 2 == 0 else "   "

            board_string += "\n"
        board_string += "    a | b | c | d | e | f | g | h"
        return board_string

    def print_board_2(self, possible_moves=[]) -> str:
        board_string = "      a    b    c    d    e    f    g    h\n"
        board_string += "  ┌────┬────┬────┬────┬────┬────┬────┬────┐\n"
        for y in range(7, -1, -1):
            board_string += f"{y+1} "
            for x in range(8):
                board_string += self.get_cell((x, y), possible_moves)
            if y > 0:
                board_string += f"│ {y+1} \n  ├────┼────┼────┼────┼────┼────┼────┼────┤\n"
            else:
                board_string += f"│ {y + 1} \n  └────┴────┴────┴────┴────┴────┴────┴────┘\n"
        board_string += "      a    b    c    d    e    f    g    h\n"
        return board_string

    def get_cell(self, coords: (), possible_moves: []) -> str:
        piece = self.find_piece_by_coordinate(coords)
        colorful_symbol = "│"+ 3*" "

        if type(piece) is Piece:
            if coords in possible_moves:
                colorful_symbol += UNDERLINE + self.color_text(piece.get_symbol(0), piece.white) + END_UNDERLINE + 3*" "
            else:
                colorful_symbol += self.color_text(piece.get_symbol(), piece.white) + 3*" "
        else:
            if coords in possible_moves:
                colorful_symbol += self.color_text("•", self.turn_white) + 2*"  "
            else:
                return "│ " + 6*" "
        return colorful_symbol

    def color_text(self, text, white: bool):
        color = R if white else B
        return color + text + W

    def find_piece_by_coordinate(self, coordinate: ()):
        """Finds if coordinate is occupied or if there is a piece and returns it
        :param coordinate: (x, y)
        :return: class Piece if occupied or None if not
        """
        for player in self.players:
            for piece in player.pieces:
                if piece.get_pos() == coordinate:
                    return piece

    def within_grid(self, coords: ()) -> bool:
        return 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7

    def an_game_to_an_move_list(self, an_game):
        """
        :param an_game: a string representing a chess game in algebraic notation (sample in readme)
        :return: a 2d array containing every move in "AN" (algebraic notation) each turn has a list of 2 moves,
        one for each player/team
        """
        game_data = an_game.split("###")[1]
        first_layer_list = game_data.split(" W")
        first_layer_list.pop(0)
        list_out = []
        for raw_move_pair in first_layer_list:
            move_pair_list = raw_move_pair.split(" B", 1)
            for i in range(len(move_pair_list)):
                move_pair_list[i] = move_pair_list[i].split(".")[1]
            list_out.append(move_pair_list)
        list_out.pop(0)
        return list_out

    def find_attacked_tiles(self, white):
        all_possible_moves = []
        i = 0 if white else 1
        for piece in self.players[i].pieces:
            all_possible_moves += self.find_possible_moves(piece, True)
        return list(set(all_possible_moves))  # removes duplicates

    def find_possible_moves(self, piece: Piece, attack: bool = False) -> []:
        """
        Finds possible move of given piece
        :param piece:
        :param attack: specify, if you want only tile which are under attack
        :return: [] of possible moves
        """
        # print(piece)
        possible_move_array = []
        if piece.figure_kind == "P":
            self.pawn_possible_moves(piece, possible_move_array, attack)
        elif piece.figure_kind == "N":
            self.knight_possible_moves(piece, possible_move_array, attack)
        elif piece.figure_kind == "B":
            self.bishop_possible_moves(piece, possible_move_array, attack)
        elif piece.figure_kind == "R":
            self.rook_possible_moves(piece, possible_move_array, attack)
        elif piece.figure_kind == "Q":
            self.queen_possible_moves(piece, possible_move_array, attack)
        elif piece.figure_kind == "K":
            self.king_possible_moves(piece, possible_move_array, attack)
        return possible_move_array

    def figure_take_or_move_check(self, piece, possible_move_array: [], coords: [], attack: bool) -> bool:
        """
        If piece can move to coords adds them in possible_move_array
        :param attack: true if you want to get all attacked tiles
        :param piece: current Piece
        :param possible_move_array:
        :param coords: (x, y)
        :return: bool if piece can continue in given direction
        """
        if self.within_grid(coords):
            piece_to_take = self.find_piece_by_coordinate(coords)
            if piece_to_take is None:
                if attack:
                    possible_move_array.append(coords)
                    return True
                elif not self.will_king_be_in_check(piece, coords):
                    possible_move_array.append(coords)
                    return True
            elif piece_to_take.white is not piece.white:
                # print(f"Piece to take: {piece_to_take}, coords: {coords}, turn: {self.get_str_color()}")
                #if not self.will_king_be_in_check(piece, coords):
                if piece.figure_kind == "K" and not attack:
                   # if piece_to_take.coordinates in self.find_attacked_tiles(piece.white):
                        return
                possible_move_array.append(coords)

    def pawn_possible_moves(self, piece: Piece, possible_move_array, attack: bool) -> None:
        y_increment = 1 if piece.white else -1

        self.pawn_take_check(piece, possible_move_array, (piece.coordinates[0] - 1, piece.coordinates[1] + y_increment),
                             attack)
        self.pawn_take_check(piece, possible_move_array, (piece.coordinates[0] + 1, piece.coordinates[1] + y_increment),
                             attack)
        if not attack:
            if self.pawn_move_check(piece, possible_move_array,
                                    (piece.coordinates[0], piece.coordinates[1] + y_increment)) and not piece.moved:
                self.pawn_move_check(piece, possible_move_array,
                                     (piece.coordinates[0], piece.coordinates[1] + 2 * y_increment))

    def pawn_move_check(self, piece: Piece, possible_move_array: [], coords: []) -> bool:
        if self.within_grid(coords) and self.find_piece_by_coordinate(coords) is None:
            if not self.will_king_be_in_check(piece, coords):
                possible_move_array.append(coords)
                return True

    def pawn_take_check(self, piece: Piece, possible_move_array: [], coords: [], attack: bool = False) -> None:
        if self.within_grid(coords):
            piece_to_take = self.find_piece_by_coordinate(coords)
            if type(piece_to_take) is Piece and piece_to_take.white is not piece.white:
                if not self.will_king_be_in_check(piece, coords):
                    possible_move_array.append(coords)
            elif attack:
                possible_move_array.append(coords)

    def knight_possible_moves(self, piece: Piece, possible_move_array: [], attack: bool) -> None:
        for x in (-2, -1, 1, 2):
            for i in (-1, 1):
                y = (3 - abs(x)) * i
                self.figure_take_or_move_check(piece, possible_move_array,
                                               (piece.coordinates[0] + x, piece.coordinates[1] + y), attack)

    def bishop_possible_moves(self, piece: Piece, possible_move_array: [], attack: bool) -> None:
        for x in (-1, 1):
            for y in (-1, 1):
                i = 1
                while self.figure_take_or_move_check(piece, possible_move_array,
                                                     (piece.coordinates[0] + i * x, piece.coordinates[1] + i * y),
                                                     attack):
                    i += 1

    def rook_possible_moves(self, piece: Piece, possible_move_array: [], attack: bool) -> None:
        for x in (-1, 1):
            i = 1
            while self.figure_take_or_move_check(piece, possible_move_array,
                                                 (piece.coordinates[0] + i * x, piece.coordinates[1]), attack):
                i += 1
        for y in (-1, 1):
            i = 1
            while self.figure_take_or_move_check(piece, possible_move_array,
                                                 (piece.coordinates[0], piece.coordinates[1] + i * y), attack):
                i += 1

    def queen_possible_moves(self, piece: Piece, possible_move_array: [], attack) -> None:
        self.bishop_possible_moves(piece, possible_move_array, attack)
        self.rook_possible_moves(piece, possible_move_array, attack)

    def king_possible_moves(self, piece: Piece, possible_move_array: [], attack) -> None:
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                self.figure_take_or_move_check(piece, possible_move_array,
                                               (piece.coordinates[0] + x, piece.coordinates[1] + y), attack)

    def will_king_be_in_check(self, piece: Piece, coords_to_be_moved) -> bool:
        old_coords = piece.coordinates
        piece.coordinates = coords_to_be_moved
        i = 0 if self.turn_white else 1
        king_in_check = self.players[i].pieces[0].coordinates in self.find_attacked_tiles(not self.turn_white)
        piece.coordinates = old_coords
        return king_in_check
