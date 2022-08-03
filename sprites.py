import pygame

WIDTH = 325
HEIGHT = 325


class ChessPieces():
    def __init__(self):
        self.sheet = pygame.image.load('assets/chess_pieces3.png') \
            .convert_alpha()

    def get_kings(self, scale):
        width, height = 261, 264
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (36, 37, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 259, 263
        image2 = pygame.Surface((width, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (37, 371, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))

        return image, image2

    def get_pawns(self, scale):
        width, height = 185, 240
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1737, 60, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 185, 240
        image2 = pygame.Surface((width, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1737, 393, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))
        return image, image2

    def get_queens(self, scale):
        width, height = 289, 265
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (356, 33, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 287, 269
        image2 = pygame.Surface((width, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (356, 371, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))
        return image, image2

    def get_bishops(self, scale):
        width, height = 258, 261
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (704, 34, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 260, 261
        image2 = pygame.Surface((width, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (704, 367, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))
        return image, image2

    def get_knights(self, scale):
        width, height = 253, 251
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1037, 45, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 253, 249
        image2 = pygame.Surface((height, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1037, 381, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))
        return image, image2

    def get_rooks(self, scale):
        width, height = 211, 234
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1393, 60, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        width, height = 214, 235
        image2 = pygame.Surface((height, height)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1393, 393, width, height))
        image2 = pygame.transform.scale(image2,
                                        (width * scale, height * scale))
        return image, image2
