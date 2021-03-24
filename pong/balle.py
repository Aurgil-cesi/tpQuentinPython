from circle import Circle

class Balle(Circle):

    def __init__(self, screen, coords = (0, 0), move_size = 1):
        super().__init__(screen, coords, move_size)

        self.direction = "down"

    def update(self):

        (x, y) = self.coords
        (screen_size_x, screen_size_y) = self.screen.get_size()

        if x <= 0:
            self.direction = "right"
        elif x >= screen_size_x:
            self.direction = "left"
        elif y <= 0:
            self.direction = "down"
        elif y >= screen_size_y:
            self.direction = "up"

        self.move(self.direction)
        super(Balle, self).update()
