from rectangle import Rectangle

class Barre(Rectangle):

    def __init__(self, screen, coords = (0, 0), size = (32, 64), move_size = 0.5):
        super().__init__(screen, coords, size, move_size)

        self.direction = "down"

    # def update(self):
    #     super(Rectangle, self).update()
