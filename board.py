from enum import Enum

RANKS = FILES = 8


class SquareColor(Enum):
    WHITE = 0
    BLACK = 1


class Pieces(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    KING = 3
    QUEEN = 4
    ROOK = 5
    EMPTY = 6


class Board:

    class Square:
        def __init__(self, color, piece=Pieces.EMPTY):
            self.__color = color
            self.__piece = piece

        def get_color(self):
            return self.__color

        def get_piece(self):
            return self.__piece

        def set_piece(self, piece):
            self.__piece = piece
            return self.__piece

    def __init__(self):
        self.squares = [[None] * RANKS for f in range(FILES)]
        self.init_square_colors()
        self.init_place_pieces()

    def init_place_pieces(self):
        black_back_rank = 0
        black_second_rank = 1
        white_back_rank = RANKS - 1
        white_second_rank = RANKS - 2
        piece_order = [Pieces.ROOK, Pieces.KNIGHT, Pieces.BISHOP,
                       Pieces.QUEEN, Pieces.KING, Pieces.BISHOP,
                       Pieces.KNIGHT, Pieces.ROOK]
        for f, piece in enumerate(piece_order):
            self.squares[black_back_rank][f].set_piece(piece)
            self.squares[white_back_rank][f].set_piece(piece)
        for f in range(FILES):
            self.squares[white_second_rank][f].set_piece(Pieces.PAWN)
            self.squares[black_second_rank][f].set_piece(Pieces.PAWN)

    def init_square_colors(self):
        for rank in range(RANKS):
            for file in range(FILES):
                if rank % 2 == 0:
                    if file % 2 == 0:
                        self.squares[rank][file] = self.Square(
                            SquareColor.WHITE)
                    else:
                        self.squares[rank][file] = self.Square(
                            SquareColor.BLACK)
                else:
                    if file % 2 == 0:
                        self.squares[rank][file] = self.Square(
                            SquareColor.BLACK)
                    else:
                        self.squares[rank][file] = self.Square(
                            SquareColor.WHITE)

    def get_square(self, rank, file):
        return self.squares[rank][file]

    def print(self):
        for r in range(RANKS):
            rank = ''
            for f in range(FILES):
                rank += 'W' if self.squares[r][f].get_color(
                ) == SquareColor.WHITE else 'B'
                rank += ' '
            print(rank)