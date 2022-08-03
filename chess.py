"""The game loop for Tiny Chess
"""
import pygame
import board


class TinyChess:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.size = self.is_running = True
        self.clock = None
        self.display_surface = None
        self.board_surface = None
        self.board = None

    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode(
            (self.width, self.height))
        self.board = board.Board()
        self.board_surface = self.board.draw()
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
