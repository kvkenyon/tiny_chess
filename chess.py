"""The game loop for Tiny Chess
"""
import pygame
import board
import sprites


class TinyChess:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.size = self.is_running = True
        self.clock = None
        self.display_surface = None
        self.board_surface = None
        self.board = board.Board()
        self.chess_pieces = None

    def draw_board(self):
        square_size = 100
        board_surface = pygame.Surface(
            (board.FILES * square_size, board.RANKS * square_size)) \
            .convert_alpha()

        black = pygame.Color(125, 135, 150)
        white = pygame.Color(232, 235, 239)

        for rank in range(board.RANKS):
            square_y = rank * square_size
            for file in range(board.FILES):
                square = self.board.get_square(rank, file)
                square_x = file * square_size
                color = white if square.get_color() \
                    == board.SquareColor.WHITE else black
                square_coordinates = (
                    square_x,
                    square_y,
                    square_size,
                    square_size)
                pygame.draw.rect(board_surface, color, square_coordinates)
                piece = square.get_piece()
                if piece.get_kind() == board.Pieces.KING:
                    light_king, dark_king = self.chess_pieces.get_kings(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(light_king, (square_x, square_y))
                    else:
                        board_surface.blit(dark_king, (square_x, square_y))
                elif piece.get_kind() == board.Pieces.PAWN:
                    white_pawn, black_pawn = self.chess_pieces.get_pawns(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(white_pawn, (square_x, square_y))
                    else:
                        board_surface.blit(black_pawn, (square_x, square_y))
                elif piece.get_kind() == board.Pieces.QUEEN:
                    white_queen, black_queen = \
                        self.chess_pieces.get_queens(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(white_queen, (square_x, square_y))
                    else:
                        board_surface.blit(black_queen, (square_x, square_y))
                elif piece.get_kind() == board.Pieces.ROOK:
                    white_rook, black_rook = \
                        self.chess_pieces.get_rooks(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(white_rook, (square_x, square_y))
                    else:
                        board_surface.blit(black_rook, (square_x, square_y))
                elif piece.get_kind() == board.Pieces.BISHOP:
                    white_bishop, black_bishop = \
                        self.chess_pieces.get_bishops(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(white_bishop, (square_x, square_y))
                    else:
                        board_surface.blit(black_bishop, (square_x, square_y))
                elif piece.get_kind() == board.Pieces.KNIGHT:
                    white_knight, black_knight = \
                        self.chess_pieces.get_knights(.35)
                    if piece.get_color() == board.PieceColor.LIGHT:
                        board_surface.blit(white_knight, (square_x, square_y))
                    else:
                        board_surface.blit(black_knight, (square_x, square_y))
        return board_surface

    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode(
            (self.width, self.height))
        self.chess_pieces = sprites.ChessPieces()
        self.board_surface = self.draw_board()
        self.is_running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.display_surface.blit(self.board_surface, (0, 0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()
        while self.is_running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(60)
        self.on_cleanup()


if __name__ == '__main__':
    tiny_chess = TinyChess()
    tiny_chess.on_execute()
    exit(0)
