import pygame
class Ball:
    def __init__(self, img_link, location, speed) -> None:
        self.speed = speed
        self.location = location
        self.img_url = pygame.image.load(img_link)
    
    def setLocation(self, location):
        self.location = location

    def setSpeed(self, speed):
        self.speed = speed

    def getLocation(self):
        return self.location

    def getSpeed(self):
        return self.speed   
    def move(
        self,
        paddle_1_min,
        paddle_1_max,
        paddle_2_min,
        paddle_2_max,
        top_edge,
        bottom_edge,


    ):
        self.location[0] += self.getSpeed([0])
        self.location[1] += self.getSpeed([1])

        self.checkCollision(paddle_1_min, paddle_1_max)
        self.checkCollision(paddle_2_min, paddle_2_max)

        self.checkCollision(top_edge, bottom_edge)

    def checkCollision(self, min, max):
        if self.getLocation([0]) <= min or self.getLocation([0]) >= max:
            self.setSpeed((-self.speed[0], self.speed[1]))
        if self.getLocation([1]) <= min or self.getLocation([0]) >= max:
            self.setSpeed((-self.speed[0], self.speed[1]))