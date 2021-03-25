from circle import Circle
from direction import Direction
import pygame

class Balle(Circle):

    def __init__(self, screen, coords = (0, 0), speed = 1):
        super().__init__(screen, coords, speed)

        self.direction = Direction.DOWN

        self.dieLeftEvent = pygame.event.Event(pygame.USEREVENT, {"data": "left"});
        self.dieRightEvent = pygame.event.Event(pygame.USEREVENT, {"data": "right"});


    def update(self):

        (x, y) = self.coords
        (screen_size_x, screen_size_y) = self.screen.get_size()

        if x <= 0:
            pygame.event.post(self.dieLeftEvent)
        elif x >= screen_size_x:
            pygame.event.post(self.dieRightEvent)
        elif y <= 0:
            if(self.direction == Direction.UP):
                self.direction = Direction.DOWN
            elif self.direction == Direction.UP_LEFT:
                self.direction = Direction.DOWN_LEFT
            elif self.direction == Direction.UP_RIGHT:
                self.direction = Direction.DOWN_RIGHT
        elif y >= screen_size_y:
            if self.direction == Direction.DOWN:
                self.direction = Direction.UP
            elif self.direction == Direction.DOWN_LEFT:
                self.direction = Direction.UP_LEFT
            elif self.direction == Direction.DOWN_RIGHT:
                self.direction = Direction.UP_RIGHT

        self.move(self.direction)
        super(Balle, self).update()
