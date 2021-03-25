from rectangle import Rectangle
import pygame

class Barre(Rectangle):

    def __init__(self, 
        screen, coords = (0, 0), size = (32, 64), speed = 1, 
        controls = {"up": pygame.K_z, "down": pygame.K_s}
    ):
        super().__init__(screen, coords, size, speed)

        self.direction = "down"
        self.controls = controls

    def update(self):
        self.events()
        super(Barre, self).update()

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls["up"]]:
            self.move("up")
        elif keys[self.controls["down"]]:
            self.move("down")
