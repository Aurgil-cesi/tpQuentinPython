import pygame
from entity import Entity

class Circle(Entity):

    def __init__(self, screen, coords = (0, 0), speed = 1, size = 15):
        
        # x, y
        super(Circle, self).__init__(coords, speed)
        self.screen = screen
        self.size = size

    def update(self):
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            self.coords,
            self.size
        )

    def move(self, direction):
        super(Circle, self).move(direction)

        (x, y) = self.coords
        (screen_size_x, screen_size_y) = self.screen.get_size()
        if(x < 0):
            x = 0
        elif x > screen_size_x:
            x = screen_size_x
        elif y < 0:
            y = 0
        elif y > screen_size_y:
            y = screen_size_y

        self.coords = (x, y)