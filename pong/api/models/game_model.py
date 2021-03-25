from .model import Model

class Game_model(Model):

    def __init__(self, name, id = None):
        super(Game_model, self).__init__()

        self.name = name
        self.id = id