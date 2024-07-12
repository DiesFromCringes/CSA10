import pygame
class Main:
    def __init__(self, size, background, title, ball: Ball, paddle_1: Paddle, paddle_2: Paddle) -> None:
        pygame.init()
        self.size = size
        self.background = background
        self.title = title
        pygame.display.set_caption(self.title)
        self.canvas = pygame.display.set_mode(size=self.size)
        self.clock = pygame.time.Clock()

        self.ball = ball
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2

    def run(self):
        while True:
            events = pygame.event.get()  # bat su kien
            for e in events:
                # quit
                if e.type == pygame.QUIT:
                    return
                # keyboard check
                elif e.type == pygame.KEYDOWN:  # nhan phim
                    if e.key == pygame.K_w:
                        self.paddle_1.getKeyUp(True)
                    elif e.key == pygame.K_s:
                        self.paddle_1.getKeyDown(True)
                    elif e.key == pygame.K_UP:
                        self.paddle_2.getKeyUp(True)
                    elif e.key == pygame.K_DOWN:
                        self.paddle_2.getKeyDown(True)

    def drawCanvas(self):
        pass