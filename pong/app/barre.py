from rectangle import Rectangle
from direction import Direction
import pygame

class Barre(Rectangle):

    def __init__(self, 
        screen, coords = (0, 0), size = (32, 64), speed = 1, 
        controls = {Direction.UP: pygame.K_z, Direction.DOWN: pygame.K_s}
    ):
        super().__init__(screen, coords, size, speed)

        self.direction = Direction.DOWN
        self.controls = controls

    def update(self):
        self.events()
        super(Barre, self).update()

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls[Direction.UP]]:
            self.move(Direction.UP)
        elif keys[self.controls[Direction.DOWN]]:
            self.move(Direction.DOWN)
