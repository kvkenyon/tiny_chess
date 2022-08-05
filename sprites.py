import pygame


class ChessPieces():
    class ChessPiece(pygame.sprite.Sprite):
        def __init__(self, sprite_sheet, x, y, width, height, scale):
            super().__init__()
            self.image = pygame.Surface((width, height)).convert_alpha()
            self.image.blit(sprite_sheet, (0, 0), (x, y, width, height))
            self.image = pygame.transform.scale(self.image,
                                                (width * scale,
                                                 height * scale))
            self.rect = self.image.get_rect()

        def get_height(self):
            return self.image.get_height()

        def get_width(self):
            return self.image.get_width()

    def __init__(self):
        self.sheet = pygame.image.load('assets/chess_pieces3.png') \
            .convert_alpha()

    def get_white_king(self, scale):
        width, height = 261, 264
        x, y = 36, 37
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_king(self, scale):
        width, height = 259, 263
        x, y = 37, 371
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_kings(self, scale):
        return self.get_white_king(scale), self.get_black_king(scale)

    def get_white_pawn(self, scale):
        width, height = 185, 240
        x, y = 1737, 60
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_pawn(self, scale):
        width, height = 185, 240
        x, y = 1737, 393
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_pawns(self, scale):
        return self.get_white_pawn(scale), self.get_black_pawn(scale)

    def get_white_queen(self, scale):
        width, height = 289, 265
        x, y = 356, 33
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_queen(self, scale):
        width, height = 287, 269
        x, y = 356, 371
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_queens(self, scale):
        return self.get_white_queen(scale), self.get_black_queen(scale)

    def get_white_bishop(self, scale):
        width, height = 258, 261
        x, y = 704, 34
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_bishop(self, scale):
        width, height = 260, 261
        x, y = 704, 367
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_bishops(self, scale):
        return self.get_white_bishop(scale), self.get_black_bishop(scale)

    def get_white_knight(self, scale):
        width, height = 253, 251
        x, y = 1037, 45
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_knight(self, scale):
        width, height = 253, 249
        x, y = 1037, 381
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_knights(self, scale):
        return self.get_white_knight(scale), self.get_black_knight(scale)

    def get_white_rook(self, scale):
        width, height = 211, 234
        x, y = 1393, 60
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_black_rook(self, scale):
        width, height = 214, 235
        x, y = 1393, 393
        return self.ChessPiece(self.sheet, x, y, width, height,
                               scale)

    def get_rooks(self, scale):
        return self.get_white_rook(scale), self.get_black_rook(scale)
