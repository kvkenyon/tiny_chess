from enum import Enum
import pygame
import sprites


RANKS = FILES = 8
SQUARE_SIZE = 100


class SquareColor(Enum):
    WHITE = 0
    BLACK = 1


class PieceColor(Enum):
    LIGHT = 0
    DARK = 1


class Pieces(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    KING = 3
    QUEEN = 4
    ROOK = 5
    EMPTY = 6


class Piece:
    def __init__(self, kind, color=None):
        self.__kind = kind
        self.__color = color

    def get_color(self):
        return self.__color

    def get_kind(self):
        return self.__kind


class Board:
    class Square:
        def __init__(self, color, piece=Piece(kind=Pieces.EMPTY)):
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
        self.chess_pieces = sprites.ChessPieces()
        self.__init_square_colors()
        self.__init_place_pieces()

    def __init_place_pieces(self):
        black_back_rank = 0
        black_second_rank = 1
        white_back_rank = RANKS - 1
        white_second_rank = RANKS - 2
        piece_order = [Pieces.ROOK, Pieces.KNIGHT, Pieces.BISHOP,
                       Pieces.QUEEN, Pieces.KING, Pieces.BISHOP,
                       Pieces.KNIGHT, Pieces.ROOK]
        for f, piece in enumerate(piece_order):
            self.squares[black_back_rank][f] \
                .set_piece(Piece(kind=piece,
                                 color=PieceColor.DARK))
            self.squares[white_back_rank][f].set_piece(Piece(piece,
                                                             PieceColor.LIGHT))
        for f in range(FILES):
            self.squares[white_second_rank][f] \
                .set_piece(Piece(Pieces.PAWN,
                                 PieceColor.LIGHT))
            self.squares[black_second_rank][f] \
                .set_piece(Piece(Pieces.PAWN, PieceColor.DARK))

    def __init_square_colors(self):
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

    def draw(self):
        board_surface = pygame.Surface(
            (FILES * SQUARE_SIZE, RANKS * SQUARE_SIZE)) \
            .convert_alpha()

        black = pygame.Color(125, 135, 150)
        white = pygame.Color(232, 235, 239)

        for rank in range(RANKS):
            square_y = rank * SQUARE_SIZE
            for file in range(FILES):
                square = self.get_square(rank, file)
                square_x = file * SQUARE_SIZE
                color = white if square.get_color() \
                    == SquareColor.WHITE else black
                square_coordinates = (
                    square_x,
                    square_y,
                    SQUARE_SIZE,
                    SQUARE_SIZE)
                pygame.draw.rect(board_surface, color, square_coordinates)
                piece = square.get_piece()
                if piece.get_kind() == Pieces.KING:
                    light_king, dark_king = self.chess_pieces.get_kings(.3)
                    height, width = light_king.get_height(), \
                        light_king.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2
                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(light_king, (square_x + offset_x,
                                                        square_y + offset_y))
                    else:
                        board_surface.blit(dark_king, (square_x + offset_x,
                                                       square_y + offset_y))
                elif piece.get_kind() == Pieces.PAWN:
                    white_pawn, black_pawn = self.chess_pieces.get_pawns(.3)
                    height, width = white_pawn.get_height(), \
                        white_pawn.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2
                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(white_pawn, (square_x + offset_x,
                                                        square_y + offset_y))
                    else:
                        board_surface.blit(black_pawn, (square_x + offset_x,
                                                        square_y + offset_y))
                elif piece.get_kind() == Pieces.QUEEN:
                    white_queen, black_queen = \
                        self.chess_pieces.get_queens(.3)
                    height, width = white_queen.get_height(), \
                        white_queen.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2

                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(white_queen, (square_x + offset_x,
                                                         square_y + offset_y))
                    else:
                        board_surface.blit(black_queen, (square_x + offset_x,
                                                         square_y + offset_y))
                elif piece.get_kind() == Pieces.ROOK:
                    white_rook, black_rook = \
                        self.chess_pieces.get_rooks(.3)
                    height, width = white_rook.get_height(), \
                        white_rook.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2
                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(white_rook, (square_x + offset_x,
                                                        square_y + offset_y))
                    else:
                        board_surface.blit(black_rook, (square_x + offset_x,
                                                        square_y + offset_y))
                elif piece.get_kind() == Pieces.BISHOP:
                    white_bishop, black_bishop = \
                        self.chess_pieces.get_bishops(.3)
                    height, width = white_bishop.get_height(), \
                        white_bishop.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2
                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(white_bishop, (square_x + offset_x,
                                                          square_y + offset_y))
                    else:
                        board_surface.blit(black_bishop, (square_x + offset_x,
                                                          square_y + offset_y))
                elif piece.get_kind() == Pieces.KNIGHT:
                    white_knight, black_knight = \
                        self.chess_pieces.get_knights(.3)
                    height, width = white_knight.get_height(), \
                        white_knight.get_width()
                    offset_y = (SQUARE_SIZE - height) // 2
                    offset_x = (SQUARE_SIZE - width) // 2
                    if piece.get_color() == PieceColor.LIGHT:
                        board_surface.blit(white_knight, (square_x + offset_x,
                                                          square_y + offset_y))
                    else:
                        board_surface.blit(black_knight, (square_x + offset_x,
                                                          square_y + offset_y))
        return board_surface

    def print(self):
        for r in range(RANKS):
            rank = ''
            for f in range(FILES):
                square = self.squares[r][f]
                piece = square.get_piece()
                if piece != Pieces.EMPTY:
                    if piece == Pieces.KING:
                        rank += 'K'
                    elif piece == Pieces.KNIGHT:
                        rank += 'N'
                    elif piece == Pieces.BISHOP:
                        rank += 'B'
                    elif piece == Pieces.QUEEN:
                        rank += 'Q'
                    elif piece == Pieces.ROOK:
                        rank += 'R'
                    elif piece == Pieces.PAWN:
                        rank += 'P'
                else:
                    rank += 'W' if self.squares[r][f].get_color(
                        ) == SquareColor.WHITE else 'B'
                rank += ' '
            print(rank)
