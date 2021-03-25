from circle import Circle
import pygame

class Balle(Circle):

    def __init__(self, screen, coords = (0, 0), speed = 1):
        super().__init__(screen, coords, speed)

        self.direction = "down"

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
            if(self.direction == "up"):
                self.direction = "down"
            elif self.direction == "up_left":
                self.direction = "down_left"
            elif self.direction == "up_right":
                self.direction = "down_right"
        elif y >= screen_size_y:
            if self.direction == "down":
                self.direction = "up"
            elif self.direction == "down_left":
                self.direction = "up_left"
            elif self.direction == "down_right":
                self.direction = "up_right"

        self.move(self.direction)
        super(Balle, self).update()
