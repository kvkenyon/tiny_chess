"""The game loop for Tiny Chess
"""
import pygame
import board


class TinyChess:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.size = self.is_running = True
        self.display_surface = None
        self.board_surface = None
        self.board = board.Board()

    def draw_board(self):
        square_size = 100
        board_surface = pygame.Surface(
            (board.FILES * square_size, board.RANKS * square_size))

        black = pygame.Color('black')
        white = pygame.Color('white')

        for x in range(board.RANKS):
            for y in range(board.FILES):
                square = self.board.get_square(x, y)
                color = white if square.get_color() \
                    == board.SquareColor.WHITE else black
                square = (
                    x * square_size,
                    y * square_size,
                    square_size,
                    square_size)
                pygame.draw.rect(board_surface, color, square)
        return board_surface

    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (self.width, self.height))
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
        self.on_cleanup()


if __name__ == '__main__':
    tiny_chess = TinyChess()
    tiny_chess.on_execute()
    exit(0)
