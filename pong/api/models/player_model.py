from .model import Model

class Player_model(Model):

    def __init__(self, username, id = None):
        super(Player_model, self).__init__()

        self.username = username
        self.id = id