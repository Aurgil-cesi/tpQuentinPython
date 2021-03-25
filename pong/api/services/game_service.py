from .service import Service

class Game_service(Service):

    def __init__(self, modelClass, repository):
        super(Game_service, self).__init__(modelClass, repository)

    def all(self):
        rows = self.repository.all()

        games = list(map(lambda row: self.modelClass(
            id = row[0],
            name = row[1]
        ), rows))

        return games

    def one(self, id):
        row = self.repository.one(id)

        if(row):
            return self.modelClass(
                id = row[0],
                name = row[1]
            )
        else:
            return None

    def create(self, game):
        self.repository.create(game)