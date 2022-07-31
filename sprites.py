import pygame

WIDTH = 325
HEIGHT = 325


class ChessPieces():
    def __init__(self):
        self.sheet = pygame.image.load('assets/chess_pieces3.png') \
            .convert_alpha()

    def get_kings(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (20, 35, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (20, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2

    def get_pawns(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1720, 30, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1720, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2

    def get_queens(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (350, 20, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (350, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2

    def get_bishops(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (685, 20, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (685, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2

    def get_knights(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1025, 20, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1025, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2

    def get_rooks(self, scale):
        image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image.blit(self.sheet, (0, 0), (1390, 20, WIDTH, HEIGHT))
        image = pygame.transform.scale(image, (WIDTH * scale, HEIGHT * scale))
        image2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        image2.blit(self.sheet, (0, 0), (1390, 370, WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2,
                                        (WIDTH * scale, HEIGHT * scale))
        return image, image2
