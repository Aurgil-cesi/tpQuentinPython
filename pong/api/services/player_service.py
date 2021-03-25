from .service import Service

class Player_service(Service):

    def __init__(self, repository):
        super(Player_service, self).__init__(repository = repository, modelname = "player")

    def all(self):
        rows = self.repository.all()

        players = list(map(lambda row: self.modelClass(
            id = row[0],
            username = row[1]
        ), rows))

        return players

    def one(self, id):
        row = self.repository.one(id)

        if(row):
            return self.modelClass(
                id = row[0],
                username = row[1]
            )
        else:
            return None

    def create(self, player):
        self.repository.create(player)
