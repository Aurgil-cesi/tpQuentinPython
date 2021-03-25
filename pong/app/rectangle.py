import pygame
from entity import Entity

class Rectangle(Entity):

    def __init__(self, screen, coords = (0, 0), size = (32, 64), speed = 1):
        
        super(Rectangle, self).__init__(coords, speed)
        self.size = size
        self.screen = screen

    def update(self):
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (self.coords[0], self.coords[1], self.size[0], self.size[1])
        )

    def move(self, direction):
        super(Rectangle, self).move(direction)

        (x, y), (w, h) = self.coords, self.size
        (screen_size_x, screen_size_y) = self.screen.get_size()
        if(x < 0):
            x = 0
        elif x + w > screen_size_x:
            x = screen_size_x - w
        elif y < 0:
            y = 0
        elif y + h > screen_size_y:
            y = screen_size_y - h

        self.coords = (x, y)