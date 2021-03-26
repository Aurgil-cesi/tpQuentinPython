from .model import Model

class Cell_model(Model):

    def __init__(self, x, y, color):
        super(Cell_model, self).__init__()

        self.x = x
        self.y = y
        self.color = color