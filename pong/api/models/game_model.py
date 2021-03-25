from .model import Model

class Game_model(Model):

    def __init__(self, name, players = [], id = None):
        super(Game_model, self).__init__()

        self.name = name
        self.id = id
        self.players = players