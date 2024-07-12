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
    
    def setKeyUp(self, key_up):
        self.key_up = key_up

    def setKeyUp(self, key_down):
        self.key_down = key_down

    def getKeyUp(self):
        return self.key_up
    
    def getKeyDown(self):
        return self.key_down
    
    def move(
        self,
        top_edge,
        bottom_edge,
    ):
        if self.checkCollision(top_edge, bottom_edge):
            if self.key_up:
                self.location[1] -= self.speed
            if self.key_down:
                self.location[1] += self.speed
    def checkCollision(self, min, max):
        if self.location[1] <= min or self.location[1] >= max:
            return False
        return True